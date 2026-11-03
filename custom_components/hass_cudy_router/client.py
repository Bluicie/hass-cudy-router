from __future__ import annotations

import hashlib
import logging
import time
from http.cookies import SimpleCookie
from typing import Any, Optional
from urllib.parse import quote_plus

import asyncio
import base64

import aiohttp
from aiohttp import ClientResponseError, ClientSession, TCPConnector
from bs4 import BeautifulSoup

_LOGGER = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 10


def encrypt_password_challenge(password: str, challenge: dict[str, Any]) -> str:
    """Build the luci_password value for newer Cudy firmware (e.g. 2.5.x).

    The login page first POSTs the username to /cgi-bin/luci/admin/login and
    receives {salt, kdfiter, nonce, key, cipher: "rsa-oaep", encode: "base64"}.
    The browser (sysauth.js) then computes:
        h = hex(PBKDF2-HMAC-SHA256(password, unhex(salt), kdfiter, 32))
        h = hex(SHA256(h + nonce))
        luci_password = base64(RSA-OAEP-SHA256(pubkey, h))
    PBKDF2 with ~1M iterations is CPU heavy: call this in an executor.
    """
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import padding

    salt = str(challenge["salt"])
    kdfiter = int(challenge.get("kdfiter") or 0)
    if kdfiter > 0:
        passhash = hashlib.pbkdf2_hmac(
            "sha256", password.encode(), bytes.fromhex(salt), kdfiter, 32
        ).hex()
    else:
        passhash = hashlib.sha256((password + salt).encode()).hexdigest()

    nonce = challenge.get("nonce")
    if nonce:
        passhash = hashlib.sha256((passhash + str(nonce)).encode()).hexdigest()

    public_key = serialization.load_pem_public_key(base64.b64decode(challenge["key"]))
    encrypted = public_key.encrypt(
        passhash.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    return base64.b64encode(encrypted).decode()


class CudyClient:

    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        *,
        use_https: bool = False,
        verify_ssl: bool = True,
        request_timeout: int = DEFAULT_TIMEOUT,
        session: ClientSession | None = None,
    ) -> None:
        self._host = host.rstrip("/")
        self._username = username
        self._password = password
        self._use_https = use_https
        self._verify_ssl = verify_ssl

        self._external_session = session is not None
        self._session: Optional[ClientSession] = session
        self._timeout = aiohttp.ClientTimeout(total=request_timeout)

        self._sysauth: str | None = None

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------
    @property
    def base_url(self) -> str:
        scheme = "https" if self._use_https else "http"
        return f"{scheme}://{self._host}"

    @property
    def is_authenticated(self) -> bool:
        return bool(self._sysauth)

    @property
    def sysauth(self) -> str | None:
        return self._sysauth

    # ------------------------------------------------------------------
    # Session handling
    # ------------------------------------------------------------------
    async def _ensure_session(self) -> ClientSession:
        if self._session is None or self._session.closed:
            connector = None
            # allow self-signed certs when verify_ssl=False
            if self._use_https and not self._verify_ssl:
                connector = TCPConnector(ssl=False)
            self._session = aiohttp.ClientSession(timeout=self._timeout, connector=connector)
        return self._session

    async def async_close(self) -> None:
        """Close the aiohttp session (called on HA unload)."""
        if self._session and not self._session.closed and not self._external_session:
            await self._session.close()
        self._session = None

    # backwards compat alias
    async def close(self) -> None:
        await self.async_close()

    # ------------------------------------------------------------------
    # Authentication (LuCI)
    # ------------------------------------------------------------------
    async def authenticate(self) -> bool:
        """Authenticate using the LuCI login form and set sysauth cookie."""

        session = await self._ensure_session()

        # try preferred scheme first, then fallback
        schemes = ["https", "http"] if self._use_https else ["http", "https"]

        for scheme in schemes:
            base = f"{scheme}://{self._host}"
            login_url = f"{base}/cgi-bin/luci"

            headers_get = {
                "User-Agent": "hass-cudy-router",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            }
            headers_post = {
                "User-Agent": "hass-cudy-router",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": login_url,
                "Origin": base,
            }

            # 1) GET login page
            try:
                async with session.get(login_url, headers=headers_get, allow_redirects=True) as resp:
                    html = await resp.text()
            except Exception as e:
                _LOGGER.error("GET login page failed (%s): %s", scheme, e)
                continue

            if not html:
                _LOGGER.error("GET login page failed (%s): empty response", scheme)
                continue

            soup = BeautifulSoup(html, "html.parser")

            def extract(name: str) -> str:
                tag = soup.find("input", {"name": name})
                if tag and tag.has_attr("value"):
                    return str(tag["value"])
                # some firmwares put them in <meta>
                meta = soup.find("meta", {"name": name})
                if meta and meta.has_attr("content"):
                    return str(meta["content"])
                return ""

            _csrf = extract("_csrf")
            token = extract("token")
            salt = extract("salt")

            # 2) compute password
            luci_password = self._password
            challenge = await self._fetch_login_challenge(session, base, headers_post)
            if challenge:
                # newer firmware: PBKDF2 + nonce + RSA-OAEP (sysauth.js)
                try:
                    luci_password = await asyncio.get_running_loop().run_in_executor(
                        None, encrypt_password_challenge, self._password, challenge
                    )
                except Exception as e:  # noqa: BLE001
                    _LOGGER.error("Building encrypted login failed (%s): %s", scheme, e)
                    continue
                salt = token = ""
            elif salt:
                hashed = hashlib.sha256((self._password + salt).encode()).hexdigest()
                if token:
                    hashed = hashlib.sha256((hashed + token).encode()).hexdigest()
                luci_password = hashed

            # 3) POST credentials
            body: dict[str, Any] = {
                "_csrf": _csrf,
                "token": token,
                "salt": salt,
                "zonename": "UTC",
                "timeclock": str(int(time.time())),
                "luci_language": "en",
                "luci_username": self._username,
                "luci_password": luci_password,
                "submit": "1",
            }
            body = {k: v for k, v in body.items() if v}

            encoded = "&".join(f"{quote_plus(k)}={quote_plus(str(v))}" for k, v in body.items())

            try:
                async with session.post(
                    login_url,
                    headers=headers_post,
                    data=encoded,
                    allow_redirects=False,
                ) as resp:
                    # try Set-Cookie header first
                    set_cookie = resp.headers.getall("Set-Cookie", [])
                    sysauth = self._parse_sysauth_from_headers(set_cookie)
                    if sysauth:
                        self._sysauth = sysauth
                        return True

                    # fallback to cookie jar
                    jar = session.cookie_jar.filter_cookies(base)
                    for key, cookie in jar.items():
                        if key.lower().startswith("sysauth") and cookie.value:
                            self._sysauth = cookie.value
                            return True
            except Exception as e:
                _LOGGER.error("POST login failed (%s): %s", scheme, e)
                continue

        _LOGGER.debug("Authentication failed: no sysauth cookie obtained")
        return False

    async def _fetch_login_challenge(
        self, session: ClientSession, base: str, headers: dict[str, str]
    ) -> dict[str, Any] | None:
        """Ask newer firmware for its login challenge; None on older firmware."""
        try:
            async with session.post(
                f"{base}/cgi-bin/luci/admin/login",
                headers={**headers, "Accept": "application/json, */*"},
                data={"username": self._username},
                allow_redirects=False,
            ) as resp:
                if resp.status != 200:
                    return None
                data = await resp.json(content_type=None)
        except Exception:  # noqa: BLE001 - not JSON / not supported
            return None
        if isinstance(data, dict) and data.get("salt") and data.get("key"):
            if data.get("nonce"):
                return data
            _LOGGER.error(
                "Router reports no admin password set yet (no nonce); "
                "finish the setup wizard in the web UI first"
            )
        return None

    @staticmethod
    def _parse_sysauth_from_headers(set_cookie_headers: list[str]) -> str | None:
        for hdr in set_cookie_headers:
            cookie = SimpleCookie()
            cookie.load(hdr)
            for key in ("sysauth", "sysauth_http", "sysauth_https"):
                morsel = cookie.get(key)
                if morsel and morsel.value:
                    return morsel.value
        return None

    async def ensure_authenticated(self) -> None:
        if not self.is_authenticated:
            ok = await self.authenticate()
            if not ok:
                raise RuntimeError("Authentication failed")

    # ------------------------------------------------------------------
    # Generic request helpers
    # ------------------------------------------------------------------
    async def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any = None,
        data: Any = None,
        require_auth: bool = True,
    ) -> Any:
        """Low-level request helper used by get/post and APIs."""

        if not path.startswith("/"):
            path = "/" + path

        if require_auth:
            await self.ensure_authenticated()

        session = await self._ensure_session()
        url = f"{self.base_url}{path}"

        headers: dict[str, str] = {
            "User-Agent": "hass-cudy-router",
            "Accept": "*/*",
        }
        if self.sysauth:
            headers["Cookie"] = f"sysauth={self.sysauth}"

        async with session.request(
            method,
            url,
            params=params,
            json=json,
            data=data,
            headers=headers,
        ) as resp:
            if resp.status == 403 and require_auth:
                await self.authenticate()
                headers["Cookie"] = f"sysauth={self.sysauth}" if self.sysauth else ""
                async with session.request(
                    method,
                    url,
                    params=params,
                    json=json,
                    data=data,
                    headers=headers,
                ) as resp2:
                    resp2.raise_for_status()
                    ctype = resp2.headers.get("Content-Type", "")
                    if "application/json" in ctype:
                        return await resp2.json(content_type=None)
                    return await resp2.text()

            try:
                resp.raise_for_status()
            except ClientResponseError as err:
                return ""

            ctype = resp.headers.get("Content-Type", "")
            if "application/json" in ctype:
                return await resp.json(content_type=None)
            return await resp.text()

    async def get(self, path: str, **kwargs: Any) -> Any:
        return await self.request("GET", path, **kwargs)

    async def post(self, path: str, **kwargs: Any) -> Any:
        return await self.request("POST", path, **kwargs)

    async def get_json(self, path: str, **kwargs: Any) -> Any:
        """Explicit JSON helper if a caller wants JSON only."""
        result = await self.request("GET", path, **kwargs)
        return result

    # ------------------------------------------------------------------
    # LuCI convenience helpers
    # ------------------------------------------------------------------
    async def luci_get(self, luci_path: str) -> str:
        """GET a LuCI path like '/admin/status/overview'."""
        if not luci_path.startswith("/"):
            luci_path = "/" + luci_path
        return await self.get(f"/cgi-bin/luci{luci_path}")

    async def luci_post(self, luci_path: str, data: dict[str, Any] | None = None) -> str:
        """POST to a LuCI path like '/admin/system/reboot'."""
        if not luci_path.startswith("/"):
            luci_path = "/" + luci_path
        return await self.post(f"/cgi-bin/luci{luci_path}", data=data)

    async def ping(self) -> bool:
        """Quick connectivity check."""
        try:
            await self.get("/cgi-bin/luci", require_auth=False)
            return True
        except Exception:
            return False

    # ------------------------------------------------------------------
    # Helper for tests / convenience
    # ------------------------------------------------------------------
    @classmethod
    def from_entry(cls, entry) -> "CudyClient":
        data = entry.data
        protocol = (data.get("protocol") or "http").lower()
        use_https = protocol == "https"
        return cls(
            host=data.get("host"),
            username=data.get("username"),
            password=data.get("password"),
            use_https=use_https,
        )
from __future__ import annotations

from typing import Any

from aiohttp import ClientResponseError

from .client import CudyClient
from .const import *
from .parser import parse_html


class CudyApi:
    def __init__(self, client: CudyClient) -> None:
        self._client = client

    @staticmethod
    def luci(path: str) -> str:
        if not path.startswith("/"):
            path = "/" + path
        return "/cgi-bin/luci" + path

    async def get_data(self) -> dict[str, Any]:
        out: dict[str, Any] = {}

        for module, urls in CAPABILITY_URLS.items():
            # try each known URL until one yields data (paths differ per model)
            for url in urls:
                try:
                    html = await self._client.get(self.luci(url))
                except ClientResponseError:
                    continue  # module not present at this path
                if not html:
                    continue
                data = parse_html(module, html)
                if data:
                    out[module] = data
                    break
        return out

    async def reboot(self) -> None:
        await self._client.post(self.luci("/admin/system/reboot"), data={"reboot": "1"})
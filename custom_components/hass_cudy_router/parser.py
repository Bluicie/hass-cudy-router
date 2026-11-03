# custom_components/hass_cudy_router/parsers.py
from __future__ import annotations

from typing import Any, Optional
import re

from bs4 import BeautifulSoup

from custom_components.hass_cudy_router.const import (
    SENSORS,
    SENSORS_KEY_KEY,
    SENSORS_KEY_DESCRIPTION,
    SENSORS_KEY_CLASS,
    SensorStateClass,
    MODULE_DEVICES,
    MODULE_DEVICE_LIST,
)

# ---- Helpers ---------------------------------------------------------------

def _clean(s: str | None) -> str:
    return " ".join((s or "").split()).strip()

def _to_int_if_possible(value: str | None) -> Optional[int]:
    if value is None:
        return None
    value = _clean(value)
    if value == "":
        return None
    try:
        return int(value)
    except ValueError:
        m = re.search(r"(\d+)", value)
        return int(m.group(1)) if m else None


def extract_kv_pairs(html: str) -> dict[str, str]:
    """
    Best-effort extraction of "Label" -> "Value" from a LuCI status page.
    Supports table (tr/td or tr/th) and dl/dt/dd.
    """
    out: dict[str, str] = {}
    if not html:
        return out

    soup = BeautifulSoup(html, "html.parser")

    # Tables
    for table in soup.find_all("table"):
        for tr in table.find_all("tr"):
            cells = tr.find_all(["th", "td"])
            if len(cells) < 2:
                continue
            # Cudy layouts vary: [label, value, (empty)] or [icon, label, value].
            # Take the first two cells that carry text; prefer the first <p>
            # (pages render the same text twice for desktop/mobile).
            texts: list[str] = []
            for cell in cells:
                p = cell.find("p")
                t = _clean(p.get_text() if p else cell.get_text())
                if t:
                    texts.append(t)
            if len(texts) < 2:
                continue
            if len(texts) > 2 and all(c.name == "th" for c in cells):
                continue  # multi-column table header (SSID | Encryption | ...)
            k, v = texts[0], texts[1]
            if k:
                if k not in out.keys():
                    out[k] = v

    # dl/dt/dd
    for dl in soup.find_all("dl"):
        dts = dl.find_all("dt")
        dds = dl.find_all("dd")
        for dt, dd in zip(dts, dds):
            k = _clean(dt.get_text())
            v = _clean(dd.get_text())
            if k:
                out[k] = v

    return out


def extract_xhr_endpoints(html: str) -> dict[str, dict[str, str]]:
    """
    Extract endpoints from pages that use cbi_xhr_load.
    Returns: { "/cgi-bin/luci/...": {"args": "nomodal=&iface=4g"} , ... }
    """
    endpoints: dict[str, dict[str, str]] = {}
    if not html:
        return endpoints

    soup = BeautifulSoup(html, "html.parser")
    scripts = soup.find_all("script")

    # Matches: cbi_xhr_load(..., '/cgi-bin/luci/admin/...', 'argstring');
    re_load = re.compile(
        r"cbi_xhr_load\([^\)]*'([^']+)'(?:\s*,\s*'([^']*)')?\)",
        re.MULTILINE,
    )

    for script in scripts:
        text = script.string or script.get_text()
        if not text:
            continue
        for m in re_load.finditer(text):
            url = m.group(1)
            args = m.group(2) or ""
            endpoints[url] = {"args": args}

    return endpoints


def parse_module_by_sensors(module: str, html: str) -> dict[str, Any]:
    sensors = SENSORS.get(module, [])
    kv = extract_kv_pairs(html)

    # case-insensitive lookup
    kv_lower = {k.lower(): v for k, v in kv.items()}

    result: dict[str, Any] = {}
    for spec in sensors:
        sensor_key = spec[SENSORS_KEY_KEY]
        labels: list[str] = spec.get(SENSORS_KEY_DESCRIPTION, []) or []

        found: str | None = None
        for label in labels:
            label = _clean(label)
            if not label:
                continue
            if label in kv:
                found = kv[label]
                break
            low = label.lower()
            if low in kv_lower:
                found = kv_lower[low]
                break

        state_class = spec.get(SENSORS_KEY_CLASS)
        if state_class == SensorStateClass.MEASUREMENT:
            result[sensor_key] = _to_int_if_possible(found)
        else:
            result[sensor_key] = _clean(found) if found else None

    return result


# ---- Special: Devices summary (combines both variants) ---------------------

def parse_devices(html: str) -> dict[str, Any]:
    """
    Combines:
    - label/value rows (Online/Blocked, etc.)
    - thead "Devices | N" total
    - per-type rows like 2.4G / 5G / Wired / Mesh
    Still uses parse_module_by_sensors for initial fill.
    """
    from custom_components.hass_cudy_router.const import (
        SENSOR_DEVICE_COUNT,
        SENSOR_DEVICE_ONLINE,
        SENSOR_DEVICE_BLOCKED,
        SENSOR_DEVICE_WIFI_24_COUNT,
        SENSOR_DEVICE_WIFI_5_COUNT,
        SENSOR_DEVICE_WIRED_COUNT,
        SENSOR_DEVICE_MESH_COUNT,
    )

    result = parse_module_by_sensors(MODULE_DEVICES, html)

    if not html:
        return result

    soup = BeautifulSoup(html, "html.parser")
    table = soup.select_one("table.table")
    if not table:
        return result

    # Total count often in THEAD: "Devices | 12"
    thead = table.find("thead")
    if thead:
        ths = [_clean(th.get_text()) for th in thead.find_all("th")]
        if len(ths) >= 2 and ths[0].lower().startswith("devices"):
            result[SENSOR_DEVICE_COUNT] = _to_int_if_possible(ths[1])

    # Per-type + online/blocked in TBODY
    tbody = table.find("tbody")
    if tbody:
        for tr in tbody.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) < 2:
                continue

            label = _clean(tds[0].get_text())
            value = _to_int_if_possible(_clean(tds[1].get_text()))
            if value is None:
                continue

            ll = label.lower()

            if ll in ("online", "online devices", "connected"):
                result[SENSOR_DEVICE_ONLINE] = value
                continue
            if ll in ("blocked", "blocked devices"):
                result[SENSOR_DEVICE_BLOCKED] = value
                continue

            if "2.4" in ll:
                result[SENSOR_DEVICE_WIFI_24_COUNT] = value
            elif "5g" in ll or "5ghz" in ll or "5 ghz" in ll:
                result[SENSOR_DEVICE_WIFI_5_COUNT] = value
            elif "wired" in ll or "ethernet" in ll or ll == "lan":
                result[SENSOR_DEVICE_WIRED_COUNT] = value
            elif "mesh" in ll:
                result[SENSOR_DEVICE_MESH_COUNT] = value

    return result


# ---- Special: Device list (devlist) ---------------------------------------

_UP_RE = re.compile(r"↑\s*([\d.]+)\s*([A-Za-z/]+)")
_DOWN_RE = re.compile(r"↓\s*([\d.]+)\s*([A-Za-z/]+)")

def parse_device_list(html: str) -> list[dict[str, Any]]:
    """
    Parses /admin/network/devices/devlist
    Returns list of dicts keyed by DEVICE_* constants.
    """
    from custom_components.hass_cudy_router.const import (
        DEVICE_HOSTNAME,
        DEVICE_IP,
        DEVICE_MAC,
        DEVICE_UPLOAD_SPEED,
        DEVICE_DOWNLOAD_SPEED,
        DEVICE_SIGNAL,
        DEVICE_ONLINE_TIME,
        DEVICE_CONNECTION_TYPE,
    )

    out: list[dict[str, Any]] = []
    if not html:
        return out

    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_=re.compile(r"\btable\b"))
    if not table:
        return out

    for row in table.select("tbody tr[id^='cbi-table-']"):
        cols = row.find_all("td")
        if len(cols) < 6:
            continue

        hostname = None
        conn_type = None
        ip = None
        mac = None
        upload = None
        download = None
        signal = None
        online = None

        # hostname + conn type
        if len(cols) > 1:
            host_p = cols[1].find("p", class_=re.compile(r"\bhidden-xs\b"))
            if host_p:
                parts = [t.strip() for t in host_p.stripped_strings]
                if parts:
                    hostname = parts[0]
                if len(parts) > 1:
                    conn_type = parts[1]

        # ip + mac
        if len(cols) > 4:
            ipmac_p = cols[4].find("p", class_=re.compile(r"\bhidden-xs\b"))
            if ipmac_p:
                parts = [t.strip() for t in ipmac_p.stripped_strings]
                if parts:
                    ip = parts[0]
                if len(parts) > 1:
                    mac = parts[1]

        # speeds
        if len(cols) > 5:
            speed_p = cols[5].find("p", class_=re.compile(r"\bhidden-xs\b"))
            if speed_p:
                txt = speed_p.get_text(" ")
                up_m = _UP_RE.search(txt)
                down_m = _DOWN_RE.search(txt)
                if up_m:
                    upload = f"{up_m.group(1)}{up_m.group(2)}"
                if down_m:
                    download = f"{down_m.group(1)}{down_m.group(2)}"

        # signal + online time
        if len(cols) > 6:
            sig_p = cols[6].find("p", class_=re.compile(r"\bhidden-xs\b"))
            if sig_p:
                signal = _clean(sig_p.get_text())
        if len(cols) > 7:
            on_p = cols[7].find("p", class_=re.compile(r"\bhidden-xs\b"))
            if on_p:
                online = _clean(on_p.get_text())

        out.append(
            {
                DEVICE_HOSTNAME: hostname,
                DEVICE_IP: ip,
                DEVICE_MAC: mac,
                DEVICE_UPLOAD_SPEED: upload,
                DEVICE_DOWNLOAD_SPEED: download,
                DEVICE_SIGNAL: signal,
                DEVICE_ONLINE_TIME: online,
                DEVICE_CONNECTION_TYPE: conn_type,
            }
        )

    return out


# ---- Dispatcher ------------------------------------------------------------

def parse_html(module: str, html: str) -> Any:
    """
    Single entrypoint:
    - returns dict of sensor values for a module
    - returns list for MODULE_DEVICE_LIST
    - returns {"xhr_endpoints": ...} if module page is an XHR shell
    """
    if not html:
        return [] if module == MODULE_DEVICE_LIST else {}

    # XHR shell detection (important for gsm/sms sometimes)
    xhr = extract_xhr_endpoints(html)
    if xhr:
        # let API fetch each xhr endpoint and parse those fragments separately
        return {"xhr_endpoints": xhr}

    if module == MODULE_DEVICES:
        return parse_devices(html)

    if module == MODULE_DEVICE_LIST:
        return parse_device_list(html)

    # default driven purely by SENSORS descriptors
    return parse_module_by_sensors(module, html)
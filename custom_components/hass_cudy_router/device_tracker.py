from __future__ import annotations

from typing import Any

from homeassistant.components.device_tracker import ScannerEntity, SourceType
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import *
from .coordinator import CudyCoordinator


def _device_unique_id(entry_id: str, mac: str) -> str:
    mac_norm = (mac or "").strip().lower().replace(":", "")
    return f"{entry_id}_dev_{mac_norm}"


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    data = hass.data[DOMAIN][entry.entry_id]
    coordinator: CudyCoordinator = data["coordinator"]
    spec = data.get("spec")
    if spec and "device_tracker" not in getattr(spec, "platforms", set()):
        return
    known: set[str] = set()

    @callback
    def _add_new_devices() -> None:
        new = []
        for dev in _get_devices(coordinator.data):
            mac = str(dev.get(DEVICE_MAC)).strip().lower()
            if mac not in known:
                known.add(mac)
                new.append(CudyDeviceTracker(coordinator, entry, dev))
        if new:
            async_add_entities(new)

    _add_new_devices()
    # clients that show up later get an entity too
    entry.async_on_unload(coordinator.async_add_listener(_add_new_devices))


def _get_devices(coordinator_data: dict[str, Any] | None) -> list[dict[str, Any]]:
    if not coordinator_data:
        return []
    # api.get_data() returns the list at top level; older code nested it
    devs = coordinator_data.get(MODULE_DEVICE_LIST)
    if not devs:
        mod = coordinator_data.get(MODULE_DEVICES, {}) or {}
        devs = mod.get(MODULE_DEVICE_LIST, []) if isinstance(mod, dict) else []
    return [
        d for d in devs or []
        if isinstance(d, dict) and d.get(DEVICE_MAC)
    ]


class CudyDeviceTracker(CoordinatorEntity, ScannerEntity):
    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: CudyCoordinator,
        entry: ConfigEntry,
        device: dict[str, Any],
    ) -> None:
        super().__init__(coordinator)
        self._entry = entry
        self._initial = device  # IMPORTANT fallback for attributes
        self._mac = str(device.get(DEVICE_MAC) or "").strip()
        hostname = (device.get(DEVICE_HOSTNAME) or "").strip()
        if hostname.lower() in ("", "unknown", "*"):
            hostname = ""
        self._attr_name = hostname or self._mac
        self._attr_unique_id = _device_unique_id(entry.entry_id, self._mac)

    @property
    def source_type(self) -> SourceType:
        return SourceType.ROUTER

    @property
    def mac_address(self) -> str | None:
        return self._mac or None

    @property
    def ip_address(self) -> str | None:
        dev = self._find_self()
        ip = (dev.get(DEVICE_IP) if dev else None) or None
        return str(ip) if ip else None

    @property
    def is_connected(self) -> bool:
        dev = self._find_self()
        if not dev:
            return False
        return True

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        dev = self._find_self()
        if dev is None:
            dev = self._initial
        return dev if isinstance(dev, dict) else None

    def _find_self(self) -> dict[str, Any] | None:
        devices = _get_devices(getattr(self.coordinator, "data", None))
        for d in devices:
            if str(d.get(DEVICE_MAC) or "").strip().lower() == self._mac.lower():
                return d
        return None
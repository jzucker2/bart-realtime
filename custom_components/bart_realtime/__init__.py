"""
Custom integration to integrate Bart Realtime with Home Assistant.

For more details about this integration, please refer to
https://github.com/jzucker2/bart-realtime
"""

import asyncio
from dataclasses import dataclass
from datetime import timedelta
import logging
from typing import NamedTuple

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Config, HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import BartRealtimeApiClient
from .const import CONF_API_KEY, CONF_STATION, DOMAIN, PLATFORMS, STARTUP_MESSAGE
from .coordinator import BartRealtimeDataUpdateCoordinator

SCAN_INTERVAL = timedelta(seconds=30)

_LOGGER: logging.Logger = logging.getLogger(__package__)


# The type alias needs to be suffixed with 'ConfigEntry'
type BartRealtimeConfigEntry = ConfigEntry[BartRealtimeData]


class BartCoordinators(NamedTuple):
    """Tuya data stored in the Home Assistant data object."""

    trains_coordinator: BartRealtimeDataUpdateCoordinator


@dataclass
class BartRealtimeData:
    api_key: str
    station: str
    client: BartRealtimeApiClient

    @classmethod
    def from_entry(cls, entry: BartRealtimeConfigEntry, session):
        _LOGGER.debug(
            "Processing data config entry: %s with entry.data: %s", entry, entry.data
        )
        api_key = entry.data.get(CONF_API_KEY)
        station = entry.data.get(CONF_STATION)

        client = BartRealtimeApiClient(api_key, station, session)

        return cls(api_key=api_key, station=station, client=client)


async def async_setup(hass: HomeAssistant, config: Config):
    """Set up this integration using YAML is not supported."""
    return True


async def async_setup_entry(
    hass: HomeAssistant,
    entry: BartRealtimeConfigEntry,
):
    """Set up this integration using UI."""
    if hass.data.get(DOMAIN) is None:
        hass.data.setdefault(DOMAIN, {})
        _LOGGER.info(STARTUP_MESSAGE)

    session = async_get_clientsession(hass)
    data = BartRealtimeData.from_entry(entry, session)

    # Assign the runtime_data
    entry.runtime_data = data

    coordinator = BartRealtimeDataUpdateCoordinator(hass, client=data.client)
    await coordinator.async_refresh()

    if not coordinator.last_update_success:
        raise ConfigEntryNotReady

    hass.data[DOMAIN][entry.entry_id] = coordinator

    coordinator.set_platforms(PLATFORMS)
    # https://developers.home-assistant.io/blog/2024/03/13/deprecate_add_run_job
    hass.async_add_job(hass.config_entries.async_forward_entry_setups(entry, PLATFORMS))

    entry.add_update_listener(async_reload_entry)
    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: BartRealtimeConfigEntry,
) -> bool:
    """Handle removal of an entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    unloaded = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
                if platform in coordinator.platforms
            ]
        )
    )
    if unloaded:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unloaded


async def async_reload_entry(
    hass: HomeAssistant,
    entry: BartRealtimeConfigEntry,
) -> None:
    """Reload config entry."""
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)

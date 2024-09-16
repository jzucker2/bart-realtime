"""
Custom integration to integrate Bart Realtime with Home Assistant.

For more details about this integration, please refer to
https://github.com/jzucker2/bart-realtime
"""

import asyncio
from dataclasses import dataclass
from datetime import timedelta
import logging
from typing import NamedTuple, Optional

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


class BartUpdateCoordinators(NamedTuple):
    """Bart update coordinators stored in the Home Assistant runtime_data object."""

    trains_coordinator: BartRealtimeDataUpdateCoordinator


@dataclass
class BartRealtimeData:
    api_key: str
    station: str
    client: BartRealtimeApiClient
    coordinators: Optional[BartUpdateCoordinators] = None

    @classmethod
    def from_entry(cls, entry: BartRealtimeConfigEntry, session):
        _LOGGER.debug(
            "Processing data config entry: %s with entry.data: %s", entry, entry.data
        )
        api_key = entry.data.get(CONF_API_KEY)
        station = entry.data.get(CONF_STATION)

        client = BartRealtimeApiClient(api_key, station, session)
        return cls(api_key=api_key, station=station, client=client)

    def set_coordinators(self, trains_update_coordinator):
        self.coordinators = BartUpdateCoordinators(
            train_update_coordinator=trains_update_coordinator,
        )


async def async_setup(hass: HomeAssistant, config: Config):
    """Set up this integration using YAML is not supported."""
    return True


async def async_setup_entry(
    hass: HomeAssistant,
    entry: BartRealtimeConfigEntry,
):
    """Set up this integration using UI."""
    if entry.runtime_data is None:
        _LOGGER.info(STARTUP_MESSAGE)

    session = async_get_clientsession(hass)
    data = BartRealtimeData.from_entry(entry, session)

    # Assign the runtime_data
    entry.runtime_data = data

    trains_coordinator = BartRealtimeDataUpdateCoordinator(hass, client=data.client)
    await trains_coordinator.async_refresh()

    if not trains_coordinator.last_update_success:
        raise ConfigEntryNotReady

    # hass.data[DOMAIN][entry.entry_id] = trains_coordinator
    data.set_coordinators(trains_coordinator)

    trains_coordinator.set_platforms(PLATFORMS)
    # https://developers.home-assistant.io/blog/2024/03/13/deprecate_add_run_job
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

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
    await hass.config_entries.async_reload(entry.entry_id)

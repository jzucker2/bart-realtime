"""
Custom integration to integrate Bart Realtime with Home Assistant.

For more details about this integration, please refer to
https://github.com/jzucker2/bart-realtime
"""

from dataclasses import dataclass
from datetime import timedelta
import logging
from typing import NamedTuple

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Config, HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.reload import async_setup_reload_service

from .api import BartRealtimeApiClient
from .const import CONF_API_KEY, CONF_STATION, DOMAIN, PLATFORMS
from .coordinator import (
    BartRealtimeAnnouncementsDataUpdateCoordinator,
    BartRealtimeTrainsDataUpdateCoordinator,
)

CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN)

SCAN_INTERVAL = timedelta(seconds=30)

_LOGGER: logging.Logger = logging.getLogger(__package__)


# The type alias needs to be suffixed with 'ConfigEntry'
type BartRealtimeConfigEntry = ConfigEntry[BartRealtimeData]


class BartUpdateCoordinators(NamedTuple):
    """Bart update coordinators stored in the Home Assistant runtime_data object."""

    trains_coordinator: BartRealtimeTrainsDataUpdateCoordinator
    announcements_coordinator: BartRealtimeAnnouncementsDataUpdateCoordinator


@dataclass
class BartRealtimeEntryConfigData:
    api_key: str
    station: str

    @classmethod
    def from_entry(cls, entry: BartRealtimeConfigEntry):
        _LOGGER.debug(
            "Processing data config entry: %s with entry.data: %s", entry, entry.data
        )
        api_key = entry.data.get(CONF_API_KEY)
        station = entry.data.get(CONF_STATION)
        return cls(api_key=api_key, station=station)


@dataclass
class BartRealtimeData:
    entry_config_data: BartRealtimeEntryConfigData
    client: BartRealtimeApiClient
    coordinators: BartUpdateCoordinators

    @classmethod
    def from_entry(cls, hass, entry_config_data: BartRealtimeEntryConfigData):
        _LOGGER.debug("Processing data config entry_config_data: %s", entry_config_data)

        session = async_get_clientsession(hass)

        client = BartRealtimeApiClient(
            entry_config_data.station, session, api_key=entry_config_data.api_key
        )

        trains_coordinator = BartRealtimeTrainsDataUpdateCoordinator(hass, client)
        announcements_coordinator = BartRealtimeAnnouncementsDataUpdateCoordinator(
            hass, client
        )
        coordinators = BartUpdateCoordinators(
            trains_coordinator=trains_coordinator,
            announcements_coordinator=announcements_coordinator,
        )

        return cls(
            entry_config_data=entry_config_data,
            client=client,
            coordinators=coordinators,
        )

    @property
    def trains_coordinator(self):
        return self.coordinators.trains_coordinator

    @property
    def announcements_coordinator(self):
        return self.coordinators.announcements_coordinator


async def async_setup(hass: HomeAssistant, config: Config):
    """Set up this integration using YAML is not supported."""
    return True


async def async_setup_entry(
    hass: HomeAssistant,
    entry: BartRealtimeConfigEntry,
):
    """Set up this integration using UI."""
    # if entry.runtime_data is None:
    #     _LOGGER.info(STARTUP_MESSAGE)

    entry_config_data = BartRealtimeEntryConfigData.from_entry(entry)

    data = BartRealtimeData.from_entry(hass, entry_config_data)

    # Assign the runtime_data
    entry.runtime_data = data

    await async_setup_reload_service(hass, DOMAIN, PLATFORMS)

    async def _set_up_coordinator(coordinator):
        await coordinator.async_refresh()

        if not coordinator.last_update_success:
            raise ConfigEntryNotReady

        coordinator.set_platforms(PLATFORMS)

    trains_coordinator = data.trains_coordinator
    await _set_up_coordinator(trains_coordinator)

    announcements_coordinator = data.announcements_coordinator
    await _set_up_coordinator(announcements_coordinator)

    # Set up all platforms for this device/entry.
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Reload entry when its updated.
    entry.async_on_unload(entry.add_update_listener(async_reload_entry))
    return True


async def async_unload_entry(
    hass: HomeAssistant,
    entry: BartRealtimeConfigEntry,
) -> bool:
    """Handle removal of an entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        _LOGGER.debug(
            "Unloading platforms entry: %s with unload_ok: %s", entry, unload_ok
        )

    return unload_ok


async def async_reload_entry(
    hass: HomeAssistant,
    entry: BartRealtimeConfigEntry,
) -> None:
    """Reload config entry."""
    await hass.config_entries.async_reload(entry.entry_id)

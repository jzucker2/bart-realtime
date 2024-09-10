"""
Custom integration to integrate Bart Realtime with Home Assistant.

For more details about this integration, please refer to
https://github.com/jzucker2/bart-realtime
"""

import asyncio
from dataclasses import dataclass
from datetime import timedelta
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import Config, HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import BartRealtimeApiClient
from .const import (
    CONF_API_KEY,
    CONF_STATION,
    DOMAIN,
    MISSING_VALUE,
    PLATFORMS,
    STARTUP_MESSAGE,
)

SCAN_INTERVAL = timedelta(seconds=30)

_LOGGER: logging.Logger = logging.getLogger(__package__)


# The type alias needs to be suffixed with 'ConfigEntry'
type BartRealtimeConfigEntry = ConfigEntry[BartRealtimeData]


@dataclass
class BartRealtimeData:
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
    data = BartRealtimeData.from_entry(entry)
    client = BartRealtimeApiClient(data.api_key, data.station, session)

    coordinator = BartRealtimeDataUpdateCoordinator(hass, client=client)
    await coordinator.async_refresh()

    if not coordinator.last_update_success:
        raise ConfigEntryNotReady

    hass.data[DOMAIN][entry.entry_id] = coordinator

    coordinator.set_platforms(PLATFORMS)
    # https://developers.home-assistant.io/blog/2024/03/13/deprecate_add_run_job
    hass.async_add_job(hass.config_entries.async_forward_entry_setups(entry, PLATFORMS))

    entry.add_update_listener(async_reload_entry)
    return True


class BartRealtimeDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the API."""

    def __init__(
        self,
        hass: HomeAssistant,
        client: BartRealtimeApiClient,
    ) -> None:
        """Initialize."""
        self.api = client
        self.platforms = []

        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=SCAN_INTERVAL)

    def set_platforms(self, configured_platforms):
        self.platforms = configured_platforms

    @property
    def bart_station(self):
        return self.api.station

    @property
    def safe_bart_station(self):
        return self.bart_station.lower()

    async def _async_update_data(self):
        """Update data via library."""
        try:
            return await self.api.async_get_data()
        except Exception as exception:
            raise UpdateFailed() from exception

    def get_current_train_data(self, train_name):
        return self.data.get_current_train_data(train_name)

    def get_current_minutes(self, train_name):
        try:
            return self.data.get_current_train_minutes(train_name)
        except AttributeError:
            return MISSING_VALUE

    def get_current_direction(self, train_name):
        try:
            return self.data.get_current_train_direction(train_name)
        except AttributeError:
            return MISSING_VALUE

    # TODO: make this actually better
    def get_sensor_state(self):
        try:
            return self.data.response_time
        except AttributeError:
            return MISSING_VALUE

    def get_is_connected(self):
        try:
            return self.data.is_connected
        except AttributeError:
            return False


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

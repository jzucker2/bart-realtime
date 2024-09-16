"""BartRealtimeDataUpdateCoordinator class"""

from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import BartRealtimeApiClient
from .const import DOMAIN, MISSING_VALUE

SCAN_INTERVAL = timedelta(seconds=30)

_LOGGER: logging.Logger = logging.getLogger(__package__)


class BartRealtimeDataUnavailable(Exception):
    pass


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

    def has_current_train_data(self, train_name):
        return self.data.has_current_train_data(train_name)

    def get_current_train_data(self, train_name):
        return self.data.get_current_train_data(train_name)

    def get_current_minutes(self, train_name):
        try:
            return self.data.get_current_train_minutes(train_name)
        except AttributeError:
            _LOGGER.error(
                "Bart data update coordinator get current minutes missing data for train_name: %s",
                train_name,
            )
            raise BartRealtimeDataUnavailable(f"train_name: {train_name} is missing")

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

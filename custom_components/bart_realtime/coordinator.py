"""BartRealtimeDataUpdateCoordinator class"""

from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import BartRealtimeApiClient
from .const import DOMAIN, LEAVING_VALUE, MISSING_VALUE

SCAN_INTERVAL = timedelta(seconds=30)

_LOGGER: logging.Logger = logging.getLogger(__package__)


class BartRealtimeBaseDataUpdateCoordinatorException(Exception):
    pass


class BartRealtimeDataUnavailable(BartRealtimeBaseDataUpdateCoordinatorException):
    pass


class BartRealtimeBaseDataUpdateCoordinator(DataUpdateCoordinator):
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
    def coordinator_type(self):
        raise BartRealtimeBaseDataUpdateCoordinatorException("not specified!")

    def get_is_connected(self):
        try:
            return self.data.is_connected
        except AttributeError:
            return False

    # TODO: make this actually better
    def get_sensor_state(self):
        try:
            return self.data.response_time
        except AttributeError:
            return MISSING_VALUE

    # TODO: make this actually better
    def get_sensor_last_updated_time(self):
        try:
            return self.data.response_time
        except AttributeError:
            return MISSING_VALUE


class BartRealtimeTrainsDataUpdateCoordinator(BartRealtimeBaseDataUpdateCoordinator):
    """Class to manage fetching train estimates data from the API."""

    async def _async_update_data(self):
        """Update data via library."""
        try:
            return await self.api.async_get_data()
        except Exception as exception:
            raise UpdateFailed() from exception

    @property
    def coordinator_type(self):
        """Necessary to override in subclasses for sensors and entities"""
        return "Trains"

    @property
    def bart_station(self):
        return self.api.station

    @property
    def safe_bart_station(self):
        return self.bart_station.lower()

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

    def get_display_time_string(self, train_name):
        try:
            found_minutes = self.get_current_minutes(train_name)
        except BartRealtimeDataUnavailable:
            return MISSING_VALUE
        else:
            if found_minutes == LEAVING_VALUE:
                return found_minutes
            return f"{found_minutes} minutes"

    def get_current_all_estimates(self, train_name):
        try:
            return self.data.get_current_train_all_estimates(train_name)
        except AttributeError:
            return list(MISSING_VALUE)

    def get_current_direction(self, train_name):
        try:
            return self.data.get_current_train_direction(train_name)
        except AttributeError:
            return MISSING_VALUE

    def get_current_delay(self, train_name):
        try:
            return self.data.get_current_train_delay(train_name)
        except AttributeError:
            return MISSING_VALUE

    def get_current_color(self, train_name):
        try:
            return self.data.get_current_train_color(train_name)
        except AttributeError:
            return MISSING_VALUE

    def get_current_hexcolor(self, train_name):
        try:
            return self.data.get_current_train_hexcolor(train_name)
        except AttributeError:
            return MISSING_VALUE


class BartRealtimeAnnouncementsDataUpdateCoordinator(
    BartRealtimeBaseDataUpdateCoordinator
):
    """Class to manage fetching (advisory) announcements data from the API."""

    async def _async_update_data(self):
        """Update data via library."""
        try:
            return await self.api.async_get_transformed_announcements()
        except Exception as exception:
            raise UpdateFailed() from exception

    @property
    def coordinator_type(self):
        """Necessary to override in subclasses for sensors and entities"""
        return "Announcements"

    def has_current_announcements(self):
        return self.data.has_current_announcements()

    def get_first_announcement(self):
        return self.data.get_first_announcement()

    def get_first_announcement_id(self):
        return self.data.get_first_announcement_id()

    def get_first_announcement_type(self):
        return self.data.get_first_announcement_type()

    def get_first_announcement_station(self):
        return self.data.get_first_announcement_station()

    def get_first_announcement_description(self):
        return self.data.get_first_announcement_description()

    def get_first_announcement_sms_text(self):
        return self.data.get_first_announcement_sms_text()

    def get_first_announcement_posted(self):
        return self.data.get_first_announcement_posted()

    def get_first_announcement_expires(self):
        return self.data.get_first_announcement_expires()

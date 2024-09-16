"""Sensor platform for Bart Realtime."""

from collections.abc import Mapping
import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import EntityCategory

from . import BartRealtimeConfigEntry
from .bart_trains import BartTrainLines
from .const import ICON, MISSING_VALUE
from .coordinator import (
    BartRealtimeAnnouncementsDataUpdateCoordinator,
    BartRealtimeTrainsDataUpdateCoordinator,
)
from .entity import BartRealtimeEntity

_LOGGER: logging.Logger = logging.getLogger(__package__)

ATTR_DIRECTION = "direction"
ATTR_COLOR = "color"
ATTR_DELAY = "delay"
ATTR_HEXCOLOR = "hexcolor"
ATTR_ALL_ESTIMATES = "all_estimates"
ATTR_ANNOUNCEMENT_ID = "announcement_id"
ATTR_ANNOUNCEMENT_TYPE = "announcement_type"
ATTR_ANNOUNCEMENT_DESCRIPTION = "announcement_description"
ATTR_SMS_TEXT = "sms_text"
ATTR_STATION = "station"
ATTR_POSTED = "posted"
ATTR_EXPIRES = "expires"


async def async_setup_entry(hass, entry: BartRealtimeConfigEntry, async_add_devices):
    """Setup sensor platform."""
    trains_coordinator = entry.runtime_data.trains_coordinator
    async_add_devices([BartRealtimeLastUpdatedSensor(trains_coordinator, entry)])
    async_add_devices(
        [
            BartRealtimeTrainSensor(trains_coordinator, entry, s.friendly_name)
            for s in BartTrainLines.get_all_train_lines()
        ]
    )
    announcements_coordinator = entry.runtime_data.announcements_coordinator
    async_add_devices([BartRealtimeLastUpdatedSensor(announcements_coordinator, entry)])
    async_add_devices(
        [BartRealtimeAnnouncementSensor(announcements_coordinator, entry)]
    )


class BartRealtimeLastUpdatedSensor(BartRealtimeEntity):
    """bart_realtime Sensor class."""

    _attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"Bart {self.coordinator_type} Last Updated Time"

    @property
    def unique_id_suffix(self):
        return "last_updated_time"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.get_sensor_last_updated_time()

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def device_class(self):
        """Return the device class of the sensor."""
        return "bart_realtime__custom_device_class"


class BartRealtimeTrainSensor(BartRealtimeEntity, SensorEntity):
    """bart_realtime train class."""

    def __init__(
        self,
        coordinator: BartRealtimeTrainsDataUpdateCoordinator,
        config_entry,
        train_name,
    ):
        super().__init__(coordinator, config_entry)
        self._train_name = train_name

    @property
    def name(self):
        """Return the name of the text."""
        return self.train_name

    @property
    def safe_bart_station(self):
        return self.coordinator.safe_bart_station

    @property
    def unique_id_suffix(self):
        return f"{self.safe_bart_station}_{self.sanitized_train_name}"

    @property
    def train_name(self):
        return self._train_name

    @property
    def sanitized_train_name(self):
        return self.train_name.replace(" /", "_").lower()

    @property
    def direction(self):
        return self.coordinator.get_current_direction(self.train_name)

    @property
    def delay(self):
        return self.coordinator.get_current_delay(self.train_name)

    @property
    def color(self):
        return self.coordinator.get_current_color(self.train_name)

    @property
    def hexcolor(self):
        return self.coordinator.get_current_hexcolor(self.train_name)

    @property
    def all_estimates(self):
        return self.coordinator.get_current_all_estimates(self.train_name)

    @property
    def available(self) -> bool:
        return self.coordinator.has_current_train_data(self.train_name)

    @property
    def friendly_display_value(self):
        """Return value of the text if data exists."""
        try:
            return self.coordinator.get_display_time_string(self.train_name)
        except Exception as unexp:
            _LOGGER.error(
                "Setting sensor state missing for self.train_name: %s with unexp: %s",
                self.train_name,
                unexp,
            )
            return MISSING_VALUE

    @property
    def state(self):
        """Return value of the text if data exists."""
        return self.friendly_display_value

    def _get_extra_state_attributes(self) -> Mapping[str, Any] | None:
        final_dict = {
            ATTR_DIRECTION: self.direction,
            ATTR_DELAY: self.delay,
            ATTR_COLOR: self.color,
            ATTR_HEXCOLOR: self.hexcolor,
            ATTR_ALL_ESTIMATES: self.all_estimates,
        }
        return dict(final_dict)

    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None:
        """Return the state attributes of the sensor."""
        return self._get_extra_state_attributes()


class BartRealtimeAnnouncementSensor(BartRealtimeEntity, SensorEntity):
    """bart_realtime announcement class."""

    def __init__(
        self, coordinator: BartRealtimeAnnouncementsDataUpdateCoordinator, config_entry
    ):
        super().__init__(coordinator, config_entry)

    @property
    def announcement_base_name(self):
        return "Announcement"

    @property
    def name(self):
        """Return the name of the text."""
        return self.announcement_base_name

    @property
    def unique_id_suffix(self):
        return f"{self.announcement_base_name}"

    @property
    def announcement_id(self):
        return self.coordinator.get_first_announcement_id()

    @property
    def announcement_type(self):
        return self.coordinator.get_first_announcement_type()

    @property
    def station(self):
        return self.coordinator.get_first_announcement_station()

    @property
    def announcement_description(self):
        return self.coordinator.get_first_announcement_description()

    @property
    def sms_text(self):
        return self.coordinator.get_first_announcement_sms_text()

    @property
    def posted(self):
        return self.coordinator.get_first_announcement_posted()

    @property
    def expires(self):
        return self.coordinator.get_first_announcement_expires()

    @property
    def available(self) -> bool:
        return self.coordinator.has_current_announcements()

    @property
    def friendly_display_value(self):
        """Return value of the text if data exists."""
        try:
            return self.sms_text
        except Exception as unexp:
            _LOGGER.error(
                "Setting sensor state missing for self: %s with unexp: %s",
                self.train_name,
                unexp,
            )
            return MISSING_VALUE

    @property
    def state(self):
        """Return value of the text if data exists."""
        return self.friendly_display_value

    def _get_extra_state_attributes(self) -> Mapping[str, Any] | None:
        final_dict = {
            ATTR_STATION: self.station,
            ATTR_ANNOUNCEMENT_ID: self.announcement_id,
            ATTR_ANNOUNCEMENT_TYPE: self.announcement_type,
            ATTR_ANNOUNCEMENT_DESCRIPTION: self.announcement_description,
            ATTR_SMS_TEXT: self.sms_text,
            ATTR_POSTED: self.posted,
            ATTR_EXPIRES: self.expires,
        }
        return dict(final_dict)

    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None:
        """Return the state attributes of the sensor."""
        return self._get_extra_state_attributes()

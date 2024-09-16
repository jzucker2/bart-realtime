"""Sensor platform for Bart Realtime."""

from collections.abc import Mapping
import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity

from . import BartRealtimeConfigEntry
from .bart_trains import BartTrainLines
from .const import DEFAULT_NAME, ICON, MISSING_VALUE, TRAIN_SENSOR
from .entity import BartRealtimeEntity

_LOGGER: logging.Logger = logging.getLogger(__package__)

ATTR_DIRECTION = "direction"
ATTR_COLOR = "color"
ATTR_DELAY = "delay"
ATTR_HEXCOLOR = "hexcolor"
ATTR_ALL_ESTIMATES = "all_estimates"


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


class BartRealtimeLastUpdatedSensor(BartRealtimeEntity):
    """bart_realtime Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"Bart {self.coordinator.coordinator_type} Last Updated Time"

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

    def __init__(self, coordinator, config_entry, train_name):
        super().__init__(coordinator, config_entry)
        self._train_name = train_name
        self._attr_unique_id = f"{self.get_unique_entity_base_name()}-{coordinator.safe_bart_station}-{train_name}"

    @classmethod
    def get_base_entity_name(self, separator="_"):
        """Return the base entity of the text."""
        return f"{DEFAULT_NAME}{separator}{TRAIN_SENSOR}"

    @classmethod
    def get_unique_entity_base_name(cls):
        return cls.get_base_entity_name(separator="_")

    @property
    def name(self):
        """Return the name of the text."""
        return self.train_name

    @property
    def unique_id(self) -> str:
        """Return a unique ID."""
        return f"{self.get_unique_entity_base_name()}_{self.safe_bart_station}_{self.sanitized_train_name}"

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
                "Setting text sensor state missing for self.train_name: %s with unexp: %s",
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

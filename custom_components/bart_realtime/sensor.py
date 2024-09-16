"""Sensor platform for Bart Realtime."""

import logging

from homeassistant.components.sensor import SensorEntity

from . import BartRealtimeConfigEntry
from .bart_trains import BartTrainLines
from .const import DEFAULT_NAME, ICON, MISSING_VALUE, SENSOR, TRAIN_SENSOR
from .coordinator import BartRealtimeDataUnavailable
from .entity import BartRealtimeEntity

_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup_entry(hass, entry: BartRealtimeConfigEntry, async_add_devices):
    """Setup sensor platform."""
    trains_coordinator = entry.runtime_data.trains_coordinator
    async_add_devices([BartRealtimeSensor(trains_coordinator, entry)])
    async_add_devices(
        [
            BartRealtimeTrainSensor(trains_coordinator, entry, s.friendly_name)
            for s in BartTrainLines.get_all_train_lines()
        ]
    )


class BartRealtimeSensor(BartRealtimeEntity):
    """bart_realtime Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.get_sensor_state()

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
    def available(self) -> bool:
        return self.coordinator.has_current_train_data(self.train_name)

    @property
    def state(self):
        """Return value of the text if data exists."""
        try:
            return self.coordinator.get_current_minutes(self.train_name)
        except BartRealtimeDataUnavailable:
            return MISSING_VALUE
        except Exception as unexp:
            _LOGGER.error(
                "Setting text sensor state missing for self.train_name: %s with unexp: %s",
                self.train_name,
                unexp,
            )
            return MISSING_VALUE

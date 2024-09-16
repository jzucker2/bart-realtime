"""Binary sensor platform for Bart Realtime."""

from homeassistant.components.binary_sensor import BinarySensorEntity

from . import BartRealtimeConfigEntry
from .const import BINARY_SENSOR, BINARY_SENSOR_DEVICE_CLASS, DEFAULT_NAME
from .entity import BartRealtimeEntity


async def async_setup_entry(hass, entry: BartRealtimeConfigEntry, async_add_devices):
    """Setup binary_sensor platform."""
    trains_coordinator = entry.runtime_data.trains_coordinator
    async_add_devices([BartRealtimeBinarySensor(trains_coordinator, entry)])


class BartRealtimeBinarySensor(BartRealtimeEntity, BinarySensorEntity):
    """bart_realtime binary_sensor class."""

    @property
    def name(self):
        """Return the name of the binary_sensor."""
        return f"{DEFAULT_NAME}_{BINARY_SENSOR}"

    @property
    def device_class(self):
        """Return the class of this binary_sensor."""
        return BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        return self.coordinator.get_is_connected()

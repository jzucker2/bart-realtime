"""Binary sensor platform for Bart Realtime."""

from homeassistant.components.binary_sensor import BinarySensorEntity

from . import BartRealtimeConfigEntry
from .const import BINARY_SENSOR_DEVICE_CLASS
from .entity import BartRealtimeEntity


async def async_setup_entry(hass, entry: BartRealtimeConfigEntry, async_add_devices):
    """Setup binary_sensor platform."""
    trains_coordinator = entry.runtime_data.trains_coordinator
    async_add_devices([BartRealtimeAPIConnectedBinarySensor(trains_coordinator, entry)])


class BartRealtimeAPIConnectedBinarySensor(BartRealtimeEntity, BinarySensorEntity):
    """bart_realtime binary_sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"Bart {self.coordinator_type} API Connected"

    @property
    def unique_id_suffix(self):
        return "api_connected"

    @property
    def device_class(self):
        """Return the class of this binary_sensor."""
        return BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        return self.coordinator.get_is_connected()

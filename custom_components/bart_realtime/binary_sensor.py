"""Binary sensor platform for Bart Realtime."""
from homeassistant.components.binary_sensor import BinarySensorEntity

from .const import BINARY_SENSOR
from .const import BINARY_SENSOR_DEVICE_CLASS
from .const import DEFAULT_NAME
from .const import DOMAIN
from .entity import BartRealtimeEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup binary_sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([BartRealtimeBinarySensor(coordinator, entry)])


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
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return self.config_entry.entry_id

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        return self.coordinator.data.get("title", "") == "foo"

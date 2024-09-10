"""Sensor platform for Bart Realtime."""

from . import BartRealtimeConfigEntry
from .const import DEFAULT_NAME, DOMAIN, ICON, SENSOR
from .entity import BartRealtimeEntity


async def async_setup_entry(hass, entry: BartRealtimeConfigEntry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([BartRealtimeSensor(coordinator, entry)])


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

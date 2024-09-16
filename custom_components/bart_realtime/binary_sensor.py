"""Binary sensor platform for Bart Realtime."""

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.const import EntityCategory

from . import BartRealtimeConfigEntry
from .const import BINARY_SENSOR_DEVICE_CLASS
from .coordinator import BartRealtimeAnnouncementsDataUpdateCoordinator
from .entity import BartRealtimeEntity


async def async_setup_entry(hass, entry: BartRealtimeConfigEntry, async_add_devices):
    """Setup binary_sensor platform."""
    trains_coordinator = entry.runtime_data.trains_coordinator
    async_add_devices([BartRealtimeAPIConnectedBinarySensor(trains_coordinator, entry)])
    announcements_coordinator = entry.runtime_data.announcements_coordinator
    async_add_devices(
        [
            BartRealtimeAPIConnectedBinarySensor(announcements_coordinator, entry),
            BartRealtimeHasAnnouncementsBinarySensor(announcements_coordinator, entry),
        ]
    )


class BartRealtimeAPIConnectedBinarySensor(BartRealtimeEntity, BinarySensorEntity):
    """bart_realtime binary_sensor class."""

    _attr_entity_category = EntityCategory.DIAGNOSTIC

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


class BartRealtimeHasAnnouncementsBinarySensor(BartRealtimeEntity, BinarySensorEntity):
    """bart_realtime has announcements binary_sensor class."""

    def __init__(
        self, coordinator: BartRealtimeAnnouncementsDataUpdateCoordinator, config_entry
    ):
        super().__init__(coordinator, config_entry)

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Bart Has Announcements"

    @property
    def unique_id_suffix(self):
        return "has_announcements"

    @property
    def device_class(self):
        """Return the class of this binary_sensor."""
        return BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self):
        """Return true if the binary_sensor has announcements available."""
        return self.coordinator.has_current_announcements()

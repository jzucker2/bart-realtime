"""Binary sensor platform for Bart Realtime."""

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.const import EntityCategory

from . import BartRealtimeConfigEntry
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
    _attr_device_class = BinarySensorDeviceClass.CONNECTIVITY

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"Bart {self.coordinator_type} API Connected"

    @property
    def unique_id_suffix(self):
        return "api_connected"

    @property
    def icon(self) -> str | None:
        """Icon of the entity."""
        return "mdi:timer-refresh"

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        return self.coordinator.get_is_connected()


class BartRealtimeHasAnnouncementsBinarySensor(BartRealtimeEntity, BinarySensorEntity):
    """bart_realtime has announcements binary_sensor class."""

    _attr_device_class = BinarySensorDeviceClass.PROBLEM

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
    def is_on(self):
        """Return true if the binary_sensor has announcements available."""
        return self.coordinator.has_current_announcements()

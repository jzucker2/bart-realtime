"""BartRealtimeEntity class"""

from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, NAME, VERSION
from .coordinator import BartRealtimeBaseDataUpdateCoordinator


class BartRealtimeEntity(CoordinatorEntity):
    def __init__(
        self, coordinator: BartRealtimeBaseDataUpdateCoordinator, config_entry
    ):
        super().__init__(coordinator)
        self.config_entry = config_entry

    @property
    def config_entry_id(self):
        return self.config_entry.entry_id

    @property
    def coordinator_type(self) -> str:
        return self.coordinator.coordinator_type

    @property
    def unique_id_base(self):
        return f"{self.config_entry_id}-{self.coordinator_type}"

    @property
    def unique_id_suffix(self):
        """Override in subclasses to ensure uniqueness"""
        return "bart_entity"

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return f"{self.unique_id_base}-{self.unique_id_suffix}"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.config_entry_id)},
            "name": NAME,
            "model": VERSION,
            "manufacturer": NAME,
        }

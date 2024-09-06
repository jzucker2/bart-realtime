"""Text sensor platform for Bart Realtime."""
from homeassistant.components.text import TextEntity

from .bart_trains import BartTrainLines
from .const import DEFAULT_NAME
from .const import DOMAIN
from .const import TEXT
from .entity import BartRealtimeEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup text platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        [
            BartRealtimeTextSensor(
                coordinator,
                entry,
                s.friendly_name
            )
            for s in BartTrainLines.get_all_train_lines()
        ]
    )


class BartRealtimeTextSensor(BartRealtimeEntity, TextEntity):
    """bart_realtime text class."""

    def __init__(self, coordinator, config_entry, train_name):
        super().__init__(coordinator, config_entry)
        self._train_name = train_name
        self._attr_unique_id = f"{self.get_unique_entity_base_name()}-{train_name}"

    @classmethod
    def get_base_entity_name(self, separator='_'):
        """Return the base entity of the text."""
        return f"{DEFAULT_NAME}{separator}{TEXT}"

    @classmethod
    def get_unique_entity_base_name(cls):
        return cls.get_base_entity_name(separator='_')

    @property
    def name(self):
        """Return the name of the text."""
        return f"{self.get_base_entity_name()}_{self.train_name}"

    @property
    def unique_id(self) -> str:
        """Return a unique ID."""
        return f"{self.get_unique_entity_base_name()}_{self.sanitized_train_name}"

    @property
    def train_name(self):
        return self._train_name

    @property
    def sanitized_train_name(self):
        return self.train_name.replace(' /', '_').lower()

    @property
    def state(self):
        """Return value of the text if data exists."""
        return self.coordinator.get_current_minutes(self.train_name)

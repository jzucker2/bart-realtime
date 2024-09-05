"""Binary sensor platform for Bart Realtime."""
from homeassistant.components.text import TextEntity

from .bart_trains import BartTrainLines
from .const import DEFAULT_NAME
from .const import DOMAIN
from .const import TEXT
from .entity import BartRealtimeEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup binary_sensor platform."""
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
    """bart_realtime binary_sensor class."""

    def __init__(self, coordinator, config_entry, train_name):
        super().__init__(coordinator, config_entry)
        self._train_name = train_name

    @property
    def name(self):
        """Return the name of the binary_sensor."""
        return f"{DEFAULT_NAME}_{TEXT}_{self.train_name}"

    @property
    def train_name(self):
        return self._train_name

    @property
    def state(self):
        """Return value of the text if data exists."""
        return self.coordinator.data.get(self.train_name, "missing")

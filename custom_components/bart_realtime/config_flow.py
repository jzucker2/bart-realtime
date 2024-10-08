"""Adds config flow for Bart Realtime."""

import logging

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.aiohttp_client import async_create_clientsession
from homeassistant.helpers.selector import (
    SelectSelector,
    SelectSelectorConfig,
    SelectSelectorMode,
)
import voluptuous as vol

from .api import BartRealtimeApiClient
from .const import (
    CONF_API_KEY,
    CONF_STATION,
    DEFAULT_API_KEY,
    DOMAIN,
    HARDCODED_STATIONS_LIST,
    PLATFORMS,
)

_LOGGER: logging.Logger = logging.getLogger(__package__)


def get_station_options_list():
    return HARDCODED_STATIONS_LIST


# This is the schema that used to display the UI to the user. This simple
# schema has a single required host field, but it could include a number of fields
# such as username, password etc. See other components in the HA core code for
# further examples.
# Note the input displayed to the user will be translated. See the
# translations/<lang>.json file and strings.json. See here for further information:
# https://developers.home-assistant.io/docs/config_entries_config_flow_handler/#translations
# At the time of writing I found the translations created by the scaffold didn't
# quite work as documented and always gave me the "Lokalise key references" string
# (in square brackets), rather than the actual translated value. I did not attempt to
# figure this out or look further into it.
DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_STATION): SelectSelector(
            SelectSelectorConfig(
                options=get_station_options_list(),
                mode=SelectSelectorMode.DROPDOWN,
                multiple=False,
                sort=False,
            )
        ),
        vol.Optional(CONF_API_KEY, default=DEFAULT_API_KEY): cv.string,
    }
)


class BartRealtimeFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for bart_realtime."""

    VERSION = 1

    def __init__(self):
        """Initialize."""
        self._errors = {}

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        self._errors = {}

        # Uncomment the next 2 lines if only a single instance of the integration is allowed:
        # if self._async_current_entries():
        #     return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            valid = await self._test_credentials(user_input)
            if valid:
                return self.async_create_entry(
                    title=user_input[CONF_STATION], data=user_input
                )
            else:
                self._errors["base"] = "auth"

            return await self._show_config_form(user_input)

        return await self._show_config_form(user_input)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return BartRealtimeOptionsFlowHandler(config_entry)

    async def _show_config_form(self, user_input):  # pylint: disable=unused-argument
        """Show the configuration form to edit location data."""
        return self.async_show_form(
            step_id="user",
            data_schema=DATA_SCHEMA,
            errors=self._errors,
        )

    async def _test_credentials(self, user_input):
        """Return true if credentials is valid."""
        try:
            _LOGGER.debug("Test credentials user_input: %s", user_input)
            session = async_create_clientsession(self.hass)
            api_key = user_input[CONF_API_KEY]
            station = user_input[CONF_STATION]
            client = BartRealtimeApiClient(station, session, api_key=api_key)
            await client.async_validate()
            return True
        except Exception:  # pylint: disable=broad-except
            pass
        return False


class BartRealtimeOptionsFlowHandler(config_entries.OptionsFlow):
    """Config flow options handler for bart_realtime."""

    def __init__(self, config_entry):
        """Initialize HACS options flow."""
        self.config_entry = config_entry
        self.options = dict(config_entry.options)

    async def async_step_init(self, user_input=None):  # pylint: disable=unused-argument
        """Manage the options."""
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        if user_input is not None:
            self.options.update(user_input)
            return await self._update_options()

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(x, default=self.options.get(x, True)): bool
                    for x in sorted(PLATFORMS)
                }
            ),
        )

    async def _update_options(self):
        """Update config entry options."""
        return self.async_create_entry(
            title=self.config_entry.data.get(CONF_STATION), data=self.options
        )

"""Constants for Bart Realtime."""

# Base component constants
NAME = "Bart Realtime"
DOMAIN = "bart_realtime"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.10.0"

ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/jzucker2/bart-realtime/issues"

# Icons
ICON = "mdi:format-quote-close"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
TEXT = "text"
PLATFORMS = [BINARY_SENSOR, SENSOR, TEXT]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_API_KEY = "api_key"
CONF_STATION = "station"

# Defaults
DEFAULT_NAME = DOMAIN

MISSING_VALUE = "missing"


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""

DEFAULT_BART_STATION = "16TH"
DEFAULT_API_KEY = "MW9S-E7SL-26DU-VV8V"

# https://api.bart.gov/docs/etd/etd.aspx
# https://api.bart.gov/api/etd.aspx?cmd=etd&orig=16TH&key=MW9S-E7SL-26DU-VV8V

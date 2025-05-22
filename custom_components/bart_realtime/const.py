"""Constants for Bart Realtime."""

# Base component constants
NAME = "Bart Realtime"
DOMAIN = "bart_realtime"
VERSION = "1.3.1"

ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/jzucker2/bart-realtime/issues"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
TRAIN_SENSOR = "train_sensor"
PLATFORMS = [BINARY_SENSOR, SENSOR]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_API_KEY = "api_key"
CONF_STATION = "station"

# Defaults
DEFAULT_NAME = DOMAIN

MISSING_VALUE = "missing"
LEAVING_VALUE = "Leaving"
NO_DELAYS_VALUE = "No delays reported."

# TODO: replace with a dynamic call
HARDCODED_STATIONS_LIST = list(
    [
        "12TH",
        "16TH",
        "19TH",
        "24TH",
        "ANTC",
        "ASHB",
        "BALB",
        "BAYF",
        "BERY",
        "CAST",
        "CIVC",
        "COLS",
        "COLM",
        "CONC",
        "DALY",
        "DBRK",
        "DUBL",
        "DELN",
        "PLZA",
        "EMBR",
        "FRMT",
        "FTVL",
        "GLEN",
        "HAYW",
        "LAFY",
        "LAKE",
        "MCAR",
        "MLBR",
        "MLPT",
        "MONT",
        "NBRK",
        "NCON",
        "OAKL",
        "ORIN",
        "PITT",
        "PCTR",
        "PHIL",
        "POWL",
        "RICH",
        "ROCK",
        "SBRN",
        "SFIA",
        "SANL",
        "SHAY",
        "SSAN",
        "UCTY",
        "WCRK",
        "WARM",
        "WDUB",
        "WOAK",
    ]
)


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

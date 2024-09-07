# Bart Realtime

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![pre-commit][pre-commit-shield]][pre-commit]
[![Black][black-shield]][black]

[![hacs][hacsbadge]][hacs]
[![Project Maintenance][maintenance-shield]][user_profile]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

**TO BE REMOVED: If you need help, as a developer, to use this custom component tempalte,
please look at the [User Guide in the Cookiecutter documentation](https://cookiecutter-homeassistant-custom-component.readthedocs.io/en/stable/quickstart.html)**

**This component will set up the following platforms.**

| Platform        | Description                       |
| --------------- | --------------------------------- |
| `binary_sensor` | Show something `True` or `False`. |
| `sensor`        | Show info from Bart Realtime API. |

![example][exampleimg]

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `bart_realtime`.
4. Download _all_ the files from the `custom_components/bart_realtime/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Bart Realtime"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/bart_realtime/translations/en.json
custom_components/bart_realtime/translations/fr.json
custom_components/bart_realtime/translations/nb.json
custom_components/bart_realtime/translations/sensor.en.json
custom_components/bart_realtime/translations/sensor.fr.json
custom_components/bart_realtime/translations/sensor.nb.json
custom_components/bart_realtime/translations/sensor.nb.json
custom_components/bart_realtime/__init__.py
custom_components/bart_realtime/api.py
custom_components/bart_realtime/binary_sensor.py
custom_components/bart_realtime/config_flow.py
custom_components/bart_realtime/const.py
custom_components/bart_realtime/manifest.json
custom_components/bart_realtime/sensor.py
custom_components/bart_realtime/switch.py
```

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

## Credits

This project was generated from [@oncleben31](https://github.com/oncleben31)'s [Home Assistant Custom Component Cookiecutter](https://github.com/oncleben31/cookiecutter-homeassistant-custom-component) template.

Code template was mainly taken from [@Ludeeus](https://github.com/ludeeus)'s [integration_blueprint][integration_blueprint] template

---

[integration_blueprint]: https://github.com/custom-components/integration_blueprint
[black]: https://github.com/psf/black
[black-shield]: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
[buymecoffee]: https://www.buymeacoffee.com/jzucker2
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/jzucker2/bart-realtime.svg?style=for-the-badge
[commits]: https://github.com/jzucker2/bart-realtime/commits/main
[hacs]: https://hacs.xyz
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/jzucker2/bart-realtime.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40jzucker2-blue.svg?style=for-the-badge
[pre-commit]: https://github.com/pre-commit/pre-commit
[pre-commit-shield]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/jzucker2/bart-realtime.svg?style=for-the-badge
[releases]: https://github.com/jzucker2/bart-realtime/releases
[user_profile]: https://github.com/jzucker2

## Local

To run the dev script locally:

```
pip install -r dev-requirements.txt

python local_data_fetcher.py
```

## Notes

- https://developers.home-assistant.io/blog/2020/05/08/logos-custom-integrations/
- https://github.com/home-assistant/brands
- https://github.com/home-assistant/brands/pull/2610
  - Example PR of adding images
- https://developers.home-assistant.io/docs/config_entries_index/
- https://github.com/boralyl/github-custom-component-tutorial
- https://github.com/project-koku/nise-populator/pull/135#issuecomment-2329879613
  - black and reorder-python-imports are now incompatible

## Bart Dev Info

- https://api.bart.gov/docs/bsa/bsa.aspx
  - Advisory endpoint (maybe a text sensor for this as well, with its own data update coordinator)
- https://api.bart.gov/docs/stn/stns.aspx
  - All stations (could use this for testing config flow better)

### Examples

```
{'?xml': {'@encoding': 'utf-8', '@version': '1.0'},
 'root': {'@id': '1',
          'date': '09/07/2024',
          'message': '',
          'station': [{'abbr': '16TH',
                       'etd': [{'abbreviation': 'ANTC',
                                'destination': 'Antioch',
                                'estimate': [{'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'YELLOW',
                                              'delay': '79',
                                              'direction': 'North',
                                              'dynamicflag': '0',
                                              'hexcolor': '#ffff33',
                                              'length': '8',
                                              'minutes': '7',
                                              'platform': '2'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'YELLOW',
                                              'delay': '0',
                                              'direction': 'North',
                                              'dynamicflag': '0',
                                              'hexcolor': '#ffff33',
                                              'length': '8',
                                              'minutes': '26',
                                              'platform': '2'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'YELLOW',
                                              'delay': '0',
                                              'direction': 'North',
                                              'dynamicflag': '0',
                                              'hexcolor': '#ffff33',
                                              'length': '8',
                                              'minutes': '46',
                                              'platform': '2'}],
                                'limited': '0'},
                               {'abbreviation': 'BERY',
                                'destination': 'Berryessa',
                                'estimate': [{'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'GREEN',
                                              'delay': '0',
                                              'direction': 'North',
                                              'dynamicflag': '0',
                                              'hexcolor': '#339933',
                                              'length': '6',
                                              'minutes': '18',
                                              'platform': '2'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'GREEN',
                                              'delay': '0',
                                              'direction': 'North',
                                              'dynamicflag': '0',
                                              'hexcolor': '#339933',
                                              'length': '6',
                                              'minutes': '38',
                                              'platform': '2'}],
                                'limited': '0'},
                               {'abbreviation': 'DALY',
                                'destination': 'Daly City',
                                'estimate': [{'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'GREEN',
                                              'delay': '408',
                                              'direction': 'South',
                                              'dynamicflag': '0',
                                              'hexcolor': '#339933',
                                              'length': '6',
                                              'minutes': '17',
                                              'platform': '1'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'BLUE',
                                              'delay': '106',
                                              'direction': 'South',
                                              'dynamicflag': '0',
                                              'hexcolor': '#0099cc',
                                              'length': '6',
                                              'minutes': '19',
                                              'platform': '1'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'GREEN',
                                              'delay': '86',
                                              'direction': 'South',
                                              'dynamicflag': '0',
                                              'hexcolor': '#339933',
                                              'length': '6',
                                              'minutes': '31',
                                              'platform': '1'}],
                                'limited': '0'},
                               {'abbreviation': 'DUBL',
                                'destination': 'Dublin/Pleasanton',
                                'estimate': [{'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'BLUE',
                                              'delay': '0',
                                              'direction': 'North',
                                              'dynamicflag': '0',
                                              'hexcolor': '#0099cc',
                                              'length': '6',
                                              'minutes': '10',
                                              'platform': '2'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'BLUE',
                                              'delay': '0',
                                              'direction': 'North',
                                              'dynamicflag': '0',
                                              'hexcolor': '#0099cc',
                                              'length': '6',
                                              'minutes': '30',
                                              'platform': '2'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'BLUE',
                                              'delay': '0',
                                              'direction': 'North',
                                              'dynamicflag': '0',
                                              'hexcolor': '#0099cc',
                                              'length': '6',
                                              'minutes': '50',
                                              'platform': '2'}],
                                'limited': '0'},
                               {'abbreviation': 'MLBR',
                                'destination': 'Millbrae',
                                'estimate': [{'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'RED',
                                              'delay': '63',
                                              'direction': 'South',
                                              'dynamicflag': '0',
                                              'hexcolor': '#ff0000',
                                              'length': '6',
                                              'minutes': '9',
                                              'platform': '1'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'RED',
                                              'delay': '0',
                                              'direction': 'South',
                                              'dynamicflag': '0',
                                              'hexcolor': '#ff0000',
                                              'length': '6',
                                              'minutes': '28',
                                              'platform': '1'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'RED',
                                              'delay': '0',
                                              'direction': 'South',
                                              'dynamicflag': '0',
                                              'hexcolor': '#ff0000',
                                              'length': '6',
                                              'minutes': '48',
                                              'platform': '1'}],
                                'limited': '0'},
                               {'abbreviation': 'RICH',
                                'destination': 'Richmond',
                                'estimate': [{'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'RED',
                                              'delay': '0',
                                              'direction': 'North',
                                              'dynamicflag': '0',
                                              'hexcolor': '#ff0000',
                                              'length': '6',
                                              'minutes': '13',
                                              'platform': '2'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'RED',
                                              'delay': '0',
                                              'direction': 'North',
                                              'dynamicflag': '0',
                                              'hexcolor': '#ff0000',
                                              'length': '6',
                                              'minutes': '33',
                                              'platform': '2'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'RED',
                                              'delay': '0',
                                              'direction': 'North',
                                              'dynamicflag': '0',
                                              'hexcolor': '#ff0000',
                                              'length': '6',
                                              'minutes': '53',
                                              'platform': '2'}],
                                'limited': '0'},
                               {'abbreviation': 'SFIA',
                                'destination': 'SF Airport',
                                'estimate': [{'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'YELLOW',
                                              'delay': '0',
                                              'direction': 'South',
                                              'dynamicflag': '0',
                                              'hexcolor': '#ffff33',
                                              'length': '8',
                                              'minutes': 'Leaving',
                                              'platform': '1'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'YELLOW',
                                              'delay': '71',
                                              'direction': 'South',
                                              'dynamicflag': '0',
                                              'hexcolor': '#ffff33',
                                              'length': '8',
                                              'minutes': '22',
                                              'platform': '1'},
                                             {'bikeflag': '1',
                                              'cancelflag': '0',
                                              'color': 'YELLOW',
                                              'delay': '0',
                                              'direction': 'South',
                                              'dynamicflag': '0',
                                              'hexcolor': '#ffff33',
                                              'length': '8',
                                              'minutes': '41',
                                              'platform': '1'}],
                                'limited': '0'}],
                       'name': '16th St. Mission'}],
          'time': '12:46:32 PM PDT',
          'uri': {'#cdata-section': 'http://api.bart.gov/api/etd.aspx?cmd=etd&orig=16TH&json=y'}}}
```

```
{
  "?xml": {
    "@version": "1.0",
    "@encoding": "utf-8"
  },
  "root": {
    "@id": "1",
    "uri": {
      "#cdata-section": "http://api.bart.gov/api/etd.aspx?cmd=etd&orig=ALL&json=y"
    },
    "date": "09/07/2024",
    "time": "04:13:18 PM PDT",
    "station": [
      {
        "name": "Lake Merritt",
        "abbr": "LAKE",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "2",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "156",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "12",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "20",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "103",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "11",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "25",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "61",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "6",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "164",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "24",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "44",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "14",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "34",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "54",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Fruitvale",
        "abbr": "FTVL",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "6",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "121",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "16",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "24",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "1",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "122",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "7",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "21",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "74",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "10",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "129",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "28",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "48",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "10",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "30",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "50",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Coliseum",
        "abbr": "COLS",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "1",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "153",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "9",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "112",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "19",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "4",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "17",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "84",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "24",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "13",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "120",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "31",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "7",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "27",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "47",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "San Leandro",
        "abbr": "SANL",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "141",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "13",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "96",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "23",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "14",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "98",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "19",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "33",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "17",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "104",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "35",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "55",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Fremont",
            "abbreviation": "FRMT",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "WHITE",
                "hexcolor": "#ffffff",
                "bikeflag": "1",
                "delay": "517",
                "cancelflag": "0",
                "dynamicflag": "1"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "3",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "22",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "42",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Bay Fair",
        "abbr": "BAYF",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "9",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "127",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "17",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "82",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "27",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "10",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "113",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "16",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "29",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "101",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "20",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "90",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "39",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Fremont",
            "abbreviation": "FRMT",
            "limited": "0",
            "estimate": [
              {
                "minutes": "4",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "WHITE",
                "hexcolor": "#ffffff",
                "bikeflag": "1",
                "delay": "503",
                "cancelflag": "0",
                "dynamicflag": "1"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "19",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "39",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "59",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Hayward",
        "abbr": "HAYW",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "13",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "108",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "20",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "64",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "6",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "117",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "26",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "44",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Fremont",
            "abbreviation": "FRMT",
            "limited": "0",
            "estimate": [
              {
                "minutes": "8",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "WHITE",
                "hexcolor": "#ffffff",
                "bikeflag": "1",
                "delay": "495",
                "cancelflag": "0",
                "dynamicflag": "1"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "15",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "35",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "55",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "South Hayward",
        "abbr": "SHAY",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "4",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "17",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "94",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "24",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "3",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "141",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "22",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "40",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Fremont",
            "abbreviation": "FRMT",
            "limited": "0",
            "estimate": [
              {
                "minutes": "12",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "WHITE",
                "hexcolor": "#ffffff",
                "bikeflag": "1",
                "delay": "481",
                "cancelflag": "0",
                "dynamicflag": "1"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "11",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "31",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Union City",
        "abbr": "UCTY",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "1",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "80",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "9",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "21",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "83",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "17",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "35",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "55",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Fremont",
            "abbreviation": "FRMT",
            "limited": "0",
            "estimate": [
              {
                "minutes": "16",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "WHITE",
                "hexcolor": "#ffffff",
                "bikeflag": "1",
                "delay": "470",
                "cancelflag": "0",
                "dynamicflag": "1"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "7",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "26",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "46",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Fremont",
        "abbr": "FRMT",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "13",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "25",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "13",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "31",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "3",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "95",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "22",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "42",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Rockridge",
        "abbr": "ROCK",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "25",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "45",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "10",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "260",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "26",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "46",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Orinda",
        "abbr": "ORIN",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "11",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "31",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "274",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "21",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "40",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Lafayette",
        "abbr": "LAFY",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "15",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "35",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "55",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "306",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "16",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "36",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Walnut Creek",
        "abbr": "WCRK",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "2",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "161",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "20",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "40",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "12",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "70",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "31",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Pleasant Hill/Contra Costa Centre",
        "abbr": "PHIL",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "151",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "23",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "43",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "9",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "65",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "28",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "48",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Concord",
        "abbr": "CONC",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "10",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "106",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "28",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "48",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "4",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "66",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "23",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "43",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "North Concord/Martinez",
        "abbr": "NCON",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "13",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "82",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "31",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "1",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "98",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "20",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "40",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Pittsburg/Bay Point",
        "abbr": "PITT",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "2",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "235",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "19",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "65",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "38",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "13",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "33",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Pittsburg Center",
        "abbr": "PCTR",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "7",
                "platform": "1",
                "direction": "North",
                "length": "1",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "27",
                "platform": "1",
                "direction": "North",
                "length": "1",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "47",
                "platform": "1",
                "direction": "North",
                "length": "1",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SFO/Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "6",
                "platform": "2",
                "direction": "South",
                "length": "1",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "26",
                "platform": "2",
                "direction": "South",
                "length": "1",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "46",
                "platform": "2",
                "direction": "South",
                "length": "1",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Antioch",
        "abbr": "ANTC",
        "etd": [
          {
            "destination": "SFO/Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "2",
                "direction": "South",
                "length": "1",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "18",
                "platform": "2",
                "direction": "South",
                "length": "1",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "38",
                "platform": "2",
                "direction": "South",
                "length": "1",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "12th St. Oakland City Center",
        "abbr": "12TH",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "17",
                "platform": "3",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "37",
                "platform": "3",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "57",
                "platform": "3",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "17",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "37",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "57",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "2",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "22",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "42",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "7",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "112",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "17",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "25",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "18",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "201",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "35",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "55",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "19th St. Oakland",
        "abbr": "19TH",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "3",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "19",
                "platform": "3",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "39",
                "platform": "3",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "15",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "35",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "55",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "1",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "71",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "20",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "40",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "112",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "8",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "109",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "19",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "17",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "242",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "33",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "53",
                "platform": "2",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "MacArthur",
        "abbr": "MCAR",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "3",
                "platform": "3",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "23",
                "platform": "3",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "43",
                "platform": "3",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "11",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "31",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "17",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "37",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "57",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "4",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "88",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "11",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "63",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "23",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "14",
                "platform": "4",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "256",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "29",
                "platform": "4",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "49",
                "platform": "4",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Castro Valley",
        "abbr": "CAST",
        "etd": [
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "11",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "31",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "68",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "25",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "66",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "43",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "West Dublin/Pleasanton",
        "abbr": "WDUB",
        "etd": [
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "1",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "21",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "41",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "14",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "69",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "34",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "67",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "53",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Dublin/Pleasanton",
        "abbr": "DUBL",
        "etd": [
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "18",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "38",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "West Oakland",
        "abbr": "WOAK",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "14",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "33",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "53",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "7",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "69",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "26",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "46",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "10",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "95",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "17",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "30",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "19",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "38",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "58",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "7",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "27",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "47",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "3",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "130",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "21",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "41",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "2",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "137",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "22",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "177",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "40",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Embarcadero",
        "abbr": "EMBR",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "7",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "71",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "26",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "46",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "122",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "19",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "39",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "4",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "67",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "17",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "70",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "24",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "12",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "70",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "31",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "14",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "34",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "54",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "14",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "34",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "54",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "8",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "112",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "29",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "152",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "47",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Montgomery St.",
        "abbr": "MONT",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "6",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "86",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "24",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "44",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "17",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "37",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "57",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "18",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "25",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "11",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "85",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "29",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "49",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "15",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "35",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "55",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "12",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "32",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "52",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "10",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "95",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "30",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "135",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "48",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Powell St.",
        "abbr": "POWL",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "4",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "90",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "23",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "43",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "15",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "35",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "55",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "7",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "20",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "27",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "9",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "91",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "28",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "48",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "17",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "37",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "57",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "11",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "31",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "11",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "76",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "32",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "116",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "50",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Civic Center/UN Plaza",
        "abbr": "CIVC",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "3",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "94",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "21",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "41",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "14",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "34",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "54",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "1",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "8",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "21",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "8",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "95",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "26",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "46",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "19",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "39",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "59",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "9",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "29",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "49",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "12",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "64",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "33",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "104",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "16th St. Mission",
        "abbr": "16TH",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "107",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "19",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "39",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "11",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "31",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "3",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "11",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "23",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "104",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "24",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "44",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "1",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "21",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "41",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "7",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "27",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "47",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "15",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "35",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "93",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "54",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "24th St. Mission",
        "abbr": "24TH",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "17",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "37",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "57",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "9",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "29",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "49",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "13",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "25",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "3",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "109",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "21",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "41",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "3",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "23",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "43",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "24",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "44",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "17",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "37",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "84",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "56",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Glen Park",
        "abbr": "GLEN",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "14",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "34",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "54",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "7",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "27",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "47",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "8",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "16",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "28",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "1",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "128",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "19",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "39",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "6",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "26",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "46",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "2",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "22",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "42",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "19",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "40",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "82",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "59",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Balboa Park",
        "abbr": "BALB",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "12",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "32",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "52",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "4",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "24",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "44",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "10",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "18",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "30",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "16",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "36",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "8",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "28",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "48",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "19",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "39",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "1",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "22",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "42",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "76",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Daly City",
        "abbr": "DALY",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "8",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "28",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "48",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "21",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "41",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Dublin/Pleasanton",
            "abbreviation": "DUBL",
            "limited": "0",
            "estimate": [
              {
                "minutes": "13",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "33",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "BLUE",
                "hexcolor": "#0099cc",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "13",
                "platform": "3",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "33",
                "platform": "3",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "53",
                "platform": "3",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "16",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "36",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "3",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "25",
                "platform": "3",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "46",
                "platform": "3",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "63",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Ashby",
        "abbr": "ASHB",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "25",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "45",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "13",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "33",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "53",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "363",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "7",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "14",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Downtown Berkeley",
        "abbr": "DBRK",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "3",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "23",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "43",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "11",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "31",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "51",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "2",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "339",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "9",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "17",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "North Berkeley",
        "abbr": "NBRK",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "1",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "21",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "41",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "8",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "28",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "48",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "4",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "344",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "11",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "19",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "El Cerrito Plaza",
        "abbr": "PLZA",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "17",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "37",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "25",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "45",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "8",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "347",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "14",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "22",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "El Cerrito del Norte",
        "abbr": "DELN",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "14",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "34",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "2",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "22",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "42",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "10",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "335",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "17",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "25",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Richmond",
        "abbr": "RICH",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "8",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "28",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "16",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "36",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Warm Springs/South Fremont",
        "abbr": "WARM",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "93",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "11",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "19",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "7",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "25",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "45",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "16",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "36",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Milpitas",
        "abbr": "MLPT",
        "etd": [
          {
            "destination": "Berryessa",
            "abbreviation": "BERY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "7",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "67",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "18",
                "platform": "1",
                "direction": "North",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "26",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "18",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "38",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "8",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "28",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Berryessa/North San Jose",
        "abbr": "BERY",
        "etd": [
          {
            "destination": "Daly City",
            "abbreviation": "DALY",
            "limited": "0",
            "estimate": [
              {
                "minutes": "14",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "34",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "GREEN",
                "hexcolor": "#339933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "4",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "24",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "ORANGE",
                "hexcolor": "#ff9933",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Colma",
        "abbr": "COLM",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "5",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "24",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "44",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "17",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "37",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "57",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "12",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "32",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "9",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "29",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "50",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "South San Francisco",
        "abbr": "SSAN",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "2",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "21",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "41",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "Leaving",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "20",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "40",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "9",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "29",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "12",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "32",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "52",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "San Bruno",
        "abbr": "SBRN",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "18",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "38",
                "platform": "2",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "3",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "23",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "43",
                "platform": "1",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "6",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "26",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "SF Airport",
            "abbreviation": "SFIA",
            "limited": "0",
            "estimate": [
              {
                "minutes": "16",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "36",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "56",
                "platform": "1",
                "direction": "South",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "Millbrae",
        "abbr": "MLBR",
        "etd": [
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "15",
                "platform": "3",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "35",
                "platform": "3",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      },
      {
        "name": "San Francisco Int'l Airport",
        "abbr": "SFIA",
        "etd": [
          {
            "destination": "Antioch",
            "abbreviation": "ANTC",
            "limited": "0",
            "estimate": [
              {
                "minutes": "14",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "34",
                "platform": "1",
                "direction": "North",
                "length": "8",
                "color": "YELLOW",
                "hexcolor": "#ffff33",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Millbrae",
            "abbreviation": "MLBR",
            "limited": "0",
            "estimate": [
              {
                "minutes": "9",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "29",
                "platform": "2",
                "direction": "South",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          },
          {
            "destination": "Richmond",
            "abbreviation": "RICH",
            "limited": "0",
            "estimate": [
              {
                "minutes": "2",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              },
              {
                "minutes": "22",
                "platform": "2",
                "direction": "North",
                "length": "6",
                "color": "RED",
                "hexcolor": "#ff0000",
                "bikeflag": "1",
                "delay": "0",
                "cancelflag": "0",
                "dynamicflag": "0"
              }
            ]
          }
        ]
      }
    ],
    "message": "Direction not supported for ALL ETD messages."
  }
}
```

```
{
  "?xml": {
    "@version": "1.0",
    "@encoding": "utf-8"
  },
  "root": {
    "uri": {
      "#cdata-section": "http://api.bart.gov/api/stn.aspx?cmd=stns&json=y"
    },
    "stations": {
      "station": [
        {
          "name": "12th St. Oakland City Center",
          "abbr": "12TH",
          "gtfs_latitude": "37.803768",
          "gtfs_longitude": "-122.271450",
          "address": "1245 Broadway",
          "city": "Oakland",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94612"
        },
        {
          "name": "16th St. Mission",
          "abbr": "16TH",
          "gtfs_latitude": "37.765062",
          "gtfs_longitude": "-122.419694",
          "address": "2000 Mission Street",
          "city": "San Francisco",
          "county": "sanfrancisco",
          "state": "CA",
          "zipcode": "94110"
        },
        {
          "name": "19th St. Oakland",
          "abbr": "19TH",
          "gtfs_latitude": "37.808350",
          "gtfs_longitude": "-122.268602",
          "address": "1900 Broadway",
          "city": "Oakland",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94612"
        },
        {
          "name": "24th St. Mission",
          "abbr": "24TH",
          "gtfs_latitude": "37.752470",
          "gtfs_longitude": "-122.418143",
          "address": "2800 Mission Street",
          "city": "San Francisco",
          "county": "sanfrancisco",
          "state": "CA",
          "zipcode": "94110"
        },
        {
          "name": "Antioch",
          "abbr": "ANTC",
          "gtfs_latitude": "37.995388",
          "gtfs_longitude": "-121.780420",
          "address": "1600 Slatten Ranch Road",
          "city": "Antioch",
          "county": "Contra Costa",
          "state": "CA",
          "zipcode": "94509"
        },
        {
          "name": "Ashby",
          "abbr": "ASHB",
          "gtfs_latitude": "37.852803",
          "gtfs_longitude": "-122.270062",
          "address": "3100 Adeline Street",
          "city": "Berkeley",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94703"
        },
        {
          "name": "Balboa Park",
          "abbr": "BALB",
          "gtfs_latitude": "37.721585",
          "gtfs_longitude": "-122.447506",
          "address": "401 Geneva Avenue",
          "city": "San Francisco",
          "county": "sanfrancisco",
          "state": "CA",
          "zipcode": "94112"
        },
        {
          "name": "Bay Fair",
          "abbr": "BAYF",
          "gtfs_latitude": "37.696924",
          "gtfs_longitude": "-122.126514",
          "address": "15242 Hesperian Blvd.",
          "city": "San Leandro",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94578"
        },
        {
          "name": "Berryessa/North San Jose",
          "abbr": "BERY",
          "gtfs_latitude": "37.368473",
          "gtfs_longitude": "-121.874681",
          "address": "1620 Berryessa Road",
          "city": "San Jose",
          "county": "Santa Clara",
          "state": "CA",
          "zipcode": "95133"
        },
        {
          "name": "Castro Valley",
          "abbr": "CAST",
          "gtfs_latitude": "37.690746",
          "gtfs_longitude": "-122.075602",
          "address": "3301 Norbridge Dr.",
          "city": "Castro Valley",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94546"
        },
        {
          "name": "Civic Center/UN Plaza",
          "abbr": "CIVC",
          "gtfs_latitude": "37.779732",
          "gtfs_longitude": "-122.414123",
          "address": "1150 Market Street",
          "city": "San Francisco",
          "county": "sanfrancisco",
          "state": "CA",
          "zipcode": "94102"
        },
        {
          "name": "Coliseum",
          "abbr": "COLS",
          "gtfs_latitude": "37.753661",
          "gtfs_longitude": "-122.196869",
          "address": "7200 San Leandro St.",
          "city": "Oakland",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94621"
        },
        {
          "name": "Colma",
          "abbr": "COLM",
          "gtfs_latitude": "37.684638",
          "gtfs_longitude": "-122.466233",
          "address": "365 D Street",
          "city": "Colma",
          "county": "sanmateo",
          "state": "CA",
          "zipcode": "94014"
        },
        {
          "name": "Concord",
          "abbr": "CONC",
          "gtfs_latitude": "37.973737",
          "gtfs_longitude": "-122.029095",
          "address": "1451 Oakland Avenue",
          "city": "Concord",
          "county": "contracosta",
          "state": "CA",
          "zipcode": "94520"
        },
        {
          "name": "Daly City",
          "abbr": "DALY",
          "gtfs_latitude": "37.706121",
          "gtfs_longitude": "-122.469081",
          "address": "500 John Daly Blvd.",
          "city": "Daly City",
          "county": "sanmateo",
          "state": "CA",
          "zipcode": "94014"
        },
        {
          "name": "Downtown Berkeley",
          "abbr": "DBRK",
          "gtfs_latitude": "37.870104",
          "gtfs_longitude": "-122.268133",
          "address": "2160 Shattuck Avenue",
          "city": "Berkeley",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94704"
        },
        {
          "name": "Dublin/Pleasanton",
          "abbr": "DUBL",
          "gtfs_latitude": "37.701687",
          "gtfs_longitude": "-121.899179",
          "address": "5801 Owens Dr.",
          "city": "Pleasanton",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94588"
        },
        {
          "name": "El Cerrito del Norte",
          "abbr": "DELN",
          "gtfs_latitude": "37.925086",
          "gtfs_longitude": "-122.316794",
          "address": "6400 Cutting Blvd.",
          "city": "El Cerrito",
          "county": "contracosta",
          "state": "CA",
          "zipcode": "94530"
        },
        {
          "name": "El Cerrito Plaza",
          "abbr": "PLZA",
          "gtfs_latitude": "37.902632",
          "gtfs_longitude": "-122.298904",
          "address": "6699 Fairmount Avenue",
          "city": "El Cerrito",
          "county": "contracosta",
          "state": "CA",
          "zipcode": "94530"
        },
        {
          "name": "Embarcadero",
          "abbr": "EMBR",
          "gtfs_latitude": "37.792874",
          "gtfs_longitude": "-122.397020",
          "address": "298 Market Street",
          "city": "San Francisco",
          "county": "sanfrancisco",
          "state": "CA",
          "zipcode": "94111"
        },
        {
          "name": "Fremont",
          "abbr": "FRMT",
          "gtfs_latitude": "37.557465",
          "gtfs_longitude": "-121.976608",
          "address": "2000 BART Way",
          "city": "Fremont",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94536"
        },
        {
          "name": "Fruitvale",
          "abbr": "FTVL",
          "gtfs_latitude": "37.774836",
          "gtfs_longitude": "-122.224175",
          "address": "3401 East 12th Street",
          "city": "Oakland",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94601"
        },
        {
          "name": "Glen Park",
          "abbr": "GLEN",
          "gtfs_latitude": "37.733064",
          "gtfs_longitude": "-122.433817",
          "address": "2901 Diamond Street",
          "city": "San Francisco",
          "county": "sanfrancisco",
          "state": "CA",
          "zipcode": "94131"
        },
        {
          "name": "Hayward",
          "abbr": "HAYW",
          "gtfs_latitude": "37.669723",
          "gtfs_longitude": "-122.087018",
          "address": "699 'B' Street",
          "city": "Hayward",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94541"
        },
        {
          "name": "Lafayette",
          "abbr": "LAFY",
          "gtfs_latitude": "37.893176",
          "gtfs_longitude": "-122.124630",
          "address": "3601 Deer Hill Road",
          "city": "Lafayette",
          "county": "contracosta",
          "state": "CA",
          "zipcode": "94549"
        },
        {
          "name": "Lake Merritt",
          "abbr": "LAKE",
          "gtfs_latitude": "37.797027",
          "gtfs_longitude": "-122.265180",
          "address": "800 Madison Street",
          "city": "Oakland",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94607"
        },
        {
          "name": "MacArthur",
          "abbr": "MCAR",
          "gtfs_latitude": "37.829065",
          "gtfs_longitude": "-122.267040",
          "address": "555 40th Street",
          "city": "Oakland",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94609"
        },
        {
          "name": "Millbrae",
          "abbr": "MLBR",
          "gtfs_latitude": "37.600271",
          "gtfs_longitude": "-122.386702",
          "address": "200 North Rollins Road",
          "city": "Millbrae",
          "county": "sanmateo",
          "state": "CA",
          "zipcode": "94030"
        },
        {
          "name": "Milpitas",
          "abbr": "MLPT",
          "gtfs_latitude": "37.410277",
          "gtfs_longitude": "-121.891081",
          "address": "1755 S. Milpitas Blvd.",
          "city": "Milpitas",
          "county": "Santa Clara",
          "state": "CA",
          "zipcode": "95035"
        },
        {
          "name": "Montgomery St.",
          "abbr": "MONT",
          "gtfs_latitude": "37.789405",
          "gtfs_longitude": "-122.401066",
          "address": "598 Market Street",
          "city": "San Francisco",
          "county": "sanfrancisco",
          "state": "CA",
          "zipcode": "94104"
        },
        {
          "name": "North Berkeley",
          "abbr": "NBRK",
          "gtfs_latitude": "37.873967",
          "gtfs_longitude": "-122.283440",
          "address": "1750 Sacramento Street",
          "city": "Berkeley",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94702"
        },
        {
          "name": "North Concord/Martinez",
          "abbr": "NCON",
          "gtfs_latitude": "38.003193",
          "gtfs_longitude": "-122.024653",
          "address": "3700 Port Chicago Highway",
          "city": "Concord",
          "county": "contracosta",
          "state": "CA",
          "zipcode": "94520"
        },
        {
          "name": "Oakland International Airport",
          "abbr": "OAKL",
          "gtfs_latitude": "37.713238",
          "gtfs_longitude": "-122.212191",
          "address": "4 Airport Drive",
          "city": "Oakland",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94621"
        },
        {
          "name": "Orinda",
          "abbr": "ORIN",
          "gtfs_latitude": "37.878361",
          "gtfs_longitude": "-122.183791",
          "address": "11 Camino Pablo",
          "city": "Orinda",
          "county": "contracosta",
          "state": "CA",
          "zipcode": "94563"
        },
        {
          "name": "Pittsburg/Bay Point",
          "abbr": "PITT",
          "gtfs_latitude": "38.018914",
          "gtfs_longitude": "-121.945154",
          "address": "1700 West Leland Road",
          "city": "Pittsburg",
          "county": "contracosta",
          "state": "CA",
          "zipcode": "94565"
        },
        {
          "name": "Pittsburg Center",
          "abbr": "PCTR",
          "gtfs_latitude": "38.016941",
          "gtfs_longitude": "-121.889457",
          "address": "2099 Railroad Avenue",
          "city": "Pittsburg",
          "county": "Contra Costa",
          "state": "CA",
          "zipcode": "94565"
        },
        {
          "name": "Pleasant Hill/Contra Costa Centre",
          "abbr": "PHIL",
          "gtfs_latitude": "37.928468",
          "gtfs_longitude": "-122.056012",
          "address": "1365 Treat Blvd.",
          "city": "Walnut Creek",
          "county": "contracosta",
          "state": "CA",
          "zipcode": "94597"
        },
        {
          "name": "Powell St.",
          "abbr": "POWL",
          "gtfs_latitude": "37.784471",
          "gtfs_longitude": "-122.407974",
          "address": "899 Market Street",
          "city": "San Francisco",
          "county": "sanfrancisco",
          "state": "CA",
          "zipcode": "94102"
        },
        {
          "name": "Richmond",
          "abbr": "RICH",
          "gtfs_latitude": "37.936853",
          "gtfs_longitude": "-122.353099",
          "address": "1700 Nevin Avenue",
          "city": "Richmond",
          "county": "contracosta",
          "state": "CA",
          "zipcode": "94801"
        },
        {
          "name": "Rockridge",
          "abbr": "ROCK",
          "gtfs_latitude": "37.844702",
          "gtfs_longitude": "-122.251371",
          "address": "5660 College Avenue",
          "city": "Oakland",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94618"
        },
        {
          "name": "San Bruno",
          "abbr": "SBRN",
          "gtfs_latitude": "37.637761",
          "gtfs_longitude": "-122.416287",
          "address": "1151 Huntington Avenue",
          "city": "San Bruno",
          "county": "sanmateo",
          "state": "CA",
          "zipcode": "94066"
        },
        {
          "name": "San Francisco International Airport",
          "abbr": "SFIA",
          "gtfs_latitude": "37.615966",
          "gtfs_longitude": "-122.392409",
          "address": "International Terminal, Level 3",
          "city": "San Francisco Int'l Airport",
          "county": "sanmateo",
          "state": "CA",
          "zipcode": "94128"
        },
        {
          "name": "San Leandro",
          "abbr": "SANL",
          "gtfs_latitude": "37.721947",
          "gtfs_longitude": "-122.160844",
          "address": "1401 San Leandro Blvd.",
          "city": "San Leandro",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94577"
        },
        {
          "name": "South Hayward",
          "abbr": "SHAY",
          "gtfs_latitude": "37.634375",
          "gtfs_longitude": "-122.057189",
          "address": "28601 Dixon Street",
          "city": "Hayward",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94544"
        },
        {
          "name": "South San Francisco",
          "abbr": "SSAN",
          "gtfs_latitude": "37.664245",
          "gtfs_longitude": "-122.443960",
          "address": "1333 Mission Road",
          "city": "South San Francisco",
          "county": "sanmateo",
          "state": "CA",
          "zipcode": "94080"
        },
        {
          "name": "Union City",
          "abbr": "UCTY",
          "gtfs_latitude": "37.590630",
          "gtfs_longitude": "-122.017388",
          "address": "10 Union Square",
          "city": "Union City",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94587"
        },
        {
          "name": "Walnut Creek",
          "abbr": "WCRK",
          "gtfs_latitude": "37.905522",
          "gtfs_longitude": "-122.067527",
          "address": "200 Ygnacio Valley Road",
          "city": "Walnut Creek",
          "county": "contracosta",
          "state": "CA",
          "zipcode": "94596"
        },
        {
          "name": "Warm Springs/South Fremont",
          "abbr": "WARM",
          "gtfs_latitude": "37.502171",
          "gtfs_longitude": "-121.939313",
          "address": "45193 Warm Springs Blvd",
          "city": "Fremont",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94539"
        },
        {
          "name": "West Dublin/Pleasanton",
          "abbr": "WDUB",
          "gtfs_latitude": "37.699756",
          "gtfs_longitude": "-121.928240",
          "address": "6501 Golden Gate Drive",
          "city": "Dublin",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94568"
        },
        {
          "name": "West Oakland",
          "abbr": "WOAK",
          "gtfs_latitude": "37.804872",
          "gtfs_longitude": "-122.295140",
          "address": "1451 7th Street",
          "city": "Oakland",
          "county": "alameda",
          "state": "CA",
          "zipcode": "94607"
        }
      ]
    },
    "message": ""
  }
}
```

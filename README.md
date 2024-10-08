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
- https://developers.home-assistant.io/blog/2024/04/30/store-runtime-data-inside-config-entry/
- https://developers.home-assistant.io/docs/integration_fetching_data/#coordinated-single-api-poll-for-data-for-all-entities
- https://developers.home-assistant.io/blog/2024/08/05/coordinator_async_setup/
- https://developers.home-assistant.io/blog/2024/05/01/improved-hass-data-typing
- https://github.com/home-assistant/core/blob/dev/homeassistant/components/airnow/__init__.py#L96
- https://developers.home-assistant.io/docs/core/entity/#entity-naming
  - Entity naming (this needs a redo)

## Bart Dev Info

- https://api.bart.gov/docs/bsa/bsa.aspx
  - Advisory endpoint (maybe a text sensor for this as well, with its own data update coordinator)
- https://api.bart.gov/docs/stn/stns.aspx
  - All stations (could use this for testing config flow better)

## UI Prototype Cards

For trains going north:

```yaml
type: entity-filter
state_filter:
  - operator: "=="
    value: North
    attribute: direction
entities:
  - sensor.24th_street
  - sensor.antioch
  - sensor.berryessa
  - sensor.daly_city
  - sensor.dublin_pleasanton
  - sensor.fremont
  - sensor.millbrae
  - sensor.pittsburg_bay_point
  - sensor.richmond
  - sensor.sf_airport
  - sensor.sfo_millbrae
card:
  title: North
```

For trains going south:

```yaml
type: entity-filter
state_filter:
  - operator: "=="
    value: South
    attribute: direction
entities:
  - sensor.24th_street
  - sensor.antioch
  - sensor.berryessa
  - sensor.daly_city
  - sensor.dublin_pleasanton
  - sensor.fremont
  - sensor.millbrae
  - sensor.pittsburg_bay_point
  - sensor.richmond
  - sensor.sf_airport
  - sensor.sfo_millbrae
card:
  title: South
```

For announcements:

```yaml
type: entities
entities:
  - entity: binary_sensor.bart_has_announcements
  - entity: sensor.announcement
title: Announcements
show_header_toggle: false
state_color: true
```

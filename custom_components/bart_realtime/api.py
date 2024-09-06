"""Sample API Client."""
import asyncio
import logging
import socket
from typing import Optional
from dataclasses import dataclass

import aiohttp
import async_timeout
import xmltodict

from .const import DEFAULT_BART_API_BASE_URL


TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)


@dataclass(frozen=True, kw_only=True)
class TrainEstimateResponse:
    bikeflag: str
    cancelflag: str
    color: str
    delay: str
    direction: str
    dynamicflag: str
    hexcolor: str
    length: str
    minutes: str
    platform: str

    @classmethod
    def from_response(cls, input_data):
        return cls(
            bikeflag=input_data['bikeflag'],
            cancelflag=input_data['cancelflag'],
            color=input_data['color'],
            delay=input_data['delay'],
            direction=input_data['direction'],
            dynamicflag=input_data['dynamicflag'],
            hexcolor=input_data['hexcolor'],
            length=input_data['length'],
            minutes=input_data['minutes'],
            platform=input_data['platform'],
        )


@dataclass(frozen=True, kw_only=True)
class TrainLineResponse:
    abbreviation: str
    destination: str
    limited: str
    estimates: list[TrainEstimateResponse] = None

    @classmethod
    def from_response(cls, input_data):
        all_estimates = input_data['estimate']
        final_estimates = [TrainEstimateResponse.from_response(e) for e in all_estimates]
        return cls(
            abbreviation=input_data['abbreviation'],
            destination=input_data['destination'],
            limited=input_data['limited'],
            estimates=final_estimates,
        )

    @property
    def latest_estimate(self):
        return self.estimates[0]

    @property
    def latest_minutes(self):
        return self.latest_estimate.minutes

    @property
    def latest_direction(self):
        return self.latest_estimate.direction


class BartRootResponseException(Exception):
    pass


@dataclass(frozen=True, kw_only=True)
class BartRootResponse:
    # TODO: need to turn into a datetime object
    response_date: str
    response_time: str
    station_abbreviation: str
    station_name: str
    message: Optional[str] = None
    train_lines: dict = None

    @classmethod
    def from_response(cls, input_data):
        final_train_lines_data = {}

        root_data = input_data['root']
        if not root_data:
            # TODO: raise exception instead
            raise BartRootResponseException('no root data')

        root_date = root_data['date']
        root_message = root_data['message']
        root_time = root_data['time']

        station_data = root_data['station']
        station_abbreviation = station_data['abbr']
        station_name = station_data['name']

        train_lines_data = station_data['etd']
        for train_line in train_lines_data:
            _LOGGER.debug(
                "Transform train times train_line: %s",
                train_line)
            train_line_key = train_line['destination']
            train_line_response = TrainLineResponse.from_response(train_line)
            final_train_lines_data[train_line_key] = train_line_response

        return cls(
            response_date=root_date,
            response_time=root_time,
            station_abbreviation=station_abbreviation,
            station_name=station_name,
            message=root_message,
            train_lines=final_train_lines_data,
        )

    def get_current_train_data(self, train_name):
        return self.train_lines.get(train_name)

    def get_current_train_minutes(self, train_name):
        return self.get_current_train_data(train_name).latest_minutes

    def get_current_train_direction(self, train_name):
        return self.get_current_train_data(train_name).latest_direction


class BartRealtimeApiClient:
    def __init__(
        self, api_key: str, station: str, session: aiohttp.ClientSession
    ) -> None:
        """Sample API Client."""
        self._api_key = api_key
        self._station = station
        self._session = session

    @property
    def base_url(self):
        return DEFAULT_BART_API_BASE_URL

    @property
    def api_key(self):
        return self._api_key

    @property
    def station(self):
        return self._station

    async def async_get_data(self) -> BartRootResponse:
        """Get data from the API."""
        return await self.async_get_transformed_train_times()

    async def async_get_xml_train_times(self) -> dict:
        """Get data from the API."""
        return await self.api_wrapper("get", self.base_url)

    async def async_get_sanitized_train_times(self) -> dict:
        """Get data from the API."""
        xml_train_times = await self.async_get_xml_train_times()
        _LOGGER.debug(
            "Data fetched async xml_train_times: %s",
            xml_train_times)
        return self.data_without_xml(xml_train_times)

    @classmethod
    def transform_train_times(cls, input_data) -> BartRootResponse:
        _LOGGER.debug(
            "Transform train times input_data: %s",
            input_data)

        bart_response = BartRootResponse.from_response(input_data)

        _LOGGER.debug(
            "Transform train times bart_response: %s",
            bart_response)
        return bart_response

    async def async_get_transformed_train_times(self) -> BartRootResponse:
        """Get data from the API."""
        san_train_times = await self.async_get_sanitized_train_times()
        _LOGGER.debug(
            "Data fetched async san_train_times: %s",
            san_train_times)
        return self.transform_train_times(san_train_times)

    @classmethod
    def data_without_xml(self, input_data) -> str | None:
        """If the data is an XML string, convert it to a JSON string."""
        _LOGGER.debug("Data fetched from resource: %s", input_data)
        value = xmltodict.parse(input_data)
        _LOGGER.debug("JSON converted from XML: %s", value)
        return value

    async def api_wrapper(
        self, method: str, url: str, data: dict = {}, headers: dict = {}
    ) -> dict:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(TIMEOUT):
                if method == "get":
                    response = await self._session.get(url, headers=headers)
                    return await response.text()

                elif method == "put":
                    await self._session.put(url, headers=headers, json=data)

                elif method == "patch":
                    await self._session.patch(url, headers=headers, json=data)

                elif method == "post":
                    await self._session.post(url, headers=headers, json=data)

        except asyncio.TimeoutError as exception:
            _LOGGER.error(
                "Timeout error fetching information from %s - %s",
                url,
                exception,
            )

        except (KeyError, TypeError) as exception:
            _LOGGER.error(
                "Error parsing information from %s - %s",
                url,
                exception,
            )
        except (aiohttp.ClientError, socket.gaierror) as exception:
            _LOGGER.error(
                "Error fetching information from %s - %s",
                url,
                exception,
            )
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.error("Something really wrong happened! - %s", exception)

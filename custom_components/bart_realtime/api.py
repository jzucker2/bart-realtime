"""Sample API Client."""

import asyncio
import logging
import socket

import aiohttp
import async_timeout

from .bart_api_response import (
    BartBSARootResponse,
    BartETDRootResponse,
    BartStationsRootResponse,
)
from .const import DEFAULT_API_KEY

TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)


class BartRealtimeApiClient:
    def __init__(
        self,
        station: str,
        session: aiohttp.ClientSession,
        api_key: str = DEFAULT_API_KEY,
    ) -> None:
        """Sample API Client."""
        self._api_key = api_key
        self._station = station
        self._session = session
        self._base_url = self.build_base_url(station, api_key=api_key)
        self._announcement_base_url = self.build_base_announcement_url(api_key=api_key)
        self._station_base_url = self.build_base_stations_url(api_key=api_key)

    @classmethod
    def build_base_url(cls, station_abbr, api_key=DEFAULT_API_KEY):
        base_url = f"https://api.bart.gov/api/etd.aspx?cmd=etd&orig={station_abbr}&key={api_key}&json=y"
        _LOGGER.debug("bart api client building base_url: %s", base_url)
        return base_url

    @classmethod
    def build_base_announcement_url(cls, api_key=DEFAULT_API_KEY):
        a_base_url = f"https://api.bart.gov/api/bsa.aspx?cmd=bsa&key={api_key}&json=y"
        _LOGGER.debug("bart api client building announcement base_url: %s", a_base_url)
        return a_base_url

    @classmethod
    def build_base_stations_url(cls, api_key=DEFAULT_API_KEY):
        s_base_url = f"https://api.bart.gov/api/stn.aspx?cmd=stns&key={api_key}&json=y"
        _LOGGER.debug("bart api client building stations base_url: %s", s_base_url)
        return s_base_url

    @property
    def base_url(self):
        return self._base_url

    @property
    def announcement_base_url(self):
        return self._announcement_base_url

    @property
    def station_base_url(self):
        return self._station_base_url

    @property
    def api_key(self):
        return self._api_key

    @property
    def station(self):
        return self._station

    async def async_validate(self) -> BartETDRootResponse:
        """Validate by getting data from the API."""
        # TODO: add a check for station in all stations and maybe even call station detail
        return await self.async_get_data()

    async def async_get_data(self) -> BartETDRootResponse:
        """Get data from the API."""
        return await self.async_get_transformed_train_times()

    async def async_get_json_train_times(self) -> dict:
        """Get data from the API."""
        return await self.api_wrapper("get", self.base_url)

    @classmethod
    def transform_train_times(cls, input_data) -> BartETDRootResponse:
        _LOGGER.debug("Transform train times input_data: %s", input_data)

        bart_response = BartETDRootResponse.from_response(input_data)

        _LOGGER.debug("Transform train times bart_response: %s", bart_response)
        return bart_response

    async def async_get_transformed_train_times(self) -> BartETDRootResponse:
        """Get data from the API."""
        json_train_times = await self.async_get_json_train_times()
        _LOGGER.debug(
            "Data fetched for transform async json_train_times: %s", json_train_times
        )
        return self.transform_train_times(json_train_times)

    async def async_get_json_announcements(self) -> dict:
        """Get data from the API."""
        return await self.api_wrapper("get", self.announcement_base_url)

    @classmethod
    def transform_announcements(cls, input_data) -> BartBSARootResponse:
        _LOGGER.debug("Transform announcements input_data: %s", input_data)

        bart_response = BartBSARootResponse.from_response(input_data)

        _LOGGER.debug("Transform announcements bart_response: %s", bart_response)
        return bart_response

    async def async_get_transformed_announcements(self) -> BartBSARootResponse:
        """Get data from the API."""
        json_announcements = await self.async_get_json_announcements()
        _LOGGER.debug(
            "Data fetched for transform async json_announcements: %s",
            json_announcements,
        )
        return self.transform_announcements(json_announcements)

    async def async_get_json_stations(self) -> dict:
        """Get data from the API."""
        return await self.api_wrapper("get", self.station_base_url)

    @classmethod
    def transform_stations(cls, input_data) -> BartStationsRootResponse:
        _LOGGER.debug("Transform stations input_data: %s", input_data)

        bart_response = BartStationsRootResponse.from_response(input_data)

        _LOGGER.debug("Transform stations bart_response: %s", bart_response)
        return bart_response

    async def async_get_transformed_stations(self) -> BartStationsRootResponse:
        """Get data from the API."""
        json_stations = await self.async_get_json_stations()
        _LOGGER.debug(
            "Data fetched for transform async json_stations: %s",
            json_stations,
        )
        return self.transform_stations(json_stations)

    async def api_wrapper(
        self, method: str, url: str, data: dict = {}, headers: dict = {}
    ) -> dict:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(TIMEOUT):
                if method == "get":
                    response = await self._session.get(url, headers=headers)
                    return await response.json()

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

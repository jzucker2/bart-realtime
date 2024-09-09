"""Sample API Client."""

import asyncio
import logging
import socket

import aiohttp
import async_timeout

from .bart_api_response import BartETDRootResponse
from .const import DEFAULT_API_KEY

TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)


class BartRealtimeApiClient:
    def __init__(
        self, api_key: str, station: str, session: aiohttp.ClientSession
    ) -> None:
        """Sample API Client."""
        self._api_key = api_key
        self._station = station
        self._session = session
        # TODO: start supplying or allowing an api_key
        self._base_url = self.build_base_url(station)

    @classmethod
    def build_base_url(cls, station_abbr, api_key=DEFAULT_API_KEY):
        base_url = f"https://api.bart.gov/api/etd.aspx?cmd=etd&orig={station_abbr}&key={api_key}&json=y"
        _LOGGER.debug("bart api client building base_url: %s", base_url)
        return base_url

    @property
    def base_url(self):
        return self._base_url

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

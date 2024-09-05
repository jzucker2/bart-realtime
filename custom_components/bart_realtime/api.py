"""Sample API Client."""
import asyncio
import logging
import socket

import aiohttp
import async_timeout
import xmltodict


from homeassistant.helpers.json import json_dumps


from .const import XML_MIME_TYPES, DEFAULT_ENCODING, DEFAULT_BART_API_BASE_URL


TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)

# HEADERS = {"Content-type": "application/json; charset=UTF-8"}
# TODO: double check this I think
HEADERS = {"Content-type": "application/xml; charset=UTF-8"}


class BartRealtimeApiClient:
    def __init__(
        self, api_key: str, session: aiohttp.ClientSession
    ) -> None:
        """Sample API Client."""
        self._api_key = api_key
        self._session = session

    @property
    def base_url(self):
        return DEFAULT_BART_API_BASE_URL

    async def async_get_data(self) -> dict:
        """Get data from the API."""
        return await self.async_get_sanitized_train_times()

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
    def data_without_xml(self, input_data) -> str | None:
        """If the data is an XML string, convert it to a JSON string."""
        _LOGGER.debug("Data fetched from resource: %s", input_data)
        value = json_dumps(xmltodict.parse(input_data))
        _LOGGER.debug("JSON converted from XML: %s", value)
        # if (
        #     (value := input_data) is not None
        #     # If the http request failed, headers will be None
        #     and (headers := self.headers) is not None
        #     and (content_type := headers.get("content-type"))
        #     and content_type.startswith(XML_MIME_TYPES)
        # ):
        #     value = json_dumps(xmltodict.parse(value))
        #     _LOGGER.debug("JSON converted from XML: %s", value)
        return value

    async def api_wrapper(
        self, method: str, url: str, data: dict = {}, headers: dict = {}
    ) -> dict:
        """Get information from the API."""
        try:
            async with async_timeout.timeout(TIMEOUT, loop=asyncio.get_event_loop()):
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

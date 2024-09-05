#!/usr/bin/env python3

import asyncio
import pprint

import aiohttp

from custom_components.bart_realtime.api import BartRealtimeApiClient


async def main():
    async with aiohttp.ClientSession() as client:
        bart_api = BartRealtimeApiClient("api_key", client)
        games = await bart_api.async_get_sanitized_train_times()
        pprint.pprint(games)
        print(len(games))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

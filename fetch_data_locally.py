#!/usr/bin/env python3
import asyncio
import pprint

import aiohttp
from custom_components.bart_realtime.api import BartRealtimeApiClient
from custom_components.bart_realtime.bart_trains import BartTrainLines


API_KEY = "api_key"
STATION = "16TH"


async def main():
    all_train_lines = BartTrainLines.get_all_train_lines()
    print(f'Going with all_train_lines: {all_train_lines}')
    async with aiohttp.ClientSession() as client:
        bart_api = BartRealtimeApiClient(API_KEY, STATION, client)
        # First do raw xml train times
        xml_train_times = await bart_api.async_get_xml_train_times()
        print('Raw xml train times incoming')
        pprint.pprint(xml_train_times)
        print(f'Type of xml_train_times => {type(xml_train_times)}')
        print(f'Length of xml_train_times => {len(xml_train_times)}')
        # Now do sanitized train times
        train_times = await bart_api.async_get_sanitized_train_times()
        print('Sanitized train times incoming')
        pprint.pprint(train_times)
        print(f'Type of train_times => {type(train_times)}')
        print(f'Length of train_times => {len(train_times)}')


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

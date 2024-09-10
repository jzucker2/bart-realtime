#!/usr/bin/env python3
import asyncio
import pprint
import sys

import aiohttp

from custom_components.bart_realtime.api import BartRealtimeApiClient
from custom_components.bart_realtime.bart_trains import BartTrainLines

API_KEY = "api_key"
STATION = "16TH"
TEST_TRAIN = "Antioch"


# https://stackoverflow.com/questions/73884117/how-to-replace-asyncio-get-event-loop-to-avoid-the-deprecationwarning
def get_current_event_loop():
    if sys.version_info < (3, 10):
        loop = asyncio.get_event_loop()
    else:
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()

        asyncio.set_event_loop(loop)
    return loop


async def main():
    all_train_lines = BartTrainLines.get_all_train_lines()
    print(f"Going with all_train_lines: {all_train_lines}")
    async with aiohttp.ClientSession() as client:
        bart_api = BartRealtimeApiClient(API_KEY, STATION, client)
        # First validate credentials like in auth flow
        validation_response = await bart_api.async_validate()
        print("First validation response")
        pprint.pprint(validation_response)
        # First do raw xml train times
        json_train_times = await bart_api.async_get_json_train_times()
        print("Raw json train times incoming")
        pprint.pprint(json_train_times)
        print(f"Type of json_train_times => {type(json_train_times)}")
        print(f"Length of json_train_times => {len(json_train_times)}")
        # Now do transformed train times
        tran_train_times = await bart_api.async_get_transformed_train_times()
        print("Transformed train times incoming")
        pprint.pprint(tran_train_times)
        print(f"Type of tran_train_times => {type(tran_train_times)}")
        latest_minutes = tran_train_times.get_current_train_minutes(TEST_TRAIN)
        latest_direction = tran_train_times.get_current_train_direction(TEST_TRAIN)
        has_current_train_data = tran_train_times.has_current_train_data(TEST_TRAIN)
        print(
            f"For TEST_TRAIN: {TEST_TRAIN} got "
            f"latest_minutes: {latest_minutes} in "
            f"latest_direction: {latest_direction} "
            f"with has_current_train_data: {has_current_train_data}"
        )


if __name__ == "__main__":
    loop = get_current_event_loop()
    loop.run_until_complete(main())

from dataclasses import dataclass
import logging
from typing import Optional

_LOGGER: logging.Logger = logging.getLogger(__package__)


class BartResponseBaseException(Exception):
    pass


class BartRootResponseException(BartResponseBaseException):
    pass


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
            bikeflag=input_data["bikeflag"],
            cancelflag=input_data["cancelflag"],
            color=input_data["color"],
            delay=input_data["delay"],
            direction=input_data["direction"],
            dynamicflag=input_data["dynamicflag"],
            hexcolor=input_data["hexcolor"],
            length=input_data["length"],
            minutes=input_data["minutes"],
            platform=input_data["platform"],
        )


@dataclass(frozen=True, kw_only=True)
class TrainLineResponse:
    abbreviation: str
    destination: str
    limited: str
    estimates: list[TrainEstimateResponse] = None

    @classmethod
    def from_response(cls, input_data):
        all_estimates = input_data["estimate"]
        final_estimates = [
            TrainEstimateResponse.from_response(e) for e in all_estimates
        ]
        return cls(
            abbreviation=input_data["abbreviation"],
            destination=input_data["destination"],
            limited=input_data["limited"],
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


@dataclass(frozen=True, kw_only=True)
class BartETDRootResponse:
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

        root_data = input_data["root"]
        if not root_data:
            # TODO: make sure I properly handle this exception
            raise BartRootResponseException("no root data")

        root_date = root_data["date"]
        root_message = root_data["message"]
        root_time = root_data["time"]

        station_list = root_data["station"]
        # assume always 1 station in list!
        station_data = station_list[0]
        station_abbreviation = station_data["abbr"]
        station_name = station_data["name"]

        train_lines_data = station_data["etd"]
        for train_line in train_lines_data:
            _LOGGER.debug("Build response train times train_line: %s", train_line)
            train_line_key = train_line["destination"]
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

    @property
    def is_connected(self):
        if not self.response_date:
            return False
        if not self.response_time:
            return False
        return True

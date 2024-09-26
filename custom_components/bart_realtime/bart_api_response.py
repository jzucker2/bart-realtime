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
    def all_estimates(self):
        return [e.minutes for e in self.estimates]

    @property
    def latest_minutes(self):
        return self.latest_estimate.minutes

    @property
    def latest_direction(self):
        return self.latest_estimate.direction

    @property
    def latest_delay(self):
        return self.latest_estimate.delay

    @property
    def latest_color(self):
        return self.latest_estimate.color

    @property
    def latest_hexcolor(self):
        return self.latest_estimate.hexcolor


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

        train_lines_data = station_data.get("etd", [])
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

    def has_current_train_data(self, train_name):
        train_data = self.train_lines.get(train_name)
        return bool(train_data is not None)

    def get_current_train_all_estimates(self, train_name):
        return self.get_current_train_data(train_name).all_estimates

    def get_current_train_minutes(self, train_name):
        return self.get_current_train_data(train_name).latest_minutes

    def get_current_train_direction(self, train_name):
        return self.get_current_train_data(train_name).latest_direction

    def get_current_train_delay(self, train_name):
        return self.get_current_train_data(train_name).latest_delay

    def get_current_train_color(self, train_name):
        return self.get_current_train_data(train_name).latest_color

    def get_current_train_hexcolor(self, train_name):
        return self.get_current_train_data(train_name).latest_hexcolor

    @property
    def is_connected(self):
        if not self.response_date:
            return False
        if not self.response_time:
            return False
        return True


@dataclass(frozen=True, kw_only=True)
class BSAAnnouncement:
    station: str
    description: str
    sms_text: str
    id: Optional[str] = None
    type: Optional[str] = None
    posted: Optional[str] = None
    expires: Optional[str] = None

    @classmethod
    def from_response(cls, input_data):
        description_dict = input_data["description"]
        sms_dict = input_data["sms_text"]
        return cls(
            station=input_data["station"],
            description=description_dict["#cdata-section"],
            sms_text=sms_dict["#cdata-section"],
            id=input_data.get("@id"),
            type=input_data.get("type"),
            posted=input_data.get("posted"),
            expires=input_data.get("expires"),
        )


@dataclass(frozen=True, kw_only=True)
class BartBSARootResponse:
    # TODO: need to turn into a datetime object
    response_date: str
    response_time: str
    message: Optional[str] = None
    announcements: list = None

    @classmethod
    def from_response(cls, input_data):
        final_announcements = []

        root_data = input_data["root"]
        if not root_data:
            # TODO: make sure I properly handle this exception
            raise BartRootResponseException("no root data")

        root_date = root_data["date"]
        root_message = root_data["message"]
        root_time = root_data["time"]

        announcements = root_data["bsa"]

        for announcement in announcements:
            _LOGGER.debug("Build response announcement: %s", announcement)
            announcement_response = BSAAnnouncement.from_response(announcement)
            final_announcements.append(announcement_response)

        return cls(
            response_date=root_date,
            response_time=root_time,
            message=root_message,
            announcements=final_announcements,
        )

    def has_current_announcements(self):
        announcements = self.announcements
        _LOGGER.debug("Checking has current announcements: %s", announcements)
        if not announcements:
            return False
        if not len(announcements):
            return False
        first_announcement = announcements[0]
        if (
            first_announcement.id is None
            and first_announcement.posted is None
            and first_announcement.expires is None
        ):
            return False
        return True

    def get_first_announcement(self):
        return self.announcements[0]

    def get_first_announcement_id(self):
        return self.get_first_announcement().id

    def get_first_announcement_type(self):
        return self.get_first_announcement().type

    def get_first_announcement_station(self):
        return self.get_first_announcement().station

    def get_first_announcement_description(self):
        return self.get_first_announcement().description

    def get_first_announcement_sms_text(self):
        return self.get_first_announcement().sms_text

    def get_first_announcement_posted(self):
        return self.get_first_announcement().posted

    def get_first_announcement_expires(self):
        return self.get_first_announcement().expires

    @property
    def is_connected(self):
        if not self.response_date:
            return False
        if not self.response_time:
            return False
        return True


@dataclass(frozen=True, kw_only=True)
class BartStation:
    name: str
    abbreviation: str
    gtfs_latitude: str
    gtfs_longitude: str
    address: str
    city: str
    county: str
    state: str
    zipcode: str

    @classmethod
    def from_response(cls, input_data):
        return cls(
            name=input_data["name"],
            abbreviation=input_data["abbr"],
            gtfs_latitude=input_data["gtfs_latitude"],
            gtfs_longitude=input_data["gtfs_longitude"],
            address=input_data["address"],
            city=input_data["city"],
            county=input_data["county"],
            state=input_data["state"],
            zipcode=input_data["zipcode"],
        )


@dataclass(frozen=True, kw_only=True)
class BartStationsRootResponse:
    message: Optional[str] = None
    stations: list = None

    @classmethod
    def from_response(cls, input_data):
        final_stations = []

        root_data = input_data["root"]
        if not root_data:
            # TODO: make sure I properly handle this exception
            raise BartRootResponseException("no root data")

        root_message = root_data["message"]

        stations_root = root_data["stations"]
        actual_stations = stations_root["station"]

        for station in actual_stations:
            _LOGGER.debug("Build response station: %s", station)
            station_response = BartStation.from_response(station)
            final_stations.append(station_response)

        return cls(
            message=root_message,
            stations=final_stations,
        )

    def get_stations_options_list(self):
        return list([s.abbreviation for s in self.stations])

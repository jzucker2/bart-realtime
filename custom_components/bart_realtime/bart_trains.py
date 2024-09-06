from enum import Enum


class BartTrainLinesException(Exception):
    pass


class BartTrainLines(Enum):
    ANTIOCH = 'Antioch'
    DALY_CITY = 'Daly City'
    DUBLIN_PLEASANTON = 'Dublin/Pleasanton'
    MILLBRAE = 'Millbrae'
    RICHMOND = 'Richmond'
    SF_AIRPORT = 'SF Airport'
    SFO_MILLBRAE = 'SFO/Millbrae'
    PITTSBURG_BAY_POINT = 'Pittsburg/Bay Point'
    BERRYESSA = 'Berryessa'
    TWENTY_FOURTH_ST = '24th Street'

    @property
    def friendly_name(self):
        return self.value

    @property
    def abbreviation(self):
        if self == self.ANTIOCH:
            return 'ANTC'
        elif self == self.DALY_CITY:
            return 'DALY'
        elif self == self.DUBLIN_PLEASANTON:
            return 'DUBL'
        elif self == self.MILLBRAE:
            return 'MLBR'
        elif self == self.RICHMOND:
            return 'RICH'
        elif self == self.SF_AIRPORT:
            return 'SFIA'
        elif self == self.SFO_MILLBRAE:
            return 'MLBR'
        elif self == self.PITTSBURG_BAY_POINT:
            return 'PITT'
        elif self == self.BERRYESSA:
            return 'BERY'
        elif self == self.TWENTY_FOURTH_ST:
            # TODO: double check this one
            return '24TH'
        raise BartTrainLinesException(f'unknown abbr for type self: {self}')

    @classmethod
    def get_all_train_lines(cls):
        # could I also do `list(cls)`?
        return list([b for b in cls])


class BartTrainLineDirections(Enum):
    NORTH = 'North'
    SOUTH = 'South'

    @property
    def friendly_name(self):
        return self.value

from enum import StrEnum, auto, IntEnum, Enum

class Role(str, Enum):
    ADMIN = 'ADMIN'
    MONITOR = 'MONITOR'
    STUDENT = 'STUDENT'

class Week(str, Enum):
    UPPER = "UPPER"
    LOWER = "LOWER"

class Day(IntEnum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()
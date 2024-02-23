from enum import StrEnum, auto

class Role(StrEnum):
    ADMIN = auto()
    MONITOR = auto()
    STUDENT = auto()

class Week(StrEnum):
    UPPER = auto()
    LOWER = auto()

class Day(StrEnum):
    MONDAY = auto()
    TUESDAY = auto()
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()
    SATURDAY = auto()
    SUNDAY = auto()
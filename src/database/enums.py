from enum import StrEnum, auto

class Role(StrEnum):
    ADMIN = auto()
    MONITOR = auto()
    STUDENT = auto()
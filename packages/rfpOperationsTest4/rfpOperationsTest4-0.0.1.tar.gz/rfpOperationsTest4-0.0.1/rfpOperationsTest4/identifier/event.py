from enum import Enum


class Event(Enum):
    UPDATED = "updated"
    NO_CHANGE = "no change"
    CREATED = "created"

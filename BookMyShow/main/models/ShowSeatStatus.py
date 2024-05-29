from enum import Enum


class ShowSeatStatus(Enum):
    BOOKED = "BOOKED"
    LOCKED = "LOCKED"
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"

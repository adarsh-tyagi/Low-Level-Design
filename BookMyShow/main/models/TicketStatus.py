from enum import Enum


class TicketStatus(Enum):
    CANCELLED = "CANCELLED"
    PENDING = "PENDING"
    PAYMENT_DONE = "PAYMENT_DONE"

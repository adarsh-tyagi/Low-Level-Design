from enum import Enum

class RequestType(Enum):
    PICKUP_UP = 1
    PICKUP_DOWN = 2
    DESTINATION = 3
    
class Request:
    def __init__(self, floor: int, type: RequestType):
        self.floor = floor
        self.type = type

    def get_floor(self) -> int:
        return self.floor

    def get_type(self) -> RequestType:
        return self.type
    
    def __eq__(self, other):
        if not isinstance(other, Request):
            return False
        return self.floor == other.floor and self.type == other.type

    def __hash__(self):
        return hash(self.floor, self.type)
    
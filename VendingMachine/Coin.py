from enum import Enum

class Coin(Enum):
    ONE = 1
    TWO = 2
    FIVE = 5
    TEN = 10
    TWENTY = 20
    FIFTY = 50
    HUNDRED = 100
    
    def get_value(self) -> int:
        return self.value
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def make_move(self, board):
        pass

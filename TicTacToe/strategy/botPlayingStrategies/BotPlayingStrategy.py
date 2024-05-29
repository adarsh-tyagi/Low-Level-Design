from abc import ABC, abstractmethod


class BotPlayingStrategy(ABC):
    @abstractmethod
    def make_move(self, board):
        pass

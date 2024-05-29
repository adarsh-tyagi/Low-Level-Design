from models.Player import Player
from strategy.botPlayingStrategies.BotPlayingStrategyFactory import BotPlayingStrategyFactory


class Bot(Player):
    def __init__(self, symbol, difficulty_level):
        super().__init__(symbol)
        self.difficulty_level = difficulty_level
        self.bot_playing_strategy = BotPlayingStrategyFactory.get_bot_playing_strategy(self.difficulty_level)

    def make_move(self, board):
        return self.bot_playing_strategy.make_move(board)

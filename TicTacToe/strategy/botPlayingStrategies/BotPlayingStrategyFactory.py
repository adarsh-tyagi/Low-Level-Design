from strategy.botPlayingStrategies.EasyBotPlayingStrategy import EasyBotPlayingStrategy
from strategy.botPlayingStrategies.MediumBotPlayingStrategy import MediumBotPlayingStrategy
from strategy.botPlayingStrategies.HardBotPlayingStrategy import HardBotPlayingStrategy
from models.BotDifficultyLevel import BotDifficultyLevel


class BotPlayingStrategyFactory:

    @staticmethod
    def get_bot_playing_strategy(bot_difficulty_level):
        if bot_difficulty_level == BotDifficultyLevel.EASY.name:
            return EasyBotPlayingStrategy()
        elif bot_difficulty_level == BotDifficultyLevel.MEDIUM.name:
            return MediumBotPlayingStrategy()
        elif bot_difficulty_level == BotDifficultyLevel.HARD.name:
            return HardBotPlayingStrategy()
        else:
            return EasyBotPlayingStrategy()

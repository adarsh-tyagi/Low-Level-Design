from strategy.botPlayingStrategies.BotPlayingStrategy import BotPlayingStrategy


class MediumBotPlayingStrategy(BotPlayingStrategy):
    def make_move(self, board):
        for row in board.board:
            for cell in row:
                if cell.symbol is None:
                    return cell
        return None

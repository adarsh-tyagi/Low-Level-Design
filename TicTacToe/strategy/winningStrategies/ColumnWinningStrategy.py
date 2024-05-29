from strategy.winningStrategies.WinningStrategy import WinningStrategy


class ColumnWinningStrategy(WinningStrategy):
    def __init__(self, size, players):
        self.colMaps = []
        for i in range(size):
            self.colMaps.append({})
            for player in players:
                self.colMaps[i][player.symbol] = 0

    def check_winner(self, board, cell):
        col = cell.column
        symbol = cell.symbol
        self.colMaps[col][symbol] += 1
        if self.colMaps[col][symbol] == board.size:
            return True
        return False

    def handle_undo(self, board, cell):
        col = cell.column
        symbol = cell.symbol
        self.colMaps[col][symbol] -= 1
        
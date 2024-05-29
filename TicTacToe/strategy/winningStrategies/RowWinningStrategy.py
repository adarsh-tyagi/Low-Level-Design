from strategy.winningStrategies.WinningStrategy import WinningStrategy


class RowWinningStrategy(WinningStrategy):
    def __init__(self, size, players):
        self.rowMaps = []
        for i in range(size):
            self.rowMaps.append({})
            for player in players:
                self.rowMaps[i][player.symbol] = 0

    def check_winner(self, board, cell):
        row = cell.row
        symbol = cell.symbol
        self.rowMaps[row][symbol] += 1
        if self.rowMaps[row][symbol] == board.size:
            return True
        return False

    def handle_undo(self, board, cell):
        row = cell.row
        symbol = cell.symbol
        self.rowMaps[row][symbol] -= 1

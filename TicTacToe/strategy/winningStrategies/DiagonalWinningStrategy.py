from strategy.winningStrategies.WinningStrategy import WinningStrategy


class DiagonalWinningStrategy(WinningStrategy):
    def __init__(self, players):
        self.leftDiagonalMap = {}
        self.rightDiagonalMap = {}
        for player in players:
            self.leftDiagonalMap[player.symbol] = 0
            self.rightDiagonalMap[player.symbol] = 0

    def check_winner(self, board, cell):
        row = cell.row
        col = cell.column
        symbol = cell.symbol
        if row == col:
            self.leftDiagonalMap[symbol] += 1
        if row + col == board.size - 1:
            self.rightDiagonalMap[symbol] += 1

        if row == col:
            if self.leftDiagonalMap[symbol] == board.size:
                return True
        if row + col == board.size - 1:
            if self.rightDiagonalMap[symbol] == board.size:
                return True
        return False

    def handle_undo(self, board, cell):
        row = cell.row
        col = cell.column
        symbol = cell.symbol
        if row == col:
            self.leftDiagonalMap[symbol] -= 1
        if row + col == board.size - 1:
            self.rightDiagonalMap[symbol] -= 1

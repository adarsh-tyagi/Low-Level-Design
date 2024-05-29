from models.Player import Player
from models.Cell import Cell


class Human(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def make_move(self, board):
        row = int(input(f"enter row (starting from 0): "))
        col = int(input(f"enter column (starting from 0): "))
        return Cell(row, col)

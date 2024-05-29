from models.Cell import Cell


class Board:
    def __init__(self, size):
        self.size = size
        self.board = []
        for r in range(self.size):
            row = []
            for c in range(self.size):
                row.append(Cell(r, c))
            self.board.append(row)

    def display(self):
        for row in self.board:
            for cell in row:
                cell.display()
            print()

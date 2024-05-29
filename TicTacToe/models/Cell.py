class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.symbol = None

    def display(self):
        if self.symbol:
            print(f" {self.symbol.char} |", end="")
        else:
            print(f" - |", end="")


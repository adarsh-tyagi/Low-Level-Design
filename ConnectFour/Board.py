from enum import Enum
from typing import Optional

class DiscColor(Enum):
    RED = "RED"
    YELLOW = "YELLOW"
    
class Board:
    def __init__(self, rows: int = 6, cols: int = 7):
        self.rows = rows
        self.cols = cols
        self.grid: list[list[Optional[DiscColor]]] = [
            [None for _ in range(cols)] for _ in range(rows)
        ]
    
    def get_rows(self) -> int:
        return self.rows

    def get_cols(self) -> int:
        return self.cols

    def can_place(self, column: int) -> bool:
        if column < 0 or column >= self.cols:
            return False
        return self.grid[0][column] is None # if first row of column is empty then there is space to place the disc
    
    def place_disc(self, column: int, color: DiscColor) -> int:
        if not self.can_place(column):
            return -1

        for row in range(self.rows-1, -1, -1):
            if self.grid[row][column] is None:
                self.grid[row][column] = color
                return row
        
        return -1
    
    def check_win(self, row: int, column: int, color: DiscColor) -> bool:
        if not self._in_bounds(row, column) or self.grid[row][column] != color:
            return False
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

        for dr, dc in directions:
            count = 1
            count += self._count_in_direction(row, column, dr, dc, color)
            count += self._count_in_direction(row, column, -dr, -dc, color)
            if count >= 4:
                return True
        return False
    
    def is_full(self) -> bool:
        return all(self.grid[0][c] is not None for c in range(self.cols))
    
    def get_cell(self, row: int, column: int) -> Optional[DiscColor]:
        if not self._in_bouds(row, column):
            return None
        return self.grid[row][column]

    def _count_in_directions(self, row: int, column: int, dr: int, dc: int, colir: DiscColor) -> int:
        count = 0
        r = row + dr
        c = column + dc
        while self._in_bounds(r, c) and self.grid[r][c] == color:
            count += 1
            r += dr
            c += dc
        return count
    
    def _in_bounds(self, row: int, column: int) -> bool:
        return 0 <= row < self.rows and 0 <= column < self.cols
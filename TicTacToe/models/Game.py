from models.Board import Board
from models.GameStatus import GameStatus


class Game:
    def __init__(self, builder):
        self.moves = []
        self.board = Board(builder.dimension)
        self.players = builder.players
        self.winning_strategies = builder.winning_strategies
        self.game_status = GameStatus.IN_PROGRESS.name
        self.winner = None
        self.currentMovePlayerIndex = 0

    def print_board(self):
        self.board.display()

    def print_result(self):
        if self.game_status == GameStatus.DRAW.name:
            print("Game is draw")
        elif self.game_status == GameStatus.FINISHED.name:
            print("Game Ended")
            print(f"Player {self.winner.symbol.char} won the game")

    def validate_move(self, cell):
        row = cell.row
        col = cell.column
        if row < 0 or col < 0 or row >= self.board.size or col >= self.board.size:
            return False
        if cell.symbol is not None:
            return False
        return True

    def undo(self):
        if len(self.moves) == 0:
            print("No moves to undo")
            return
        last_moved_cell = self.moves[-1]
        for winning_strategy in self.winning_strategies:
            winning_strategy.handle_undo(self.board, last_moved_cell)
        last_moved_cell.symbol = None
        self.moves.pop()
        self.currentMovePlayerIndex = (self.currentMovePlayerIndex - 1) % len(self.players)

    def check_draw(self):
        if len(self.moves) == self.board.size * self.board.size:
            self.game_status = GameStatus.DRAW.name
            return True
        return False

    def check_game_won(self, cell):
        for winning_strategy in self.winning_strategies:
            if winning_strategy.check_winner(self.board, cell):
                self.game_status = GameStatus.FINISHED.name
                self.winner = self.players[self.currentMovePlayerIndex]
                return True
        return False

    def make_move(self):
        current_player = self.players[self.currentMovePlayerIndex]
        print(f"Player {current_player.symbol.char}'s turn")
        current_cell = current_player.make_move(self.board)
        print(f"Move made at row: {current_cell.row}, column: {current_cell.column}")
        if not self.validate_move(current_cell):
            print("Invalid move")
            return
        cell_in_board = self.board.board[current_cell.row][current_cell.column]
        cell_in_board.symbol = current_player.symbol
        self.moves.append(cell_in_board)
        if self.check_game_won(cell_in_board):
            self.print_result()
            return
        if self.check_draw():
            self.print_result()
            return
        self.currentMovePlayerIndex = (self.currentMovePlayerIndex + 1) % len(self.players)

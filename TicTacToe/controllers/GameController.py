from models.Builder import Builder


class GameController:

    def create_game(self, dimension, players, winning_strategies):
        builder = Builder()
        return builder.set_dimension(dimension).set_players(players).set_winning_strategies(winning_strategies).build()

    def display_board(self, game):
        game.print_board()

    def undo_move(self, game):
        game.undo()

    def make_move(self, game):
        return game.make_move()

    def get_game_status(self, game):
        return game.game_status

    def print_result(self, game):
        game.print_result()

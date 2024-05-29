from controllers.GameController import GameController
from models.Human import Human
from models.Bot import Bot
from models.Symbol import Symbol
from models.BotDifficultyLevel import BotDifficultyLevel
from strategy.winningStrategies.RowWinningStrategy import RowWinningStrategy
from strategy.winningStrategies.ColumnWinningStrategy import ColumnWinningStrategy
from strategy.winningStrategies.DiagonalWinningStrategy import DiagonalWinningStrategy
from models.GameStatus import GameStatus


def choose_difficulty_level():
    inp = input("Choose difficulty level for Bot: (E/M/H))")
    if inp.lower() == "e":
        return BotDifficultyLevel.EASY.name
    elif inp.lower() == 'm':
        return BotDifficultyLevel.MEDIUM.name
    elif inp.lower() == 'h':
        return BotDifficultyLevel.HARD.name
    else:
        print("Invalid input. Choose again")
        choose_difficulty_level()


def create_players():
    inp = input("Do you want to play with Bot or Human? (B/H)")
    if inp.lower() in ('b', 'h'):
        first_player_symbol = input("Create your symbol first: ")
        first_player = Human(Symbol(first_player_symbol))
        if inp.lower() == "b":
            difficulty_level = choose_difficulty_level()
            second_player_symbol = input("Create Bot's symbol: ")
            second_player = Bot(Symbol(second_player_symbol), difficulty_level)
        elif inp.lower() == 'h':
            second_player_symbol = input("Create your friend's symbol: ")
            second_player = Human(Symbol(second_player_symbol))
        return [first_player, second_player]
    else:
        print("Invalid input. Choose again")
        create_players()


def main():
    game_controller = GameController()
    dimension = int(input("Enter the dimension of the board (for e.g. 3, 5, 7, etc): "))
    players = create_players()
    winning_strategies = []
    winning_strategies.extend([RowWinningStrategy(dimension, players), ColumnWinningStrategy(dimension, players),
                               DiagonalWinningStrategy(players)])
    try:
        game = game_controller.create_game(dimension, players, winning_strategies)
    except Exception as e:
        print(e)
        return

    print("***** Game Starting *****")
    while game_controller.get_game_status(game) == GameStatus.IN_PROGRESS.name:
        print("This is the current board looks like : ")
        game_controller.display_board(game)
        print("Does anyone want to do undo? (Y/N)")
        undo_input = input()
        if undo_input.lower() == 'y':
            game_controller.undo_move(game)
        else:
            game_controller.make_move(game)
    game_controller.display_board(game)


if __name__ == '__main__':
    main()

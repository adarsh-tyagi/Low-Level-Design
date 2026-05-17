from Game import Game, GameState
from Player import Player
from Board import DiscColor

player1 = Player("A", DiscColor.RED)
player2 = Player("B", DiscColor.YELLOW)

game = Game(player1, player2)

while game.get_game_state() == GameState.IN_PROGRESS:
    player = game.current_player
    print(f"It's {player}'s turn")
    column = input("select column (1-7): ")
    game.make_move(player, column)

print(f"Game result: {game.state.value}")
if game.winner:
    print(f"Winner is: {game.winner}")
    
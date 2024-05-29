from models.Game import Game


class Builder:
    def __init__(self):
        self.players = []
        self.winning_strategies = []
        self.dimension = None

    def set_players(self, players):
        self.players = players
        return self

    def set_winning_strategies(self, winning_strategies):
        self.winning_strategies = winning_strategies
        return self

    def set_dimension(self, dimension):
        self.dimension = dimension
        return self

    def valid(self):
        if len(self.players) < 2:
            return False
        if len(self.players) != self.dimension-1:
            return False

        existing_symbols = set()
        for player in self.players:
            if player.symbol in existing_symbols:
                return False
            existing_symbols.add(player.symbol)
        return True

    def build(self):
        if not self.valid():
            raise Exception("Invalid game configuration")
        return Game(self)
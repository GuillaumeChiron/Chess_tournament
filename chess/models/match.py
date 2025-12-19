from chess.models.player import Player


class Match:
    def __init__(self, name, player1: Player, player2: Player):
        self.name = name
        self.player1 = player1
        self.player2 = player2

    def to_dict(self):
        return {
            self.name: (
                [self.player1.name, self.player1.score],
                [self.player2.name, self.player2.score],
            )
        }

    @classmethod
    def from_dict(cls, dict):
        for cle, value in dict.items():

            return cls(
                name=cle,
                player1=Player(value[0][0], "", None, None, value[0][1]),
                player2=Player(value[1][0], "", None, None, value[1][1]),
            )

from chess.models.player import Player


class Match:
    def __init__(self, name, player1: Player, player2: Player, score1=0.0, score2=0.0):
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        return {
            self.name: (
                [self.player1.name, self.score1],
                [self.player2.name, self.score2],
            )
        }

    @classmethod
    def from_dict(cls, dict):
        for cle, value in dict.items():

            return cls(
                name=cle,
                player1=Player(value[0][0], "", None, None),
                player2=Player(value[1][0], "", None, None),
                score1=value[0][1],
                score2=value[1][1],
            )

from player import Player


class Match:
    def __init__(self, player1, score1, player2, score2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        return (
            [self.player1, self.score1],
            [self.player2, self.score2],
        )

    @staticmethod
    def from_dict(dict):
        return Match(
            player1=dict[0][0],
            player2=dict[1][0],
            score1=dict[0][1],
            score2=dict[1][1],
        )

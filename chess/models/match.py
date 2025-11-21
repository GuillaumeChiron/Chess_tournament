class Match:
    def __init__(self, player1, player2, score1, score2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def serialize_to_tuple(self):
        return ([self.player1, self.score1], [self.player2, self.score2])

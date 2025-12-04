class Match:
    def __init__(self, name, player1, player2, score1, score2):
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        return {
            "Match": self.name,
            "Joueur_1": self.player1,
            "Joueur_2": self.player2,
            "Score_1": self.score1,
            "Score_2": self.score2,
        }

    @staticmethod
    def from_dict(dict):
        return Match(
            name=dict["match"],
            player1=dict["Joueur_1"],
            player2=dict["Joueur_2"],
            score1=dict["Score_1"],
            score2=dict["Score_2"],
        )

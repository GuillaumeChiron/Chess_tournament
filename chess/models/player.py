class Player:
    def __init__(
        self, name, last_name, player_id, birth_date, score=0, player_against=[]
    ):
        self.name = name
        self.last_name = last_name
        self.player_id = player_id
        self.score = score
        self.birth_date = birth_date
        self.player_against = player_against

    def to_dict(self):
        return {
            "Prenom": self.name,
            "Nom": self.last_name,
            "Identifiant": self.player_id,
            "Date_de_naissance": self.birth_date,
            "Score": self.score,
            "Adversaires": self.player_against,
        }

    @classmethod
    def from_dict(cls, dict):
        return cls(
            name=dict["Prenom"],
            last_name=dict["Nom"],
            player_id=dict["Identifiant"],
            birth_date=dict["Date_de_naissance"],
            score=dict["Score"],
            player_against=dict["Adversaires"],
        )

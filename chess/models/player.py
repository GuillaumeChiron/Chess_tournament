class Player:
    def __init__(self, name, last_name, player_id, birth_date):
        self.name = name
        self.last_name = last_name
        self.player_id = player_id
        self.birth_date = birth_date

    def to_dict(self):
        return {
            "Prenom": self.name,
            "Nom": self.last_name,
            "Identifiant": self.player_id,
            "Date_de_naissance": self.birth_date,
        }

    @classmethod
    def from_dict(cls, dict):
        return cls(
            name=dict["Prenom"],
            last_name=dict["Nom"],
            player_id=dict["Identifiant"],
            birth_date=dict["Date_de_naissance"],
        )

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
            "Date de naissance": self.birth_date,
        }

    @staticmethod
    def from_dict(dict):
        return Player(
            name=dict["Prenom"],
            last_name=dict["Nom"],
            player_id=dict["Identifiant"],
            birth_date=dict["Date de naissance"],
        )

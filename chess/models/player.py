class Player:
    def __init__(self, name, last_name, chess_id, birth_date):
        self.name = name
        self.last_name = last_name
        self.ches_id = chess_id
        self.birth_date = birth_date

    def serialize_to_dict(self):
        return {
            "Prenom": self.name,
            "Nom": self.last_name,
            "Identifiant": self.ches_id,
            "Date de naissance": self.birth_date,
        }

    def deserialize_to_dict():
        pass

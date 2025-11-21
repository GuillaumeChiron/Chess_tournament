class Player:
    def __init__(self, name, last_name, chess_id, birth_date, score):
        self.name = name
        self.last_name = last_name
        self.ches_id = chess_id
        self.birth_date = birth_date
        self.score = score

    def serialize_to_dict(self):
        return {
            "Prenom": self.name,
            "Nom": self.last_name,
            "Identifiant": self.ches_id,
            "Anniversaire": self.birth_date,
            "Score": self.score,
        }

    def deserialize_to_dict():
        pass

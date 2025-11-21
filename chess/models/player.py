class Player:
    def __init__(self, name, last_name, birth_date, score):
        self.name = name
        self.last_name = last_name
        self.birth_date = birth_date
        self.score = score

    def transform_to_dict(self):
        return {
            "Prenom": self.name,
            "Nom": self.last_name,
            "Anniversaire": self.birth_date,
            "Score": self.score,
        }

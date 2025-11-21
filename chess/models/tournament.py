class Tournament:
    def __init__(
        self, name, location, start_date, end_date, rounds, total_rounds, players
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.total_rounds = total_rounds
        self.players = players

    def generate_round(self):
        pass

    def transform_to_dict(self):
        return {
            "Nom": self.name,
            "Lieu": self.location,
            "Date de début": self.start_date,
            "Date de fin": self.end_date,
            "Rounds": self.rounds,
            "Nombre de rounds": self.total_rounds,
            "Joueurs": self.players,
        }

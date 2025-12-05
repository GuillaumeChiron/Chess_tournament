from datetime import datetime


class Tournament:
    def __init__(
        self,
        name,
        location,
        players,
        description,
        total_rounds=4,
        round=1,
    ):
        self.name = name
        self.location = location
        self.start_date = None
        self.end_date = None
        self.round = round
        self.total_rounds = total_rounds
        self.players = players
        self.description = description

    def start_tournament(self):
        self.start_date = datetime.now().isoformat()
        return self.start_date

    def end_tournament(self):
        self.end_date = datetime.now().isoformat()

    def generate_rounds(self):
        pass

    def to_dict(self):
        return {
            "Nom": self.name,
            "Lieu": self.location,
            "Date de debut": self.start_date,
            "Date de fin": self.end_date,
            "Round actuel": self.round,
            "Nombre de rounds": self.total_rounds,
            "Joueurs": self.players,
            "Description": self.description,
        }

    @staticmethod
    def from_dict(dict):
        return Tournament(
            name=dict["Nom"],
            location=dict["Lieu"],
            start_date=dict["Date de debut"],
            end_date=dict["Date de fin"],
            rounds=dict["Round actuel"],
            total_rounds=dict["nombre de rounds"],
            players=dict["Joueurs"],
            description=dict["Description"],
        )

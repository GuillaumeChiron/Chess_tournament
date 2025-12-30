from datetime import datetime


class Tournament:
    def __init__(
        self,
        name,
        location,
        players,
        description,
        total_rounds=4,
        rounds=[],
        current_round_index=1,
    ):
        self.name = name
        self.location = location
        self.players = players
        self.rounds = rounds
        self.description = description
        self.current_round_index = current_round_index
        self.total_rounds = total_rounds
        self.start_date = ""
        self.end_date = ""

    def start_tournament(self):
        heure = datetime.now()
        self.start_date = heure.strftime("%d/%m/%Y")
        return self.start_date

    def end_tournament(self):
        heure = datetime.now()
        self.end_date = heure.strftime("%d/%m/%Y")

    def to_dict(self):
        return {
            "Nom": self.name,
            "Lieu": self.location,
            "Date de debut": self.start_date,
            "Date de fin": self.end_date,
            "Joueurs": self.players,
            "Description": self.description,
            "Rounds": self.rounds,
            "Round actuel": self.current_round_index,
            "Nombre de rounds": self.total_rounds,
        }

    @classmethod
    def from_dict(cls, dict):
        tournoi = cls(
            name=dict["Nom"],
            location=dict["Lieu"],
            rounds=dict["Rounds"],
            current_round_index=dict["Round actuel"],
            total_rounds=dict["Nombre de rounds"],
            players=dict["Joueurs"],
            description=dict["Description"],
        )
        tournoi.start_date = dict["Date de debut"]
        tournoi.end_date = dict["Date de fin"]

        return tournoi

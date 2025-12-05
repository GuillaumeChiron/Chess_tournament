from datetime import datetime
from chess.models.match import Match


class Round:
    def __init__(self, name, matches=[]):
        self.name = name
        self.matches = matches
        self.start_time = None
        self.end_time = None

    def start_round(self):
        self.start_time = datetime.now().isoformat()
        return self.start_time

    def end_round(self):
        self.end_time = datetime.now().isoformat()
        return self.end_time

    def generate_round(self):
        return self.matches

    def to_dict(self):
        return {
            "Nom": self.name,
            "Matches": self.matches,
            "Heure de début": self.start_time,
            "Heure de fin": self.end_time,
        }

    @staticmethod
    def from_dict(dict):
        return Round(
            name=dict["Nom"],
            matches=dict["Matches"],
            start_time=dict["Heure de début"],
            end_time=dict["Heure de fin"],
        )

from datetime import datetime


class Round:
    def __init__(self, name, matches=[]):
        self.name = name
        self.matches = matches
        self.start_time = ""
        self.end_time = ""

    # debut d'un round
    def start_round(self):
        heure = datetime.now()
        self.start_time = heure.strftime("%H:%M")
        return self.start_time

    # fin d'un round
    def end_round(self):
        heure = datetime.now()
        self.end_time = heure.strftime("%H:%M")
        return self.end_time

    def to_dict(self):
        # retourne les données d'un round sous la forme d'un dictionnaire
        return {
            "Nom": self.name,
            "Matches": self.matches,
            "Heure de debut": self.start_time,
            "Heure de fin": self.end_time,
        }

    @classmethod
    def from_dict(cls, dict):
        # permet de récréer un objet round
        round = cls(name=dict["Nom"], matches=dict["Matches"])
        round.start_time = dict["Heure de debut"]
        round.end_time = dict["Heure de fin"]
        return round

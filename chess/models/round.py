import tournament


class Round(tournament.Tournament):
    def __init__(self, name, matches, start_datetime, end_datetime):
        self.name = name
        self.matches = matches
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def start_round(self):
        pass

    def end_round(self):
        pass

    def transform_to_dict(self):
        return {
            "Nom": self.name,
            "Matches": self.matches,
            "Heure-début": self.start_datetime,
            "Heure-fin": self.end_datetime,
        }

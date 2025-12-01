class Round:
    def __init__(self, name, matches, start_time, end_time):
        self.name = name
        self.matches = matches
        self.start_time = start_time
        self.end_time = end_time

    def start_round(self):
        pass

    def end_round(self):
        pass

    def serialize_to_dict(self):
        return {
            "Nom": self.name,
            "Matches": self.matches,
            "Heure de début": self.start_time,
            "Heure de fin": self.end_time,
        }

    @staticmethod
    def deserialize_from_dict(dict):
        return Round(
            name=dict["Nom"],
            matches=dict["Matches"],
            start_time=dict["Heure de début"],
            end_time=dict["Heure de fin"],
        )

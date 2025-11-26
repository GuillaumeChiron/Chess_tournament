class Tournament:
    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        rounds,
        players,
        description,
        total_rounds="4",
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.total_rounds = total_rounds
        self.players = players
        self.description = description

    def generate_round(self):
        pass

    def serialize_to_dict(self):
        return {
            "Nom": self.name,
            "Lieu": self.location,
            "Date de début": self.start_date,
            "Date de fin": self.end_date,
            "Rounds": self.rounds,
            "Nombre de rounds": self.total_rounds,
            "Joueurs": self.players,
            "Description": self.description,
        }

    @classmethod
    def deserialize_to_dict(cls, dict):
        return cls(
            name=dict["Nom"],
            location=dict["Lieu"],
            start_date=dict["Date de début"],
            end_date=dict["Date de fin"],
            rounds=dict["Rounds"],
            total_rounds=dict["nombre de rounds"],
            players=dict["Joueurs"],
            description=dict["Description"],
        )

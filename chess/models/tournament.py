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

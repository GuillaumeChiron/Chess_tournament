from rich.console import Console
from tinydb import TinyDB, Query
from chess.models.match import Match


# initialise la mise en forme
rich = Console()
# initialise la base de données et les recherches dans la base de données
tournaments_db = TinyDB("chess/data/tournaments.json")
players_db = TinyDB("chess/data/players.json")
qr = Query()


class Match_controllers:

    # retourne le nouveau score
    @staticmethod
    def update_match_scores(data):
        new_score = data.to_dict()
        return new_score

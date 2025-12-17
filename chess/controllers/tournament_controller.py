from rich.console import Console
from rich.table import Table
from tinydb import TinyDB, Query
from chess.models.tournament import Tournament

rich = Console()
tournaments_db = TinyDB("chess/data/tournaments.json")
qr = Query()


class Tournament_controller:

    # ajoute un tournoi dans la base de données
    @staticmethod
    def create_tournament(name, location, players, desciption):
        tournament = Tournament(
            name,
            location,
            players,
            desciption,
        )
        return tournament

    # enregistre un tournoi dans la base de données "tournaments.json"
    @staticmethod
    def save_tournament(tournament):
        tournament_data = tournament.to_dict()
        if not tournaments_db.search(qr.Nom == tournament.name):
            tournaments_db.insert(tournament_data)

    # met à jour un tournoi
    @staticmethod
    def update_tournament(name_tournament, data):
        tournaments_db.update(data, qr.Nom == name_tournament)

    # recupère les données du fichier "tournaments.json"
    @staticmethod
    def load_tournaments():
        all_tournaments = tournaments_db.all()
        return all_tournaments

    # recupère un tournoi dans la base de données "tournaments.json"
    @staticmethod
    def get_tournament(data):
        result = tournaments_db.search(qr.Nom.test(lambda v: v.lower() == data.lower()))
        return result

    # execute un round
    @staticmethod
    def launch_round():
        pass

    # execute un tournoi
    @staticmethod
    def run_tournament():
        pass

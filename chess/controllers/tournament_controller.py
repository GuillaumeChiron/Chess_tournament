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
    def update_tournament(tournoi):
        data = tournoi.to_dict()
        tournaments_db.update(data, qr.Nom == tournoi.name)

    # recupère les données du fichier "tournaments.json"
    @staticmethod
    def load_tournaments():
        all_tournaments = tournaments_db.all()
        return all_tournaments

    # recupère un tournoi dans la base de données "tournaments.json"
    @staticmethod
    def get_tournament(data):
        result = tournaments_db.search(qr.Nom.test(lambda v: v.lower() == data.lower()))
        tournoi = Tournament.from_dict(result[0])
        return tournoi

    # execute un round du tournoi
    @staticmethod
    def launch_round(tournoi):
        from chess.controllers.round_controller import Round_controllers
        from chess.controllers.player_controller import Player_controllers
        from chess.models.round import Round

        round = Round.from_dict(tournoi.rounds[tournoi.current_round_index - 1])
        round.start_round()
        round_update = Round_controllers.update_round(round)
        round_update.end_round()
        tournoi.rounds[tournoi.current_round_index - 1] = round_update.to_dict()
        tournoi.current_round_index += 1
        tournoi = Player_controllers.update_score_players(tournoi)
        return tournoi

    # execute un tournoi
    @staticmethod
    def run_tournament(tournoi):

        round = Tournament_controller.launch_round(tournoi.players)
        round_data = round.to_dict()
        tournoi.rounds.append(round_data)
        return tournoi

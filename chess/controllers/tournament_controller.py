from tinydb import Query, TinyDB
from chess.models.tournament import Tournament

# initialise la base de données et les recherches dans la base de données
tournaments_db = TinyDB("chess/data/tournaments.json")
qr = Query()


class Tournament_controller:

    # Créer un tournoi
    @staticmethod
    def create_tournament(name, location, players, description, rounds=4):
        tournament = Tournament(
            name,
            location,
            players,
            description,
            rounds,
        )
        return tournament

    # enregistre un tournoi dans la base de données "tournaments.json"
    @staticmethod
    def save_tournament(tournament):
        tournament_data = tournament.to_dict()
        if not tournaments_db.search(qr.Nom == tournament.name):
            tournaments_db.insert(tournament_data)

    # met à jour un tournoi de la base de données
    @staticmethod
    def update_tournament(tournoi):
        data = tournoi.to_dict()
        tournaments_db.update(data, qr.Nom == tournoi.name)

    # recupère les données des tournois du fichier "tournaments.json"
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

        tournoi = Round_controllers.update_round(tournoi)
        tournoi.players = Player_controllers.sorted_players(tournoi)
        tournoi.current_round_index += 1

        return tournoi

    # execute un tournoi
    @staticmethod
    def run_tournament(name_tournoi: str) -> Tournament:
        from chess.controllers.round_controller import Round_controllers

        tournoi = Tournament_controller.get_tournament(name_tournoi)
        tournoi = Round_controllers.generate_first_round(tournoi)
        tournoi = Tournament_controller.launch_round(tournoi)

        while tournoi.current_round_index <= tournoi.total_rounds:

            pairing = Round_controllers.generate_swiss_pairings(tournoi)
            tournoi = Round_controllers.generate_next_round(tournoi, pairing)
            tournoi = Tournament_controller.launch_round(tournoi)
            # Tournament_controller.update_tournament(tournoi)
        return tournoi

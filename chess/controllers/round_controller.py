from rich.console import Console
from tinydb import TinyDB, Query
import random
from chess.controllers.match_controller import Match_controllers


rich = Console()
tournaments_db = TinyDB("chess/data/tournaments.json")
qr = Query()


class Round_controllers:

    # genère une paire de joueurs aléatoire dans une liste de joueurs donnée
    @staticmethod
    def generate_pairings(data):
        tirage = random.sample(data, 2)
        joueurs = []
        for info in tirage:
            joueurs.append(info)
        return joueurs

    # enregistre un round dans la base de données "tournaments.json"
    @staticmethod
    def save_round(name_tournament, matches):
        tournaments_db.update({"Rounds": [matches]}, qr.Nom == name_tournament)

    # met à jour les scores des joueurs pour un round précis
    @staticmethod
    def update_round(round):
        from chess.views.match_view import ask_scores

        liste_new_score = []
        for data in round.matches:
            new_scores = ask_scores(data)
            new_match = Match_controllers.update_match_scores(new_scores)
            liste_new_score.append(new_match)
        round.matches = liste_new_score
        return round

    # genère le premier round dun tournoi
    @staticmethod
    def generate_first_round(players):
        from chess.models.player import Player
        from chess.models.match import Match
        from chess.models.round import Round

        players = players.copy()
        round1 = Round("Round 1")
        count = 1
        for i in range(int(len(players) / 2)):

            name = "Match" + str(count)
            count += 1

            tirage = Round_controllers.generate_pairings(players)
            for data_player in tirage:
                players.remove(data_player)

            player1 = Player.from_dict(tirage[0])
            player2 = Player.from_dict(tirage[1])

            match1 = Match(name, player1, player2)
            match_data = match1.to_dict()
            round1.matches.append(match_data)
        return round1

    # genère le round suivant
    @staticmethod
    def generate_next_round():
        pass

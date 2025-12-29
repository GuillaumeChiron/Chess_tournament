import random

from rich.console import Console
from tinydb import Query, TinyDB

from chess.controllers.match_controller import Match_controllers
from chess.models.tournament import Tournament

rich = Console()
tournaments_db = TinyDB("chess/data/tournaments.json")
qr = Query()


class Round_controllers:

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

    # genère une paire de joueurs aléatoire dans une liste de joueurs donnée
    @staticmethod
    def generate_pairings(data):
        tirage = random.sample(data, 2)
        joueurs = []
        for info in tirage:
            joueurs.append(info)
        return joueurs

    # genère le premier round dun tournoi
    @staticmethod
    def generate_first_round(tournoi: Tournament):
        from chess.models.match import Match
        from chess.models.player import Player
        from chess.models.round import Round

        players_copy = tournoi.players.copy()
        list_of_players = []
        for p in players_copy:
            list_of_players.append(p)

        round1 = Round("Round 1")
        count = 1
        for i in range(int(len(list_of_players) / 2)):

            name = "Match" + str(count)
            count += 1

            tirage = Round_controllers.generate_pairings(list_of_players)
            for data_player in tirage:
                list_of_players.remove(data_player)

            player1 = Player.from_dict(tirage[0])
            player2 = Player.from_dict(tirage[1])

            for p in tournoi.players:
                if p["Identifiant"] == player1.player_id:
                    p["Adversaires"].append(player2.player_id)
                if p["Identifiant"] == player2.player_id:
                    p["Adversaires"].append(player1.player_id)

            # next(p for p in tournoi.players if p["player"] == player)["play_against"].append(opponent)
            match1 = Match(name, player1, player2)
            match_data = match1.to_dict()
            round1.matches.append(match_data)

        tournoi.rounds.append(round1.to_dict())
        return tournoi

    # genère le round suivant
    @staticmethod
    def generate_swiss_pairings(tournoi: Tournament):
        from chess.models.player import Player

        pairings = []
        used_ids = set()

        players_copy = tournoi.players.copy()
        list_of_players = []
        for p in players_copy:
            object_player = Player.from_dict(p)
            list_of_players.append(object_player)

        # Tri par score décroissant
        list_of_players = sorted(list_of_players, key=lambda p: p.score, reverse=True)

        for i, player in enumerate(list_of_players):

            if player.player_id in used_ids:
                continue

            for opponent in list_of_players[i + 1 :]:
                if opponent.player_id in used_ids:
                    continue

                player_entry = next(
                    (
                        p
                        for p in tournoi.players
                        if p["Identifiant"] == player.player_id
                    ),
                    None,
                )

                if opponent.player_id not in player_entry["Identifiant"]:
                    used_ids.add(player.player_id)
                    used_ids.add(opponent.player_id)

                    pairings.append(
                        {
                            "player_1": f"{player.name} {player.last_name}",
                            "player_2": f"{opponent.name} {opponent.last_name}",
                            "ids": (player.player_id, opponent.player_id),
                            "Score": (player.score, opponent.score),
                        }
                    )
                    break

            else:
                raise Exception(
                    f"Aucun adversaire valide pour {player.name} {player.last_name}"
                )
        return pairings

    def generate_next_round(tournoi, pairings):
        from chess.controllers.player_controller import Player_controllers
        from chess.models.match import Match
        from chess.models.player import Player
        from chess.models.round import Round

        name_round = f"Round {str(tournoi.current_round_index)}"
        current_round = Round(name_round, [])
        count = 1

        for i in pairings:

            name_match = "match" + str(count)
            count += 1
            player1 = Player_controllers.get_player(i["ids"][0])
            player2 = Player_controllers.get_player(i["ids"][1])

            player1 = Player.from_dict(player1[0])
            player2 = Player.from_dict(player2[0])

            for p in tournoi.players:
                if p["Identifiant"] == player1.player_id:
                    p["Adversaires"].append(player2.player_id)
                if p["Identifiant"] == player2.player_id:
                    p["Adversaires"].append(player1.player_id)

            player1.score = i["Score"][0]
            player2.score = i["Score"][1]

            match = Match(name_match, player1, player2)
            current_round.matches.append(match.to_dict())
        tournoi.rounds.append(current_round.to_dict())
        return tournoi

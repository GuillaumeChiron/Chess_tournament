import random

from tinydb import Query, TinyDB

from chess.models.tournament import Tournament

# initialise la base de données et les recherches dans la base de données
tournaments_db = TinyDB("chess/data/tournaments.json")
qr = Query()


class Round_controllers:

    # enregistre un round dans la base de données "tournaments.json"
    @staticmethod
    def save_round(name_tournament: str, matches: dict):
        tournaments_db.update({"Rounds": [matches]}, qr.Nom == name_tournament)

    # met à jour les scores des joueurs pour un round précis
    @staticmethod
    def update_round(tournoi: Tournament) -> Tournament:
        from chess.models.round import Round
        from chess.views.match_view import Match_views

        # recréer un round et met à jour les nouveaux score des matchs
        round = Round.from_dict(tournoi.rounds[tournoi.current_round_index - 1])
        round.start_round()
        liste_new_score = []
        for data in round.matches:
            new_scores = Match_views.ask_scores(data)
            for p in tournoi.players:
                if p["Prenom"] == new_scores.player1.name:
                    p["Score"] = new_scores.player1.score
                if p["Prenom"] == new_scores.player2.name:
                    p["Score"] = new_scores.player2.score

            liste_new_score.append(new_scores.to_dict())
        round.matches = liste_new_score
        tournoi.rounds[tournoi.current_round_index - 1] = round.to_dict()
        return tournoi

    # genère une paire de joueurs aléatoire dans une liste de joueurs donnée
    @staticmethod
    def generate_pairings(data: list) -> list:
        tirage = random.sample(data, 2)
        joueurs = []
        for info in tirage:
            joueurs.append(info)
        return joueurs

    # genère le premier round d'un tournoi
    @staticmethod
    def generate_first_round(tournoi: Tournament) -> Tournament:
        from chess.models.match import Match
        from chess.models.player import Player
        from chess.models.round import Round

        players_copy = tournoi.players.copy()
        list_of_players = []
        for p in players_copy:
            list_of_players.append(p)

        # création du round
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

            # ajoute et stock les adversaires des joueurs dans une liste
            for p in tournoi.players:
                if p["Identifiant"] == player1.player_id:
                    p["Adversaires"].append(player2.player_id)
                if p["Identifiant"] == player2.player_id:
                    p["Adversaires"].append(player1.player_id)

            # recréer le match et l'ajoute au round
            match1 = Match(name, player1, player2)
            match_data = match1.to_dict()
            round1.matches.append(match_data)

        tournoi.rounds.append(round1.to_dict())
        return tournoi

    # genère le pairings pour le round suivant en suivant le format des rounds suisses
    @staticmethod
    def generate_swiss_pairings(tournoi: Tournament) -> list:
        from chess.models.player import Player

        players = [Player.from_dict(p) for p in tournoi.players]
        players.sort(key=lambda p: p.score, reverse=True)

        used = set()
        result = []

        def backtrack():
            if len(used) == len(players):
                return True

            # Premier joueur libre
            player = next(p for p in players if p.player_id not in used)

            player_entry = next(
                p for p in tournoi.players if p["Identifiant"] == player.player_id
            )

            for opponent in players:
                if opponent.player_id in used:
                    continue
                if opponent.player_id == player.player_id:
                    continue
                if opponent.player_id in player_entry["Adversaires"]:
                    continue

                # Essai
                used.add(player.player_id)
                used.add(opponent.player_id)
                result.append((player, opponent))

                if backtrack():
                    return True

                # Annulation
                used.remove(player.player_id)
                used.remove(opponent.player_id)
                result.pop()

            return False

        backtrack()

        # Mise en forme et mise à jour adversaires
        pairings = []
        for p1, p2 in result:
            pairings.append(
                {
                    "player_1": f"{p1.name} {p1.last_name}",
                    "player_2": f"{p2.name} {p2.last_name}",
                    "ids": (p1.player_id, p2.player_id),
                    "Score": (p1.score, p2.score),
                }
            )

            for p in tournoi.players:
                if p["Identifiant"] == p1.player_id:
                    p["Adversaires"].append(p2.player_id)
                if p["Identifiant"] == p2.player_id:
                    p["Adversaires"].append(p1.player_id)

        return pairings

    # genère le round suivant
    def generate_next_round(tournoi: Tournament, pairings: list) -> Tournament:
        from chess.models.match import Match
        from chess.models.player import Player
        from chess.models.round import Round

        name_round = f"Round {str(tournoi.current_round_index)}"
        current_round = Round(name_round, [])
        count = 1

        # permet de recréer les joueurs et les matchs pour les stocker dans le round
        for i in pairings:

            name_match = "match" + str(count)
            count += 1
            for p in tournoi.players:
                if p["Identifiant"] == i["ids"][0]:
                    player1 = p
                if p["Identifiant"] == i["ids"][1]:
                    player2 = p

            # recréer les joueurs
            player1 = Player.from_dict(player1)
            player2 = Player.from_dict(player2)

            player1.score = i["Score"][0]
            player2.score = i["Score"][1]

            # recréer le match
            match = Match(name_match, player1, player2)
            current_round.matches.append(match.to_dict())
        tournoi.rounds.append(current_round.to_dict())

        return tournoi

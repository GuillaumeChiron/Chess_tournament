from rich.table import Table
from tinydb import Query, TinyDB

# initialise la base de données et les recherches dans la base de données
tournaments_db = TinyDB("chess/data/tournaments.json")
players_db = TinyDB("chess/data/players.json")
qr = Query()


class Reports_controller:

    # Affiche un joueur de la base de données dans un tableau
    @staticmethod
    def player(data: str) -> Table:
        # cherche le joueur dans la base de donnée
        result = players_db.search(qr.Prenom.test(lambda v: v.lower() == data.lower()))

        if not result:
            return None

        # création du tableau

        table_player = Table(title="Joueur", style="blue", header_style="blue bold")
        # recupère les données et les ajoute dans les colonnes et les lignes
        list_of_keys = []
        for cle in result[0].keys():
            list_of_keys.append(cle)

        titles = list_of_keys[0:4]
        for title in titles:
            table_player.add_column(title, justify="center")
        for info in result:
            table_player.add_row(
                info["Prenom"],
                info["Nom"],
                info["Identifiant"],
                info["Date_de_naissance"],
            )
        return table_player

    # Affiche tous les joueurs de la base de données dans un tableau
    @staticmethod
    def list_players() -> Table:
        # Stock les données de players.json dans "all_users"
        all_users = players_db.all()
        all_users = sorted(all_users, key=lambda x: x["Nom"].lower())

        # Création du tableau
        table_players = Table(
            title="Liste des Joueurs",
            row_styles=["none", "blue"],
            header_style="blue bold",
            style="blue",
        )
        # recupère les données et les ajoute dans les colonnes et les lignes
        list_of_keys = []
        for cle in all_users[0].keys():
            list_of_keys.append(cle)
        titles = list_of_keys[0:4]
        for title in titles:
            table_players.add_column(title, justify="center")
        for info in all_users:
            table_players.add_row(
                info["Prenom"],
                info["Nom"],
                info["Identifiant"],
                info["Date_de_naissance"],
            )
        return table_players

    # Affiche un tournoi de la base de données dans un tableau
    @staticmethod
    def tournament(tournoi: str) -> Table:
        result = tournaments_db.search(
            qr.Nom.test(lambda v: v.lower() == tournoi.lower())
        )

        # création du tableau
        table_tournament = Table(
            title="Tournoi", style="blue", header_style="blue bold"
        )
        # recupere les données et les ajoute dans les colonnes et les lignes
        list_of_keys = []
        for cle in result[0].keys():
            list_of_keys.append(cle)
        for i in (0, 2, 3):
            table_tournament.add_column(list_of_keys[i], justify="center")

        for info in result:
            table_tournament.add_row(
                info["Nom"], info["Date de debut"], info["Date de fin"]
            )

        return table_tournament

    # Affiche tous les tournois de la base de données dans un tableau
    @staticmethod
    def list_tournaments() -> Table:
        # stock les données de tournaments.json dans "all_tournaments"
        all_tournaments = tournaments_db.all()

        # création du tableau
        table_tournaments = Table(
            title="Liste des Tournois",
            row_styles=["none", "blue"],
            header_style="blue bold",
            style="blue",
        )
        # recupere les données et les ajoute dans les colonnes et les lignes
        list_of_keys = []
        for cle in all_tournaments[0].keys():
            list_of_keys.append(cle)

        titles = list_of_keys[0:2]
        titles.append("Rounds")
        for title in titles:
            table_tournaments.add_column(title, justify="center")

        for info in all_tournaments:
            table_tournaments.add_row(
                info["Nom"], info["Lieu"], str(info["Nombre de rounds"])
            )

        return table_tournaments

    # Affiche tous les joueurs d'un tournoi dans un tableau
    @staticmethod
    def tournament_list_players(tournoi: str) -> Table:
        result = tournaments_db.search(
            qr.Nom.test(lambda v: v.lower() == tournoi.lower())
        )

        # création du tableau
        table_tournament = Table(
            title=tournoi,
            style="blue",
            row_styles=["none", "blue"],
            header_style="blue bold",
        )
        # recupère les la liste des joueurs et les tries par ordre alphabétique
        players = result[0]["Joueurs"]
        players = sorted(players, key=lambda x: x["Nom"].lower())

        # recupère les données et les ajoute dans les colonnes et les lignes
        list_of_keys = []
        for cle in players[0].keys():
            list_of_keys.append(cle)

        titles = list_of_keys[0:5]
        for title in titles:
            table_tournament.add_column(title, justify="center")
        for info in players:
            table_tournament.add_row(
                info["Prenom"],
                info["Nom"],
                info["Identifiant"],
                info["Date_de_naissance"],
                str(info["Score"]),
            )

        return table_tournament

    # Affiche les rounds avec les matchs les concernants d'un tournoi dans un tableau
    @staticmethod
    def tournament_list_rounds(tournoi: str) -> Table:
        from chess.models.match import Match
        from chess.models.round import Round

        result = tournaments_db.search(
            qr.Nom.test(lambda v: v.lower() == tournoi.lower())
        )

        # création du tableau
        table_tournament = Table(
            title=tournoi,
            style="blue",
            row_styles=["none", "blue"],
            header_style="blue bold",
        )
        # création des colonnes
        table_tournament.add_column("Round", justify="center")
        table_tournament.add_column("matchs", justify="center")

        # recupere les données et les ajoute dans les lignes
        rounds_data = result[0]["Rounds"]
        for r in rounds_data:
            round = Round.from_dict(r)

            matches = []
            for m in round.matches:
                match = Match.from_dict(m)
                matches.append(
                    f"({match.name}: {match.player1.name} {str(match.player1.score)} / "
                    f"{match.player2.name} {str(match.player2.score)} -> {round.end_time})"
                )
            matches_str = " - ".join(matches)
            table_tournament.add_row(round.name, matches_str)

        return table_tournament

from tinydb import TinyDB, Query
from rich.table import Table

tournaments_db = TinyDB("chess/data/tournaments.json")
players_db = TinyDB("chess/data/players.json")
qr = Query()


class Reports_controller:

    # Retourne un joueur de la base de données dans un tableau
    @staticmethod
    def player(data):
        # cherche le joueur dans la base de donnée
        result = players_db.search(qr.Prenom.test(lambda v: v.lower() == data.lower()))

        if not result:
            return None

        # création du tableau
        for info in result:
            table_player = Table(
                title=result[0]["Prenom"], style="blue", header_style="blue bold"
            )
            for cle in info.keys():
                table_player.add_column(cle)
            table_player.add_row(*[str(value) for value in info.values()])
        return table_player

    # Retourne tous les joueurs de la base de données dans un tableau
    @staticmethod
    def list_players():
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
        for cle in all_users[0].keys():
            table_players.add_column(cle)
        for info in all_users:
            table_players.add_row(*(str(value) for value in info.values()))
        return table_players

    # affiche un tournoi de la base de données dans un tableau
    @staticmethod
    def tournament(tournoi):
        result = tournaments_db.search(
            qr.Nom.test(lambda v: v.lower() == tournoi.lower())
        )

        # création du tableau
        table_tournament = Table(
            title=result[0]["Nom"], style="blue", header_style="blue bold"
        )
        for info in result:
            for cle in info.keys():
                table_tournament.add_column(cle)
            table_tournament.add_row(*[str(value) for value in info.values()])
        return table_tournament

    # affiche tous les tournois de la base de données dans un tableau
    @staticmethod
    def list_tournaments():
        # stock les données de tournaments.json dans "all_tournaments"
        all_tournaments = tournaments_db.all()

        # création du tableau
        table_tournaments = Table(
            title="Liste des Tournois",
            row_styles=["none", "blue"],
            header_style="blue bold",
            style="blue",
        )

        for cle in all_tournaments[0].keys():
            table_tournaments.add_column(cle)
        for info in all_tournaments:
            table_tournaments.add_row(*(str(value) for value in info.values()))

        return table_tournaments

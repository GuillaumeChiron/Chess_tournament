from rich.table import Table
from tinydb import Query, TinyDB

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
        list_of_keys = []
        for cle in all_users[0].keys():
            list_of_keys.append(cle)
        titles = list_of_keys[0:4]
        for title in titles:
            table_players.add_column(title)
        for info in all_users:
            table_players.add_row(info["Prenom"], info["Nom"], info["Identifiant"], info["Date_de_naissance"])
        return table_players

    # affiche un tournoi de la base de données dans un tableau
    @staticmethod
    def tournament(tournoi):
        result = tournaments_db.search(
            qr.Nom.test(lambda v: v.lower() == tournoi.lower())
        )

        # création du tableau
        table_tournament = Table(
            title="Tournoi", style="blue", header_style="blue bold"
        )
        list_of_keys = []
        for cle in result[0].keys():
            list_of_keys.append(cle)
        for i in (0, 2, 3):
            table_tournament.add_column(list_of_keys[i])

        for info in result:
            table_tournament.add_row(info["Nom"], info["Date de debut"],info["Date de fin"])
  
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
        
        list_of_keys = []
        for cle in all_tournaments[0].keys():
            list_of_keys.append(cle)
        
        titles = list_of_keys[0:2]
        for title in titles:
            table_tournaments.add_column(title)
        
        for info in all_tournaments:
            table_tournaments.add_row(info["Nom"], info["Lieu"])

        return table_tournaments

    @staticmethod
    def tournament_list_players(tournoi):
        result = tournaments_db.search(
            qr.Nom.test(lambda v: v.lower() == tournoi.lower())
        )

        # création du tableau
        table_tournament = Table(
            title=tournoi, style="blue", row_styles=["none", "blue"],
            header_style="blue bold"
        )

        players = result[0]["Joueurs"]
        players = sorted(players, key=lambda x: x["Nom"].lower())

        list_of_keys = []
        for cle in players[0].keys():
            list_of_keys.append(cle)

        titles = list_of_keys[0:4]
        for title in titles:
            table_tournament.add_column(title)
        for info in players:
            table_tournament.add_row(info["Prenom"], info["Nom"], info["Identifiant"], info["Date_de_naissance"])
       
        return table_tournament
    
    @staticmethod
    def tournament_list_rounds(tournoi):
        from chess.models.round import Round
        from chess.models.match import Match

        result = tournaments_db.search(
            qr.Nom.test(lambda v: v.lower() == tournoi.lower())
        )
         
         # création du tableau
        table_tournament = Table(
        title=tournoi, style="blue", row_styles=["none", "blue"],
        header_style="blue bold"
        )
        table_tournament.add_column("Round")
        table_tournament.add_column("matchs")

        rounds = result[0]["Rounds"]
        for r in rounds:
            round = Round.from_dict(r)
            matches = []
            for m in round.matches:
                match = Match.from_dict(m)
                matches.append(f"{match.name}: {match.player1.name} {str(match.player1.score)} / {match.player2.name} {str(match.player2.score)}")
                table_tournament.add_row(round.name, matches[0])
            
        return table_tournament

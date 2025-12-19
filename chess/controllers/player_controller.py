from rich.console import Console
from rich.table import Table
from tinydb import TinyDB, Query
from chess.models.player import Player


# initialise la mise en forme, la base de donnée et les recherches
rich = Console()
players_db = TinyDB("chess/data/players.json")
qr = Query()


class Player_controllers:

    # recupère les données des joueurs du fichier "players.json"
    @staticmethod
    def load_players():
        all_players = players_db.all()
        return all_players

    # Créer un joueur
    @staticmethod
    def create_player(name, last_name, player_id, birth):
        player = Player(name, last_name, player_id, birth)
        return player

    # sauvegarde les données d'un joueur dans la base de données "players.json"
    @staticmethod
    def save_player(player):
        player_data = player.to_dict()
        if not players_db.search(qr.Identifiant == player.player_id):
            players_db.insert(player_data)

    # Retourne les données d'un ou plusieurs joueurs en fonction de l'attribut
    @staticmethod
    def get_player(data):
        if players_db.search(qr.Prenom.test(lambda v: v.lower() == data.lower())):
            result = players_db.search(
                qr.Prenom.test(lambda v: v.lower() == data.lower())
            )
        elif players_db.search(qr.Nom.test(lambda v: v.lower() == data.lower())):
            result = players_db.search(qr.Nom.test(lambda v: v.lower() == data.lower()))
        elif players_db.search(
            qr.Identifiant.test(lambda v: v.lower() == data.lower())
        ):
            result = players_db.search(
                qr.Identifiant.test(lambda v: v.lower() == data.lower())
            )
        elif players_db.search(
            qr.Date_de_naissance.test(lambda v: v.lower() == data.lower())
        ):
            result = players_db.search(
                qr.Date_de_naissance.test(lambda v: v.lower() == data.lower())
            )
        return result

    def update_score_players(tournoi):
        from chess.models.round import Round
        from chess.models.match import Match

        round = Round.from_dict(tournoi.rounds[0])

        matches = []
        liste_players = []

        for i in round.matches:
            match = Match.from_dict(i)
            score = {
                match.player1.name: match.player1.score,
                match.player2.name: match.player2.score,
            }
            matches.append(score)

        for i in matches:
            for cle, value in i.items():
                player = Player.from_dict(Player_controllers.get_player(cle)[0])
                if player.name == cle:
                    player.score = value
                liste_players.append(player.to_dict())

        liste_players.sort(key=lambda x: x["Score"], reverse=True)
        tournoi.players = liste_players
        return tournoi

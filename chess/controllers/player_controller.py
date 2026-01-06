from tinydb import Query, TinyDB
from chess.models.player import Player

# initialise la base de données et les recherches dans la base de données
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

    # Tri les joueurs en fonction de leur score
    def sorted_players(tournoi):

        players_copy = tournoi.players.copy()
        list_of_players = []
        for p in players_copy:
            list_of_players.append(p)

        # Tri par score décroissant
        list_of_players = sorted(
            list_of_players, key=lambda p: p["Score"], reverse=True
        )
        return list_of_players

    # mets à jour les score des joueurs dans un tournoi
    def update_score_players(tournoi):
        from chess.models.match import Match
        from chess.models.round import Round
        
        # permet de recréer un round
        round = Round.from_dict(tournoi.rounds[tournoi.current_round_index - 1])
        players_copy = tournoi.players.copy()
        liste_object_players = []
        liste_players = []

        for p in players_copy:
            player = Player.from_dict(p)
            liste_object_players.append(player)

        # recréer un match pour mettre à jour les scores
        for m in round.matches:
            match = Match.from_dict(m)

            for p in liste_object_players:
                if match.player1.name == p.name:
                    p.score = match.player1.score
                    liste_object_players.remove(p)

                elif match.player2.name == p.name:
                    p.score = match.player2.score
                    liste_object_players.remove(p)
                # ajoute dans la liste "liste_players" les nouveau scores
                liste_players.append(p.to_dict())

        # Tri les joueurs en focntion de leur score par ordre décroissant 
        liste_players.sort(key=lambda x: x["Score"], reverse=True)
        tournoi.players = liste_players
        return tournoi

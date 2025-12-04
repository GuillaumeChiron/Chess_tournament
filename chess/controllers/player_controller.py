from rich.console import Console
from rich.table import Table
from tinydb import TinyDB, Query
from chess.models.player import Player


# initialise la mise en forme
rich = Console()

# initialise une base de données
player_db = TinyDB("chess/data/players.json")
# initialise la recherche
qr = Query()


def add_player(name, last_name, chess_id, birth):

    # initialise un joeur
    player1 = Player(name, last_name, chess_id, birth)
    player_data = player1.to_dict()

    # insert les données d'un joueurs si elles n'existent pas dans la base de données
    if not player_db.search(qr.Identifiant == chess_id):
        player_db.insert(player_data)
        rich.print("Joueur ajouté", style="blue bold")


def print_player(data):

    # cherche le joueur dans la base de donnée
    result = player_db.search(qr.Prenom == data)
    if not result:
        rich.print("Ce joueur n'existe pas", style="red bold")
    else:
        for info in result:
            # création du tableau
            table_player = Table(
                title=result[0]["Prenom"], style="blue", header_style="blue bold"
            )
            for cle in info.keys():
                table_player.add_column(cle)
            table_player.add_row(*[str(value) for value in info.values()])
            rich.print(table_player)
            print(" ")

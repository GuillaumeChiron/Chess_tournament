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


# ajoute un joueur a la base de données
def add_player(name, last_name, chess_id, birth):

    # initialise un joeur
    player1 = Player(name, last_name, chess_id, birth)
    # transforme les données de la Classe en un dictionnaire
    player_data = player1.to_dict()

    # insert les données d'un joueurs si elles n'existent pas dans la base de données
    if not player_db.search(
        qr.Identifiant.test(lambda v: v.lower() == chess_id.lower())
    ):
        player_db.insert(player_data)
        rich.print("Joueur ajouté", style="blue bold")
    else:
        rich.print("L'identifiant de ce joueur est déja existant", style="red bold")


# affiche un joueur de la base de données dans un tableau
def print_player(data):

    # cherche le joueur dans la base de donnée
    result = player_db.search(qr.Prenom.test(lambda v: v.lower() == data.lower()))
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


# affiche tous les joueurs de la base de données dans un tableau
def print_list_players():

    # Stock les données de players.json dans "all_users"
    all_users = player_db.all()

    # Cr&ation du tableau
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

    print(" ")
    rich.print(table_players)
    print(" ")

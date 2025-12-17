from rich.console import Console
from chess.controllers.player_controller import create_player, save_player, get_player
from chess.controllers.reports_controller import player

rich = Console()


def player_menu():

    while True:

        rich.print("1 Ajouter un joueur", style="green bold")
        rich.print("2 Afficher un joueur", style="green bold")
        rich.print("3 Quitter", style="red bold")
        print(" ")
        option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
        print(" ")

        if option == 1:
            add_player()
            print(" ")
        elif option == 2:
            print_player()
            print(" ")

        elif option == 3:
            break


# selecionne les joueurs pour un tournoi
def select_players():
    from chess.models.player import Player

    liste_players = []
    liste_players_data = []
    count = int(input("Nombre de particiapants: "))
    for i in range(count):
        id = input("Identifiant du joueur: ")
        player_data = get_player(id)
        liste_players_data.append(player_data[0])
        joueur = Player.from_dict(player_data[0])
        liste_players.append(joueur.name)
    return liste_players, liste_players_data


# ajouyer un joueur à la base de données
def add_player():
    name = rich.input("[yellow]Prénom: [/]")
    last_name = rich.input("[yellow]Nom : [/]")
    chess_id = rich.input("[yellow]chess_ID: [/]")
    birth = rich.input("[yellow]Date de niassance: ")
    print(" ")
    player = create_player(name, last_name, chess_id, birth)
    save_player(player)
    print(" ")


def print_player():
    name = rich.input("[yellow]Quel joueur voulez-vous afficher ? [/]")
    print(" ")
    table_player = player(name)
    if table_player:
        rich.print(table_player)
    else:
        not_player()


def not_player():
    rich.print("Ce joueur n'existe pas", style="red bold")

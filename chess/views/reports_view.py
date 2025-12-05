from chess.controllers.player_controller import print_list_players
from chess.controllers.tournament_controller import print_list_tournament
from rich.console import Console
from rich.table import Table
from tinydb import TinyDB, Query

rich = Console()
player_db = TinyDB("chess/data/players.json")
qr = Query()


def reports_menu():

    while True:

        rich.print("1 Détails des [bold]Joueurs[/]", style="green")
        rich.print("2 Détails des [bold]Tournois[/]", style="green")
        rich.print("3 Quitter", style="red bold")
        print(" ")
        option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
        print(" ")

        if option == 1:
            print_list_players()
            print(" ")

        elif option == 2:
            print_list_tournament()
            print(" ")

        elif option == 3:
            break

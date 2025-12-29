from rich.console import Console

from chess.views.player_view import player_menu
from chess.views.reports_view import reports_menu
from chess.views.tournament_view import tournament_menu

rich = Console()


def menu_principal():

    while True:

        print(" ")
        rich.print("1 Tournoi", style="green bold")
        rich.print("2 Rapports", style="green bold")
        rich.print("3 Quitter l'application", style="red bold")
        print(" ")

        choice = int(rich.input("[yellow]Veuillez faire un choix: [/]"))
        print(" ")

        if choice == 1:
            while True:
                rich.print("1 Interface des joueurs", style="green bold")
                rich.print("2 Interface des tournois", style="green bold")
                rich.print("3 Quitter", style="red bold")
                print(" ")
                option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
                print(" ")
                if option == 1:
                    player_menu()
                    print(" ")
                elif option == 2:
                    tournament_menu()
                    print(" ")
                elif option == 3:
                    break
        elif choice == 2:
            reports_menu()
        elif choice == 3:
            rich.print("Application quittée", style="red bold")
            print(" ")
            quit()

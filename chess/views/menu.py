from chess.views.player_view import player_menu
from chess.views.tournament_view import tournament_menu
from chess.views.reports_view import reports_menu
from rich.console import Console

rich = Console()


def menu_principal():

    while True:

        print(" ")
        rich.print("1 Joueur", style="green")
        rich.print("2 Tournoi", style="green")
        rich.print("3 Rapports", style="green")
        rich.print("4 Quitter l'application", style="red bold")
        print(" ")

        choice = int(rich.input("[yellow]Veuillez faire un choix: [/]"))
        print(" ")

        if choice == 1:
            player_menu()

        elif choice == 2:
            tournament_menu()

        elif choice == 3:
            reports_menu()

        elif choice == 4:
            rich.print("Application quittée", style="red")
            print(" ")
            quit()

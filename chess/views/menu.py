from rich.console import Console
from chess.views.player_view import Player_views
from chess.views.reports_view import Reports_views
from chess.views.tournament_view import Tournament_views

rich = Console()


class Menu_views:

    @staticmethod
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
                        Player_views.player_menu()
                        print(" ")
                    elif option == 2:
                        Tournament_views.tournament_menu()
                        print(" ")
                    elif option == 3:
                        break
            elif choice == 2:
                Reports_views.reports_menu()
            elif choice == 3:
                rich.print("Application quittée", style="red bold")
                print(" ")
                quit()

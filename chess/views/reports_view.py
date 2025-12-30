from rich.console import Console
from rich.table import Table
from tinydb import Query, TinyDB

from chess.controllers.reports_controller import Reports_controller

rich = Console()


class Reports_views:

    @staticmethod
    def reports_menu():

        while True:

            rich.print("1 Détails des joueurs", style="green bold")
            rich.print("2 Détails des tournois", style="green bold")
            rich.print("3 Dates d'un tournoi", style="green bold")
            rich.print("4 Détails des joueurs d'un tournoi", style="green bold")
            rich.print(
                "5 Détails des rounds et des matchs d'un tournoi", style="green bold"
            )
            rich.print("6 Quitter", style="red bold")
            print(" ")
            option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
            print(" ")

            if option == 1:
                rich.print(Reports_controller.list_players())
                print(" ")

            elif option == 2:
                rich.print(Reports_controller.list_tournaments())
                print(" ")

            elif option == 3:
                rich.print("dates d'un tournoi")

            elif option == 4:
                rich.print("détails joueurs d'un tournoi")

            elif option == 5:
                rich.print("détails rounds et matchs d'un tournoi")

            elif option == 6:
                break

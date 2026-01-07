from rich.console import Console
from chess.models.tournament import Tournament
from chess.controllers.tournament_controller import Tournament_controller

rich = Console()


class Tournament_views:

    @staticmethod
    def tournament_menu():

        while True:

            rich.print("1 Créer un tournoi", style="green bold")
            rich.print("2 Afficher un tournoi", style="green bold")
            rich.print("3 Démarrer un tournoi", style="green bold")
            rich.print("4 Reprendre un tournoi", style="green bold")
            rich.print("5 Quitter", style="red bold")
            print(" ")

            option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
            print(" ")

            if option == 1:
                Tournament_views.add_tournament()
                rich.print("Tournoi créé", style="blue bold")
                print(" ")

            elif option == 2:
                rich.print("Démarrer un tournoi")

            elif option == 3:
                rich.print("Reprendre un tournoi")

            elif option == 4:
                break

    # Créer un tournoi et l'enregistrer dans la base de données
    @staticmethod
    def add_tournament():
        from chess.views.player_view import Player_views

        name = rich.input("[yellow]Nom: [/]")
        location = rich.input("[yellow]Lieu: [/]")
        players = Player_views.select_players()
        description = rich.input("[yellow]Description: [/]")
        print(" ")

        tournoi = Tournament_controller.create_tournament(
            name, location, players, description
        )
        Tournament_controller.save_tournament(tournoi)

    # Affiche un tournoi de la base de données
    @staticmethod
    def get_start_tournament():
        pass

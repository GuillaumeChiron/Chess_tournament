from rich.console import Console

from chess.controllers.tournament_controller import Tournament_controller

rich = Console()


class Tournament_views:

    @staticmethod
    def tournament_menu():

        while True:

            rich.print("1 Créer un tournoi", style="green bold")
            rich.print("2 Démarrer un tournoi", style="green bold")
            rich.print("3 Reprendre un tournoi", style="green bold")
            rich.print("4 Quitter", style="red bold")
            print(" ")

            option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
            print(" ")

            if option == 1:
                Tournament_views.add_tournament()
                rich.print("Tournoi créé", style="blue bold")
                print(" ")

            elif option == 2:
                name_tournament = rich.input("[yellow]Saisir le nom du tournoi: [/]")
                Tournament_controller.run_tournament(name_tournament)

            elif option == 3:
                name_tournament = rich.input("[yellow]Saisir le nom du tournoi: [/]")
                Tournament_controller.resume_tournament(name_tournament)

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
        rounds = int(rich.input("[yellow]Nombre de rounds: [/]"))
        print(" ")

        tournoi = Tournament_controller.create_tournament(
            name, location, players, description, rounds
        )
        Tournament_controller.save_tournament(tournoi)

    # demande si on veut lancer le round suivant d'un tournoi
    @staticmethod
    def ask_next_round() -> str:
        choice = rich.input("[yellow]Lancer le round suivant (oui/non): [/]")
        return choice

    # Affiche un tournoi de la base de données
    @staticmethod
    def get_start_tournament():
        pass

from rich.console import Console

from chess.controllers.tournament_controller import Tournament_controller
from chess.models.tournament import Tournament

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

    # Affiche les scores des joueurs d'un tournoi
    @staticmethod
    def print_players_scores(tournoi: Tournament):
        from chess.models.player import Player

        # Recréer les joueurs sous fourme d'objet et les stocks dans une liste
        list_of_players = []
        for player_data in tournoi.players:
            player = Player.from_dict(player_data)
            list_of_players.append(player)

        # Affiche le round en cours
        print(" ")
        rich.print(f"Round {str(tournoi.current_round_index)}", style="purple bold")
        print(" ")
        # affiche les prenoms et noms des joueurs avec leur scores
        for player_object in list_of_players:
            rich.print(
                f"{player_object.name} {player_object.last_name}: {player_object.score}",
                style="blue bold",
            )

        print(" ")

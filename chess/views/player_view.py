from rich.console import Console

from chess.controllers.player_controller import Player_controllers
from chess.controllers.reports_controller import Reports_controller

rich = Console()


class Player_views:

    @staticmethod
    def player_menu():

        while True:

            rich.print("1 Ajouter un joueur", style="green bold")
            rich.print("2 Afficher un joueur", style="green bold")
            rich.print("3 Quitter", style="red bold")
            print(" ")
            option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
            print(" ")

            if option == 1:
                Player_views.add_player()
                print(" ")
            elif option == 2:
                Player_views.print_player()
                print(" ")

            elif option == 3:
                break

    # selecionne les joueurs pour un tournoi
    @staticmethod
    def select_players() -> list:
        from chess.models.player import Player

        liste_players = []
        count = int(input("Nombre de particiapants: "))
        for i in range(count):
            id = input("Identifiant du joueur: ")
            player_data = Player_controllers.get_player(id)
            liste_players.append(player_data[0])
        return liste_players

    # ajouyer un joueur à la base de données
    @staticmethod
    def add_player():
        name = rich.input("[yellow]Prénom: [/]")
        last_name = rich.input("[yellow]Nom : [/]")
        chess_id = rich.input("[yellow]chess_ID: [/]")
        birth = rich.input("[yellow]Date de niassance: ")
        print(" ")
        player = Player_controllers.create_player(name, last_name, chess_id, birth)
        Player_controllers.save_player(player)
        print(" ")

    @staticmethod
    def print_player():
        name = rich.input("[yellow]Quel joueur voulez-vous afficher ? [/]")
        print(" ")
        table_player = Reports_controller.player(name)
        if table_player:
            rich.print(table_player)
        else:
            Player_views.not_player()

    @staticmethod
    def not_player():
        rich.print("Ce joueur n'existe pas", style="red bold")

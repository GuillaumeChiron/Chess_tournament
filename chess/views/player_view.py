from rich.console import Console
from chess.controllers.player_controller import add_player, print_player

rich = Console()


def player_menu():

    while True:

        rich.print("1 Ajouter un [bold]Joueur[/]", style="green")
        rich.print("2 Afficher un [bold]Joueur[/]", style="green")
        rich.print("3 Quitter", style="red bold")
        print(" ")
        option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
        print(" ")

        if option == 1:

            name = rich.input("[yellow]Prénom: [/]")
            last_name = rich.input("[yellow]Nom : [/]")
            chess_id = rich.input("[yellow]chess_ID: [/]")
            birth = rich.input("[yellow]Date de niassance: ")
            print(" ")
            add_player(name, last_name, chess_id, birth)
            print(" ")

        elif option == 2:
            name1 = rich.input("[yellow]Quel joueur voulez-vous afficher ? [/]")
            print(" ")
            print_player(name1)
            print(" ")

        elif option == 3:
            break

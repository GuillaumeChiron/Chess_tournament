from rich.console import Console
from chess.models.player import Player

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

            player_data = Player(name, last_name, chess_id, birth)
            joueur = player_data.serialize_to_dict()

            for info in joueur:
                rich.print(f"[blue bold]{info}[/] : {joueur[info]}")
            print(" ")
            rich.print("Joueur ajouté", style="blue")
            print(" ")

        elif option == 2:
            rich.input("[yellow]Quel joueur voulez-vous afficher ? [/]")
            print(" ")
            rich.print("Joueur affiché", style="blue")
            print(" ")
        elif option == 3:
            break

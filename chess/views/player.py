from rich.console import Console
from chess.models.player import Player

rich = Console()


def player_menu():

    guitou = Player("Guitou", "Chiron", "GC6754", "14/06/2000")
    condition = True
    while condition:

        rich.print("1 Ajouter un joueur à la base de données", style="green")
        rich.print("2 Afficher un joueur de la base de données", style="green")
        rich.print("3 Retour au menu précendent", style="green")
        print(" ")
        option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
        print(" ")

        if option == 1:
            rich.print("Joueur ajouté", style="blue")
            print("------------------------")

        elif option == 2:
            rich.input("[yellow]Quel joueur voulez-vous afficher ? [/]")
            print(" ")
            dict = guitou.serialize_to_dict()
            for i in dict:
                rich.print(f"[blue bold]{i} : [/]{dict[i]}")
            print("------------------------")
        elif option == 3:
            condition = False

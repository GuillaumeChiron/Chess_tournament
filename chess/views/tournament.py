from rich.console import Console

rich = Console()


def tournament_menu():

    condition = True
    while condition:

        rich.print("1 Selectionner un tournoi existant", style="green")
        rich.print("2 Créer un nouveau tournoi", style="green")
        rich.print("3 Retour au menu précedent", style="green")
        print(" ")

        option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
        print(" ")

        if option == 1:

            rich.input("[yellow]Vous pouvez choisir un tournoi: [/]")
            print(" ")

        elif option == 2:
            rich.print("Tournoi créé", style="blue")
            print(" ")

        elif option == 3:
            condition = False

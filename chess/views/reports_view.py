from rich.console import Console

rich = Console()


def reports_menu():

    while True:

        rich.print("1 Détails des [bold]Joueurs[/]", style="green")
        rich.print("2 Détails des [bold]Tournois[/]", style="green")
        rich.print("3 Quitter", style="red bold")
        print(" ")
        option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
        print(" ")

        if option == 1:
            rich.print("Liste joueurs: ", style="blue")
            print(" ")

        elif option == 2:
            rich.print("Liste des tounois: ", style="blue")
            print(" ")

        elif option == 3:
            break

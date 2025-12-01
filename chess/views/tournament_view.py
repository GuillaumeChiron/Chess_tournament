from rich.console import Console

rich = Console()


def tournament_menu():

    while True:

        rich.print("1 Créer un [bold]Tournoi[/]", style="green")
        rich.print("2 Selectionner un [bold]Tournoi[/]", style="green")
        rich.print("3 Quitter", style="red bold")
        print(" ")

        option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
        print(" ")

        if option == 1:
            rich.print("Tournoi créé", style="blue")
            print(" ")

        elif option == 2:
            tournament_name = rich.input("[yellow]Vous pouvez choisir un tournoi: [/]")
            print(" ")
            rich.print(f"Tournoi: {tournament_name}", style="blue")
            print(" ")

            while True:

                rich.print("1 Résultats", style="green")
                rich.print("2 Gestion des Rounds", style="green")
                rich.print("3 Quitter", style="red bold")
                print(" ")

                option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
                print(" ")

                if option == 1:
                    rich.print("Resultat: ", style="blue")
                    print(" ")

                elif option == 2:
                    rich.print("Gérer vos Rounds: ", style="blue")
                    print(" ")

                elif option == 3:
                    break

        elif option == 3:
            break

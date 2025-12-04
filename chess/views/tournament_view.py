from rich.console import Console
from chess.controllers.tournament_controller import add_tournament, print_tournament

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

            name = rich.input("[yellow]Nom: [/]")
            location = rich.input("[yellow]Lieu: [/]")
            start_date = rich.input("[yellow]Date de début: [/]")
            end_date = rich.input("[yellow]Date de fin: [/]")
            total_rounds = rich.input("[yellow]Nombre de rounds(minimum 4): [/]")
            players = rich.input("[yellow]Liste des joueurs: [/]")
            description = rich.input("[yellow]Description: [/]")
            print(" ")
            add_tournament(
                name, location, start_date, end_date, players, description, total_rounds
            )
            rich.print("Tournoi créé", style="blue")
            print(" ")

        elif option == 2:
            tournament_name = rich.input("[yellow]Vous pouvez choisir un tournoi: [/]")
            print(" ")
            rich.print(f"Tournoi: {tournament_name}", style="blue")
            print(" ")
            print_tournament(tournament_name)
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

from rich.console import Console

rich = Console()


class Tournament_views:

    @staticmethod
    def tournament_menu():

        while True:

            rich.print("1 Créer un tournoi", style="green bold")
            rich.print("2 Afficher un tournoi", style="green bold")
            rich.print("3 Démarrer un tournoi", style="green bold")
            rich.print("4 Reprendre un tournoi", style="green bold")
            rich.print("5 Quitter", style="red bold")
            print(" ")

            option = int(rich.input("[yellow]Veuillez faire votre choix: [/]"))
            print(" ")

            if option == 1:
                rich.print("Créer un tournoi")
            elif option == 2:
                rich.print("Afficher un tournoi")
            elif option == 3:
                rich.print("Démarrer un tournoi")
            elif option == 4:
                rich.print("Reprendre un tournoi")
            elif option == 5:
                break

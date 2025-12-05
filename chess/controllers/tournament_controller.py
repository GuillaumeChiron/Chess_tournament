from rich.console import Console
from rich.table import Table
from tinydb import TinyDB, Query
from chess.models.tournament import Tournament

rich = Console()
tournament_db = TinyDB("chess/data/tournaments.json")
qr = Query()


# ajoute un tournoi dans la base de données
def add_tournament(name, location, players, desciption, total_rounds, round):

    tournament = Tournament(name, location, players, desciption, total_rounds, round)
    tournament.start_tournament()
    # transforme les données de la Classe en un dictionnaire
    tournament_data = tournament.to_dict()

    if not tournament_db.search(qr.Nom.test(lambda v: v.lower() == name.lower())):
        tournament_db.insert(tournament_data)
        rich.print("Tournoi Créé", style="blue bold")
    else:
        rich.print("Ce Tournoi est déja existant", style="red bold")


# affiche un tournoi de la base de données dans un tableau
def print_tournament(data):
    result = tournament_db.search(qr.Nom.test(lambda v: v.lower() == data.lower()))
    if not result:
        rich.print("Ce tournoi n'esxiste pas", style="red bold")
    else:
        # création du tableau
        table_tournament = Table(
            title=result[0]["Nom"], style="blue", header_style="blue bold"
        )
        for info in result:
            for cle in info.keys():
                table_tournament.add_column(cle)
            table_tournament.add_row(*[str(value) for value in info.values()])
            rich.print(table_tournament)


# affiche tous les tournois de la base de données dans un tableau
def print_list_tournament():
    # stock les données de tournaments.json dans "all_tournaments"
    all_tournaments = tournament_db.all()

    # création du tableau
    table_players = Table(
        title="Liste des Tournois",
        row_styles=["none", "blue"],
        header_style="blue bold",
        style="blue",
    )

    for cle in all_tournaments[0].keys():
        table_players.add_column(cle)
    for info in all_tournaments:
        table_players.add_row(*(str(value) for value in info.values()))

    print(" ")
    rich.print(table_players)
    print(" ")

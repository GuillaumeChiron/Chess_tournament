from rich.console import Console
from rich.table import Table
from tinydb import TinyDB, Query
from chess.models.tournament import Tournament

rich = Console()
tournament_db = TinyDB("chess/data/tournaments.json")
qr = Query()


def add_tournament(
    name, location, start_date, end_date, players, desciption, total_rounds
):

    tournament = Tournament(
        name, location, start_date, end_date, players, desciption, total_rounds
    )

    tournament_data = tournament.to_dict()

    if not tournament_db.search(qr.Nom == name):
        tournament_db.insert(tournament_data)
    print(tournament_data)


def print_tournament(data):
    result = tournament_db.search(qr.Nom == data)
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

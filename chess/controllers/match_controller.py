from rich.console import Console
from rich.table import Table
from tinydb import TinyDB, Query
from chess.models.match import Match

# initialise la mise en forme
rich = Console()

# initialise la base de données et les recherches dans la base de données
match_db = TinyDB("chess/data/tournaments.json")
qr = Query()


def add_match(name, player1, player2, score1, score2):

    match1 = Match(name, player1, player2, score1, score2)
    match_data = match1.to_dict()

    if not match_db.search(qr.Match == name):
        match_db.insert(match_data)


def print_match(data):
    result = match_db.search(qr.Match == data)
    if not result:
        rich.print("Ce joueur n'existe pas", style="red bold")

    else:
        for info in result:
            # création du tableau
            table_match = Table(
                title=result[0]["Match"], style="blue", header_style="Blue bold"
            )
            table_match.add_column("Match", style="purple")
            table_match.add_column("Joueur 1")
            table_match.add_column("Joueur 2")
            table_match.add_column("Score joueur 1")
            table_match.add_column("Score joueur 2")

            table_match.add_row(*[str(value) for value in info.values()])
            rich.print(table_match)

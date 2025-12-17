from rich.console import Console
from chess.models.match import Match

rich = Console()


def ask_scores(data):
    match = Match.from_dict(data)
    rich.print(
        f"{match.name}:\n {match.player1.name} {match.score1} / {match.player2.name} {match.score2}"
    )
    print(" ")
    match.score1 = int(input(f"Veuillez saisir le score de {match.player1.name}: "))
    match.score2 = int(input(f"Veuillez saisir le score de {match.player2.name}: "))
    print(" ")
    rich.print(f"Score {match.player1.name}: {match.score1}")
    rich.print(f"Score {match.player2.name}: {match.score2}")
    print(" ")
    return match

from rich.console import Console
from chess.models.match import Match

rich = Console()


def ask_scores(data):
    match = Match.from_dict(data)
    rich.print(
        f"{match.name}:\n {match.player1.name} {match.score1} / {match.player2.name} {match.score2}"
    )
    print(" ")
    score = float(input(f"Veuillez saisir le score de {match.player1.name}: "))
    print(" ")
    if score == 1:
        match.score1 += 1
    elif score == 0:
        match.score2 += 1
    elif score == 0.5:
        match.score1 += 0.5
        match.score2 += 0.5
    print(" ")
    rich.print(
        f"Score {match.player1.name}: {match.score1} / {match.player2.name}: {match.score2}"
    )
    print(" ")
    return match

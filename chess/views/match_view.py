from rich.console import Console

from chess.models.match import Match

rich = Console()


class Match_views:

    @staticmethod
    def ask_scores(data: dict) -> Match:
        match = Match.from_dict(data)
        rich.print(
            f"{match.name}:\n {match.player1.name} {match.player1.score} / {match.player2.name} {match.player2.score}"
        )
        print(" ")
        score = float(input(f"Veuillez saisir le score de {match.player1.name}: "))

        if score == 1:
            match.player1.score += 1
        elif score == 0:
            match.player2.score += 1
        elif score == 0.5:
            match.player1.score += 0.5
            match.player2.score += 0.5

        rich.print(
            f"Score {match.player1.name}: {match.player1.score} / {match.player2.name}: {match.player2.score}"
        )
        print(" ")
        return match

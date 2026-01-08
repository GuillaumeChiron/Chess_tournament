from rich.console import Console

from chess.models.match import Match

rich = Console()


class Match_views:

    @staticmethod
    def ask_scores(data: dict) -> Match:
        match = Match.from_dict(data)
        print(" ")
        rich.print(
            f"{match.name}:\n {match.player1.name} {0} / {match.player2.name} {0}"
        )
        print(" ")
        score = float(input(f"Veuillez saisir le score de {match.player1.name}: "))

        if score == 1:
            match.player1.score += 1
            score1 = 1
            score2 = 0
        elif score == 0:
            match.player2.score += 1
            score1 = 0
            score2 = 1
        elif score == 0.5:
            match.player1.score += 0.5
            match.player2.score += 0.5
            score1 = 0.5
            score2 = 0.5

        rich.print(
            f"Score {match.player1.name}: {score1} / {match.player2.name}: {score2}"
        )
        print(" ")
        return match

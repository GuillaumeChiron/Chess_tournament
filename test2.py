from rich.console import Console
from chess.views.player_view import select_players
from chess.controllers.player_controller import (
    get_player,
    create_player,
    save_player,
    load_players,
)
from chess.controllers.round_controller import (
    update_round,
    generate_first_round,
    save_round,
)
from chess.controllers.tournament_controller import (
    create_tournament,
    save_tournament,
    update_tournament,
)
from chess.controllers.match_controller import update_match_scores
from chess.views.match_view import ask_scores

rich = Console()


name = "tournoi 10"
location = "Reims"
players = select_players()
description = "tournoi des goooooat"

tournament = create_tournament(name, location, players[0], description)
tournament_data = tournament.to_dict()
rich.print(tournament_data)

players = players[1]
tournament.start_tournament()
round = generate_first_round(players)

round.start_round()
round_data = update_round(round)
round.end_round()

round_data = round.to_dict()
tournament.rounds = round_data
tournament_data = tournament.to_dict()

rich.print(tournament_data)

from rich.console import Console
from chess.models.player import Player
from chess.controllers.player_controller import load_players, get_player
from chess.controllers.reports_controller import (
    tournament,
    list_tournaments,
    player,
    list_players,
)

rich = Console()

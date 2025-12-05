from rich.console import Console
from tinydb import TinyDB, Query
import random
from chess.models.round import Round
from chess.models.match import Match
from chess.models.match import Player

rich = Console()
players_db = TinyDB("chess/data/players.json")
qr = Query()
all_users = players_db.all()

tirage = random.sample(all_users, 4)
joueurs = []

for info in tirage:
    joueurs.append(info)


player1 = Player.from_dict(joueurs[0])
player2 = Player.from_dict(joueurs[1])
player3 = Player.from_dict(joueurs[2])
player4 = Player.from_dict(joueurs[3])

"""
rich.print(player1.name, player1.player_id, style="green")
rich.print(player2.name, player2.player_id, style="green")
rich.print(player3.name, player3.player_id, style="green")
rich.print(player4.name, player4.player_id, style="green")

guillaume = Player("guillaume", "chiron", "gc1111", "14/06/2000")
alyssa = Player("alyssa", "chiron", "ac2222", "04/05/2008")
arnaud = Player("arnaud", "chiron", "ac3333", "05/09/1996")
amelie = Player("amelie", "chiron", "ac4444", "15/01/1993")
"""

match1 = Match("match 1", player1, player2)
match2 = Match("match 2", player3, player4)


liste_matches = []
liste_matches.append(match1.to_dict())
liste_matches.append(match2.to_dict())

round1 = Round("Round 1", liste_matches)

round1.start_round()
round1.end_round()

rich.print(round1.generate_round(), style="blue bold")

from tinydb import TinyDB, Query
from chess.models.player import Player

# initialise une base de données
player_db = TinyDB("chess/data/players.json")
# initialise la recherche
user = Query()
# initialise un joueur
name = input("Prenom: ")
last_name = input("Nom: ")
chess_id = input("Chess_id : ")
birth = input("age: ")
player1 = Player(name, last_name, chess_id, birth)

fichier = player1.to_dict()

# insert les données d'un joueurs si elles n'existent pas dans la base de données
if not player_db.search(user.Prenom == name):
    player_db.insert(fichier)

data = player_db.all()

for info in data:
    print(info)

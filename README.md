# Chess Tournament

Ce projet est un gestionnaire de tournois d’échecs, qui a pour but d’aider un petit club.  
L’objectif est de créer un programme qui fonctionne de manière locale afin que le club puisse l’utiliser sans connexion internet.

## Fonctionnalités global

- Créer des joueurs et les enregistrer dans une base de données
- Créer des tournois et les enregistrer dans une base de données
- Exécuter un tournoi et le stopper à tout moment
- Enregistrer les tournois avec leurs rounds et matchs dans une base de données
- Affichage des rapports (rapports de joueurs et de tournois)

## Packages utilisés

- Rich
- TinyDB
- Isort
- Flake8

## Fonctionnalités et architecture

### Programmation Orientée Objet (POO)

Le projet repose sur les principes de la **programmation orientée objet** afin de modéliser les entités du tournoi de manière claire et cohérente.

Les principales classes du projet sont :
- `Player` : représente un joueur avec ses informations (nom, prénom, identifiant, score, adversaires)
- `Tournament` : gère les informations générales du tournoi et son déroulement
- `Round` : représente un tour du tournoi
- `Match` : gère les matchs entre deux joueurs et leurs résultats

Chaque classe est responsable de ses propres données et comportements, ce qui permet :
- une meilleure lisibilité du code
- une maintenance facilitée
- une évolution plus simple du projet

### Architecture MVC

Le projet est structuré selon le modèle **MVC (Modèle – Vue – Contrôleur)** afin de garantir une séparation claire des responsabilités.

- **Modèle**  
  Gère les données et la logique métier (joueurs, tournois, tours, matchs, etc.).  
  Il est responsable de la création, de la modification et de la persistance des données.

- **Vue**  
  Gère l’interaction avec l’utilisateur via la console.  
  Elle affiche les menus, les informations et récupère les entrées utilisateur sans contenir de logique métier.

- **Contrôleur**  
  Fait le lien entre le Modèle et la Vue.  
  Il traite les actions de l’utilisateur, applique les règles du jeu et orchestre le déroulement du tournoi.


## Installation

1. **Cloner le dépôt :**

   ```bash
   git clone https://github.com/GuillaumeChiron/Chess_tournament.git
   cd Chess_tournament

---

### Utilisation

1. Exécute le script principal :
   ```bash
   python main.py

2. Entrez dans l'interface le chiffre que vous souhaitez afin de vous rendre soit dans les tournois ou soit dans les rapports.

3. Ensuite entrez dans l'interface le chiffre que vous souhaitez afin d'executer une fonction précise (par exemple: afficher les joueurs de la base de données).

## Générer un nouveau fichier flake8-html

  ```bash
  flake8 --exclude=env,__pycache__ --max-line-length=119 --format=html --htmldir=flake8-report

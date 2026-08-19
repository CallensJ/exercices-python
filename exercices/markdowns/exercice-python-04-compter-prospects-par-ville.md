# Exercice Python 04 — Compter les prospects actifs par ville

## Contexte

Dans `prospect_engine`, tu devras souvent résumer des données brutes avant de les afficher ou de les exporter. Cette fois, tu vas produire un petit rapport : le nombre de prospects **actifs** dans chaque ville.

## Objectif

Écris une fonction nommée `count_active_prospects_by_city(prospects)`.

Elle reçoit une liste de dictionnaires représentant des prospects et retourne un dictionnaire dont :

- chaque clé est le nom normalisé d'une ville ;
- chaque valeur est le nombre de prospects actifs dans cette ville.

## Données de départ

Crée un fichier `data.py` contenant :

```python
prospects = [
    {"name": "  Alice Martin ", "city": "ales", "active": True},
    {"name": "Bruno Costa", "city": "Alès", "active": False},
    {"name": "Chloé Durand", "city": " ANDUZE ", "active": True},
    {"name": "David Leroy", "city": "alès ", "active": True},
    {"name": "Emma Roy", "city": "", "active": True},
    {"name": "Farid Benali", "city": "Anduze", "active": True},
]
```

## Règles

1. Compte uniquement les prospects dont `active` vaut `True`.
2. Ignore les prospects dont `city` est vide après nettoyage.
3. Normalise chaque ville avec `strip()` puis `capitalize()` avant de l'utiliser comme clé.
4. Si une ville apparaît plusieurs fois, son compteur doit augmenter : tu ne dois pas écraser le compteur précédent.
5. La fonction ne doit ni modifier la liste `prospects`, ni afficher quoi que ce soit avec `print()`.
6. Dans `main.py`, importe les données et la fonction, appelle-la, puis affiche son résultat.

## Résultat attendu

L'exécution de `main.py` doit afficher :

```python
{"Alès": 2, "Anduze": 2}
```

L'ordre d'affichage peut varier selon ta manière de construire le dictionnaire ; ce n'est pas un problème.

## Ce qui est évalué

- parcourir une liste de dictionnaires ;
- filtrer avec une condition ;
- utiliser un dictionnaire comme compteur ;
- écrire une fonction qui reçoit ses données en paramètre ;
- organiser un mini-projet avec `data.py`, un fichier de fonction et `main.py`.

## Avant de coder

Envoie-moi d'abord ton pseudo-code ou explique, en quelques phrases, ce qui doit se passer lorsqu'une ville apparaît pour la première fois, puis lorsqu'elle apparaît une deuxième fois.

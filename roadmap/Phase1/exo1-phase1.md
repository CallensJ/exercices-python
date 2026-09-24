# Exercice 1 — Phase 1 : Variables, types et structures de données de base

## Objectif

Manipuler les types primitifs de Python (`int`, `float`, `str`, `bool`), la conversion de types, et une première prise en main des quatre structures de collection (`list`, `tuple`, `dict`, `set`) — sans entrer dans leur manipulation avancée (ce sera l'exercice 2).

## Contexte

Tu vas écrire un script `profile_card.py` qui construit et affiche une fiche d'identité à partir d'entrées utilisateur.

## Consignes

1. Demande à l'utilisateur (`input()`) : son prénom, son nom, son âge, sa taille en mètres (ex: `1.78`).
   Attention : `input()` renvoie toujours une chaîne de caractères — convertis explicitement l'âge en `int` et la taille en `float`.

2. Stocke une liste (`list`) de 3 à 5 loisirs, saisis un par un ou en dur dans le code (au choix).

3. Stocke un tuple (`tuple`) représentant une donnée qui ne doit jamais changer une fois définie (par exemple les coordonnées de naissance : `(ville, code_postal)`, ou une date de naissance `(jour, mois, annee)`).

4. Stocke un set (`set`) de compétences, en veillant à démontrer qu'un set élimine automatiquement les doublons (ajoute volontairement un doublon à la création et vérifie sa disparition).

5. Regroupe toutes ces informations dans un dictionnaire (`dict`) unique nommé `profile`, avec des clés explicites (`"first_name"`, `"age"`, `"hobbies"`, etc.).

6. Affiche un résumé formaté de la fiche via des f-strings, incluant :
   - une phrase de présentation (prénom, nom, âge)
   - un calcul simple utilisant l'âge (ex : âge en mois, ou année de naissance approximative)
   - un booléen calculé (ex : `is_adult = age >= 18`) affiché dans la phrase
   - la liste des loisirs
   - le tuple affiché tel quel
   - le set de compétences affiché tel quel

7. Utilise `type()` ou `isinstance()` pour vérifier et afficher le type réel d'au moins 3 variables différentes (une de chaque type primitif utilisé).

## Contraintes

- Noms de variables, fonctions et commentaires en anglais (ta convention habituelle).
- Pas de list/dict/set comprehension ici — utilise des constructions simples (ce sera vu à l'exercice suivant).
- Le script doit s'exécuter sans erreur quelle que soit la casse ou les espaces superflus saisis par l'utilisateur pour le prénom/nom (indice : une méthode de `str` peut nettoyer ça).

## Pour aller plus loin (facultatif)

- Gère le cas où l'utilisateur saisit un âge non numérique, sans faire planter le script (tu n'as pas encore vu `try/except` en détail dans cette phase, une solution simple ou une recherche ponctuelle suffit).

## Progression

Quand tu bloques plus de 2 jours sur un point précis, dis-le-moi : on ne passera pas à un exercice plus difficile, je t'en donnerai un autre sur le même thème pour consolider avant d'avancer.

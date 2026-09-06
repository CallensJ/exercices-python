# Exercice 01 — Calculatrice interactive

**Phase :** 1 — Fondamentaux de Python
**Concepts visés :** variables, types de base (`int`, `float`, `str`), conversion de types, `input()`, `print()`, opérateurs arithmétiques

## Contexte

Avant de faire quoi que ce soit d'intéressant en Python, tu dois être à l'aise avec les échanges de base entre ton programme et l'utilisateur : demander une valeur, la convertir dans le bon type, faire un calcul, afficher un résultat proprement.

## Objectif

Écris un script `calculatrice.py` qui :

1. Demande à l'utilisateur deux nombres (via `input()`).
2. Demande une opération parmi `+`, `-`, `*`, `/`.
3. Effectue le calcul correspondant.
4. Affiche le résultat avec un message clair, par exemple :
   `Résultat de 4.0 + 2.0 = 6.0`

## Contraintes

- Les nombres saisis peuvent être des entiers ou des flottants (ex : `3` ou `3.5`) — ton programme doit gérer les deux sans planter.
- Le résultat de la division doit être affiché avec 2 décimales maximum.
- Pas de gestion d'erreurs avancée pour l'instant (`try/except` n'est pas encore au programme) — on part du principe que l'utilisateur saisit des valeurs correctes.

## Piste de réflexion

- Quelle fonction utilises-tu pour transformer une chaîne de caractères saisie en `input()` en nombre exploitable pour un calcul ?
- Comment forcer l'affichage d'un nombre à virgule avec un nombre de décimales précis dans un `print()` ou une f-string ?

## Critère de validation

Le script tourne sans erreur pour les 4 opérations, avec des entiers et des flottants, et affiche un résultat lisible.

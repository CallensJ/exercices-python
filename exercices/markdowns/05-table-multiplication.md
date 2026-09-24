# Exercice 05 — Générateur de table de multiplication

**Phase :** 1 — Fondamentaux de Python
**Concepts visés :** boucles imbriquées `for`, `range()`, formatage de chaînes (f-strings), alignement de texte

## Contexte

Dernier exercice de la Phase 1 : il consolide tout ce que tu as vu (boucles, conditions légères, conversion de types) avec un accent particulier sur le formatage d'affichage — une compétence qu'on sous-estime souvent mais que tu retrouveras partout (logs, rapports, sorties d'outils).

## Objectif

Écris un script `table_multiplication.py` qui :

1. Demande à l'utilisateur un nombre entier `n` (entre 1 et 20).
2. Affiche la table de multiplication de `n`, de `n × 1` jusqu'à `n × 10`.
3. Affiche ensuite une grille complète (tableau) des tables de multiplication de 1 à `n`, bien alignée en colonnes.

Exemple pour `n = 3` (étape 2 seulement) :
```
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 10 = 30
```

Pour l'étape 3, avec `n = 3`, tu dois produire une grille 3x10 où chaque colonne est alignée verticalement, quels que soient les nombres de chiffres des résultats (1 vs 100).

## Contraintes

- Utilise des boucles `for` imbriquées pour la grille.
- Utilise le formatage des f-strings (par exemple `f"{valeur:>4}"`) pour aligner les colonnes proprement, plutôt que de la concaténation manuelle d'espaces.

## Piste de réflexion

- Comment forcer une largeur fixe pour un nombre affiché avec une f-string, pour que les colonnes restent alignées même quand les résultats ont 1, 2 ou 3 chiffres ?
- Pour la grille, quelle boucle représente les lignes, et laquelle représente les colonnes ?

## Critère de validation

Pour `n = 3` et `n = 12`, l'affichage de la table simple est correct, et la grille reste parfaitement alignée visuellement dans le terminal, sans décalage entre les lignes.

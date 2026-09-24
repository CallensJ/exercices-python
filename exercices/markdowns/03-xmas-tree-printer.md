# Exercice 03 — Xmas Tree Printer

**Phase :** 1 — Fondamentaux de Python
**Concepts visés :** boucles imbriquées, réplication de chaînes (`str * n`), concaténation, `input()`

## Contexte

Cet exercice est cité dans ta roadmap (`xmasTreePrint.py`). Il combine boucles imbriquées et manipulation de chaînes pour afficher une structure géométrique dans le terminal — un bon test de ta capacité à "penser en lignes et colonnes".

## Objectif

Écris un script `xmas_tree.py` qui demande à l'utilisateur la hauteur du sapin (un nombre entier, par exemple 5), puis affiche un sapin centré fait d'étoiles `*`, comme ceci pour une hauteur de 5 :

```
    *
   ***
  *****
 *******
*********
```

## Contraintes

- Le sapin doit être symétrique et centré (autant d'espaces à gauche que nécessaire pour centrer chaque ligne).
- Le nombre d'étoiles sur la ligne `i` (en partant de 1) doit suivre une progression simple et régulière — à toi de trouver la formule.
- Utilise uniquement `for`, `range()`, et la réplication de chaînes (`"*" * n`) — pas de bibliothèque externe.

## Piste de réflexion

- Pour une hauteur `h`, combien d'espaces faut-il avant les étoiles sur la ligne `i` ? Et combien d'étoiles ?
- Essaie d'abord sur papier ou dans un commentaire de calculer les deux formules avant de les coder.

## Bonus (facultatif)

Ajoute un "tronc" de 1 caractère de large et 2 lignes de haut, centré sous le sapin.

## Critère de validation

Pour n'importe quelle hauteur saisie (teste avec 3, 5, 10), le sapin s'affiche bien centré et symétrique, sans erreur.

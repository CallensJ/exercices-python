# Exercice 2 — Choisir le dossier de destination

## Objectif

Écrire une fonction qui valide un dossier de destination fourni sous forme de chemin (`str` ou `Path`), et retourne un résultat clair indiquant si ce dossier peut être utilisé.

## Consignes

Écris une fonction :

```python
def validate_destination_dir(path: Path) -> list[str]:
```

Elle retourne la liste des erreurs trouvées (liste vide si tout est valide). Les règles à vérifier :

- Le chemin doit exister.
- Le chemin doit être un dossier (pas un fichier).
- (Réfléchis : y a-t-il d'autres garde-fous utiles à ce stade, avant même de connaître le dossier source ? Le roadmap parle de "comparaison de chemins" — à quoi ça pourrait servir ici si on ne compare qu'un seul dossier pour l'instant ? Pas obligatoire de le résoudre maintenant, juste à y penser.)

## Contraintes

- Pas de `print()`, pas de `input()` dans cette fonction. Elle retourne une valeur ; un appelant décidera quoi afficher.
- Utilise `pathlib.Path`, pas de manipulation de chemins en `str` avec des `+` ou du slicing.
- La fonction doit pouvoir signaler plusieurs erreurs à la fois si applicable, pas juste s'arrêter à la première.

## Ce qu'on ne demande PAS encore

- Pas de création automatique du dossier s'il n'existe pas.
- Pas encore de comparaison avec un dossier source (ce sera pertinent plus tard, une fois qu'on aura les deux dossiers en main).
- Pas d'interface, pas de boucle sur des fichiers.

## Pour démarrer

Pense d'abord en pseudo-code : quelles sont les entrées, quelles conditions dois-tu vérifier, que retournes-tu dans chaque cas ?

Montre-moi ton code (ou ton pseudo-code si tu préfères démarrer par là) et on regarde ensemble.

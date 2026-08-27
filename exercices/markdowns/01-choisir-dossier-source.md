# Exercice 01 — Choisir le dossier source

**Projet :** ImageTool (convertisseur PNG/JPEG → WebP)
**Fonctionnalité liée :** 1. Choisir le dossier source

## Contexte

Avant de pouvoir convertir la moindre image, le programme doit savoir où aller les chercher. C'est la toute première brique : donner un chemin de dossier, vérifier qu'il est valide, et en extraire la liste des images qu'il contient.

## Concepts à mobiliser

- `pathlib.Path`
- chemins absolus / relatifs
- `iterdir()`
- boucles `for`
- conditions (`if` / `else`)
- listes
- `.suffix`
- `.is_file()`

Ressource si besoin : [Pathlib — Corey Schafer (YouTube)](https://www.youtube.com/watch?v=yxa-DJuuTBI)

## Objectif

Écrire un script qui :

1. Récupère un chemin de dossier (pour l'instant, via `input()` ou une variable codée en dur, peu importe — l'interface graphique viendra bien plus tard).
2. Vérifie que ce chemin existe et qu'il s'agit bien d'un dossier (pas d'un fichier). Si ce n'est pas le cas, affiche un message clair et arrête le programme proprement — pas de plantage avec une trace d'erreur brute.
3. Parcourt le contenu du dossier (uniquement les fichiers directement dedans, pas les sous-dossiers) et construit une liste des fichiers dont l'extension est `.png`, `.jpg` ou `.jpeg` — en ignorant la casse (`.PNG`, `.Jpg`, etc. doivent aussi être détectés).
4. Affiche le nombre d'images trouvées, puis leur nom, un par ligne.

## Contraintes

- Pas de bibliothèque externe pour cet exercice (pas de Pillow ici, on ne fait que lister).
- Le dossier peut contenir d'autres types de fichiers (`.txt`, `.pdf`, etc.) — ils doivent être ignorés sans faire planter le script.
- Si le dossier est vide ou ne contient aucune image, le script doit le dire clairement plutôt que d'afficher une liste vide sans explication.

## Avant de coder

Écris d'abord ton pseudo-code : quelles sont les entrées, quelles décisions le programme doit prendre, quelles actions il effectue, et quelle est la sortie attendue. Envoie-le-moi avant de passer au code — je te donne un retour dessus en premier.

## Ce que je regarderai à la correction

- Est-ce que tu utilises `Path` plutôt que des manipulations de chaînes de caractères pour les chemins ?
- Est-ce que la vérification du dossier couvre les bons cas (n'existe pas / existe mais n'est pas un dossier) ?
- Est-ce que la comparaison d'extension est vraiment insensible à la casse ?
- Est-ce que le code reste lisible — noms de variables clairs, pas de logique entassée sur une seule ligne ?

Je ne te donnerai pas le corrigé directement : si tu bloques, dis-moi où précisément, et je t'oriente avec des questions ou des indices plutôt que la solution toute faite.

## Pour aller plus loin (facultatif, pas obligatoire pour valider l'exercice)

- Que se passerait-il si tu voulais aussi détecter les images dans les sous-dossiers ? (indice : une autre méthode de `Path` existe pour ça — pas besoin de la connaître maintenant, juste d'y réfléchir)

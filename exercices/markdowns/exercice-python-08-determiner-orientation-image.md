# Exercice Python 08 — Déterminer l’orientation d’une image

## Énoncé

Écris une fonction pure `get_orientation(width, height)` qui reçoit la largeur et la hauteur d’une image, puis retourne son orientation sous forme de chaîne de caractères.

Les trois résultats possibles sont :

- `"landscape"` si la largeur est supérieure à la hauteur ;
- `"portrait"` si la hauteur est supérieure à la largeur ;
- `"square"` si les deux dimensions sont égales.

Cet exercice est indépendant des fichiers précédents. Ne réutilise pas le code de lecture d’image : travaille uniquement à partir de nombres afin de vérifier ta compréhension des fonctions et des conditions.

Avant de coder, rédige obligatoirement un pseudo-code structuré entre `DEBUT` et `FIN`. Il doit prévoir explicitement les trois orientations.

## Données de départ

Utilise ces cas de test dans `main.py` :

```python
dimensions = [
    (1920, 1080),
    (1080, 1350),
    (800, 800),
    (1200, 628),
    (600, 900),
]
```

## Contraintes

- Place la fonction dans `orientation.py` et les appels dans `main.py`.
- La fonction doit recevoir exactement deux paramètres : `width` et `height`.
- La fonction doit retourner une chaîne de caractères.
- La fonction ne doit rien afficher elle-même.
- Utilise des conditions explicites pour distinguer les trois cas.
- N’utilise ni Pillow, ni `pathlib`, ni fichier image.
- N’utilise pas de dictionnaire associant directement les dimensions aux réponses.
- Ne modifie pas la liste `dimensions`.
- Depuis `main.py`, parcours la liste avec une boucle et affiche chaque résultat sous la forme demandée.
- Ne copie pas de solution avant d’avoir fourni ton pseudo-code et une tentative exécutable.

En JavaScript, tu écrirais probablement une chaîne `if / else if / else`. Python suit la même logique, avec sa propre syntaxe et l’indentation comme structure du bloc. Le raisonnement algorithmique, lui, ne change pas de langage pour te faire plaisir.

## Résultat attendu

L’affichage doit respecter cette forme :

```text
1920x1080 -> landscape
1080x1350 -> portrait
800x800 -> square
1200x628 -> landscape
600x900 -> portrait
```

Ajoute ensuite trois appels supplémentaires choisis par toi : un paysage, un portrait et un carré. Ces appels ne doivent pas être ajoutés à la liste de départ.

## Ce qui est évalué

- **Difficulté principale :** traduire correctement trois cas métier en conditions exclusives.
- Qualité du pseudo-code `DEBUT` → `FIN`.
- Compréhension des paramètres et de la valeur de retour.
- Distinction entre calcul dans une fonction et affichage dans le programme principal.
- Utilisation correcte d’une boucle pour tester plusieurs entrées.
- Capacité à transférer un raisonnement déjà rencontré en JavaScript vers une écriture idiomatique Python.

Trace de progression à confirmer après correction :

- détection de fichiers avec `pathlib` : **première tentative fonctionnelle, consolidation en cours** ;
- paramètres et retours de fonction : **fragile, ciblés aujourd’hui** ;
- conditions : **déjà travaillées, compréhension à confirmer aujourd’hui** ;
- boucles : **déjà travaillées, consolidation en cours** ;
- pseudo-code algorithmique : **fragile** ;
- lecture d’image avec Pillow : **introduite dans l’exercice 07, validation en attente** ;
- conversion et compression : **non acquises, pas encore abordées**.

# Exercice Python 09 — Filtrer les images trop lourdes

## Énoncé

Avant de manipuler de vrais fichiers, **WebAsset Optimizer** doit pouvoir travailler avec des données déjà préparées.

Écris une fonction `get_heavy_image_names(images, max_size_kb)` qui reçoit :

- une liste de dictionnaires représentant des images ;
- un poids maximal exprimé en kilo-octets.

La fonction doit retourner une nouvelle liste contenant uniquement les noms des images dont le poids est strictement supérieur à la limite.

Avant de coder, réponds en français simple à ces quatre questions :

1. Quelle donnée entre dans la fonction ?
2. Quelle donnée doit sortir de la fonction ?
3. Que faut-il vérifier pour chaque image ?
4. Que faut-il conserver lorsque la condition est vraie ?

Transforme ensuite tes réponses en un pseudo-code court, entre `DEBUT` et `FIN`. Six à huit lignes suffisent. Le pseudo-code doit décrire les actions, pas utiliser de syntaxe Python.

## Données de départ

Place cette liste dans `data.py` :

```python
images = [
    {"name": "logo.png", "size_kb": 85},
    {"name": "hero.jpg", "size_kb": 1240},
    {"name": "menu.png", "size_kb": 640},
    {"name": "icon.webp", "size_kb": 24},
    {"name": "gallery.jpg", "size_kb": 980},
]
```

Organisation attendue :

```text
exercice-09/
├── data.py
├── image_filter.py
└── main.py
```

## Contraintes

- Place la fonction dans `image_filter.py`.
- Importe les données et appelle la fonction depuis `main.py`.
- La fonction doit utiliser les deux paramètres reçus ; elle ne doit pas importer directement `images` depuis `data.py`.
- Utilise une boucle `for`.
- Accède au nom et au poids avec les clés des dictionnaires.
- Construis une nouvelle liste sans modifier la liste d’origine.
- Ajoute uniquement le nom de l’image à la liste retournée, pas le dictionnaire complet.
- Une image dont le poids est exactement égal à la limite ne doit pas être retenue.
- La fonction doit retourner le résultat ; elle ne doit rien afficher.
- Affiche le résultat uniquement dans `main.py`.
- N’utilise pas `filter()`, de compréhension de liste, de fichier image, de `pathlib` ou de Pillow.
- Ne demande aucune valeur avec `input()` dans cet exercice.
- Ne copie pas de solution avant d’avoir écrit tes quatre réponses, ton pseudo-code et une première tentative.

En JavaScript, tu travaillerais ici avec un tableau d’objets. En Python, il s’agit d’une liste de dictionnaires : la structure change de nom, mais tu dois toujours parcourir une collection et lire une propriété — ici une clé — sur chaque élément.

## Résultat attendu

Avec une limite de `500`, le résultat attendu est :

```text
["hero.jpg", "menu.png", "gallery.jpg"]
```

Teste également ces deux limites depuis `main.py` :

- avec `1000`, seule `hero.jpg` doit être retournée ;
- avec `2000`, une liste vide doit être retournée.

## Ce qui est évalué

- **Difficulté principale :** parcourir une liste de dictionnaires et filtrer ses éléments avec une condition.
- Compréhension de l’entrée et de la sortie d’une fonction.
- Construction progressive d’une nouvelle liste.
- Utilisation correcte d’une boucle, d’une condition et de `append()`.
- Distinction entre `return` et `print()`.
- Capacité à écrire un pseudo-code court à partir de quatre questions concrètes.

Trace de progression à confirmer après correction :

- listes : **fragile, retravaillées aujourd’hui** ;
- dictionnaires : **fragile, retravaillés aujourd’hui** ;
- boucles et conditions : **fragiles, à consolider** ;
- paramètres et valeur de retour : **fragiles** ;
- distinction `return` / `print` : **fragile** ;
- pseudo-code algorithmique : **fragile, exercice guidé aujourd’hui** ;
- fichiers, `pathlib` et Pillow : **mis en pause jusqu’à consolidation des fondamentaux**.

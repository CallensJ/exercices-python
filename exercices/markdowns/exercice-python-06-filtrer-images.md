# Exercice Python 06 — Filtrer des fichiers image

## Contexte

Tu continues à construire les bases nécessaires pour ton futur outil desktop de traitement d’images.

Pour cet exercice, **aucune nouvelle notion avancée**.

Le but est de réutiliser ce que tu as déjà vu :

- listes ;
- dictionnaires ;
- boucles `for` ;
- conditions `if` ;
- fonctions ;
- chaînes de caractères ;
- méthodes simples comme `.lower()` et `.endswith()`.

On ne touche pas encore aux fichiers réels sur le disque.  
Le chapitre sur les fichiers de *Python Crash Course* arrive plus tard, donc ici on travaille uniquement avec une liste de noms de fichiers.

---

## Objectif

Créer une fonction :

```python
filter_images(files)
```

Cette fonction reçoit une liste de noms de fichiers et retourne uniquement les fichiers qui sont des images compatibles.

Extensions acceptées :

- `.jpg`
- `.jpeg`
- `.png`
- `.webp`

---

## Données de départ

Crée un fichier `data.py` contenant :

```python
files = [
    "photo_vacances.jpg",
    "document.pdf",
    "logo.PNG",
    "notes.txt",
    "portrait.jpeg",
    "banner.webp",
    "archive.zip",
    "capture.JPG",
]
```

---

## Résultat attendu

Ta fonction doit retourner :

```python
[
    "photo_vacances.jpg",
    "logo.PNG",
    "portrait.jpeg",
    "banner.webp",
    "capture.JPG",
]
```

Attention : les extensions peuvent être écrites en majuscules ou en minuscules.

---

## Contraintes

Tu dois :

1. créer une fonction `filter_images(files)` ;
2. créer une liste vide pour stocker les images valides ;
3. parcourir `files` avec une boucle `for` ;
4. vérifier l’extension de chaque fichier ;
5. ajouter les fichiers compatibles dans la nouvelle liste ;
6. retourner cette liste avec `return`.

Tu ne dois pas utiliser :

- `filter()` ;
- les list comprehensions ;
- de bibliothèque externe ;
- de manipulation de vrais fichiers ou dossiers.

Le but est de pratiquer les fondamentaux, pas de convoquer la sorcellerie compacte de Python avant de comprendre ce qu’elle cache.

---

## Structure conseillée

```text
exercice_06/
│
├── data.py
├── filter_images.py
└── main.py
```

---

## Travail demandé

### Étape 1 — Français simple

Avant d’écrire du Python, réponds à cette question :

> Quelles sont les étapes nécessaires pour prendre une liste de fichiers et ne conserver que les images ?

Écris entre **4 et 7 étapes maximum**.

Exemple de niveau de détail attendu :

```text
Créer une liste vide.
Parcourir les fichiers.
...
```

Ne cherche pas à écrire du “beau pseudo-code” immédiatement.

---

### Étape 2 — Pseudo-code

Transforme ensuite tes étapes en pseudo-code avec cette structure :

```text
DEBUT

...

FIN
```

Tu peux utiliser :

```text
POUR CHAQUE
SI
AJOUTER
RETOURNER
```

---

### Étape 3 — Python

Écris ensuite la fonction dans `filter_images.py`.

Dans `main.py` :

1. importe `files` depuis `data.py` ;
2. importe `filter_images` ;
3. appelle la fonction ;
4. affiche le résultat.

---

## Indice 1

Tu peux transformer temporairement un nom de fichier en minuscules :

```python
filename.lower()
```

Ainsi :

```python
"PHOTO.JPG".lower()
```

devient :

```python
"photo.jpg"
```

---

## Indice 2

Une chaîne de caractères possède la méthode :

```python
.endswith()
```

Exemple :

```python
filename.endswith(".jpg")
```

renvoie `True` si la chaîne se termine par `.jpg`.

---

## Bonus facultatif

Seulement après avoir terminé l’exercice principal :

Compte combien d’images valides ont été trouvées et affiche par exemple :

```text
5 images trouvées
```

Ne fais pas le bonus tant que la version principale n’est pas terminée.

---

## Ce que cet exercice entraîne réellement

Cet exercice ne cherche pas à t’apprendre une nouvelle fonctionnalité Python.

Il entraîne surtout :

- la décomposition d’un problème ;
- le passage du français au pseudo-code ;
- le passage du pseudo-code au Python ;
- la répétition des listes, boucles, conditions et fonctions ;
- la lecture d’une méthode simple sur une chaîne.

Ces bases doivent devenir naturelles avant de complexifier le projet.

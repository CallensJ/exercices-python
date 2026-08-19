# Exercice Python 05 — Lister les images d’un dossier

## Contexte

Tu démarres le cœur de **WebAsset Optimizer**, une future application desktop open source qui servira à convertir et optimiser des images pour le web.

Avant de transformer une image, le programme doit savoir trouver les fichiers image dans un dossier. C’est exactement l’objectif d’aujourd’hui.

> Pour cet exercice, on n’utilise pas encore Pillow et on ne convertit rien. On travaille seulement les chemins et le filtrage de fichiers avec `pathlib`.

## Objectif

Créer une fonction `list_images(folder_path)` qui reçoit le chemin d’un dossier et retourne une liste des fichiers image présents directement dans ce dossier.

Les extensions acceptées sont : `.jpg`, `.jpeg`, `.png`, `.webp`.

L’extension doit être reconnue même si elle contient des majuscules : `PHOTO.JPG` doit être accepté.

## Arborescence demandée

Crée un dossier `exercice-python-05` avec ces fichiers :

```text
exercice-python-05/
├── image_scanner.py
└── main.py
```

## Données de test

Crée aussi un dossier de test avec quelques fichiers factices :

```text
exercice-python-05/
├── test_assets/
│   ├── hero.jpg
│   ├── logo.PNG
│   ├── portrait.jpeg
│   ├── old-image.webp
│   ├── notes.txt
│   └── document.pdf
├── image_scanner.py
└── main.py
```

Ces fichiers peuvent être vides : leur contenu n’a aucune importance aujourd’hui. Tu peux les créer dans Zed.

## Contraintes

Dans `image_scanner.py` :

- importe `Path` depuis `pathlib` ;
- définis une constante `IMAGE_EXTENSIONS` contenant les extensions autorisées ;
- crée `list_images(folder_path)` ;
- transforme `folder_path` en objet `Path` ;
- parcours les éléments du dossier ;
- garde seulement les fichiers, puis seulement ceux dont l’extension est autorisée ;
- retourne la liste des chemins retenus.

Dans `main.py` :

- importe `list_images` ;
- appelle la fonction avec le dossier `test_assets` ;
- affiche chaque image trouvée, une par ligne.

## Résultat attendu

Le programme doit afficher les quatre images, sans les fichiers `.txt` ni `.pdf` :

```text
test_assets/hero.jpg
test_assets/logo.PNG
test_assets/old-image.webp
test_assets/portrait.jpeg
```

L’ordre exact peut varier selon ton système. Ce n’est pas un bug.

## Pseudo-code à écrire avant de coder

```text
FONCTION list_images(folder_path)
    convertir folder_path en objet Path
    créer une liste vide images

    POUR chaque element du dossier
        SI element est un fichier
            recuperer son extension en minuscules
            SI cette extension est dans IMAGE_EXTENSIONS
                ajouter element à images

    retourner images
```

## Indices (à ouvrir seulement si tu bloques)

<details>
<summary>Indice 1 — créer un chemin</summary>

```python
folder = Path(folder_path)
```
</details>

<details>
<summary>Indice 2 — parcourir un dossier</summary>

```python
for item in folder.iterdir():
    print(item)
```
</details>

<details>
<summary>Indice 3 — vérifier fichier et extension</summary>

```python
item.is_file()
item.suffix.lower()
```
</details>

## Critères de validation

- [ ] `Path` est importé depuis `pathlib`.
- [ ] `IMAGE_EXTENSIONS` contient les quatre extensions attendues.
- [ ] `list_images()` retourne une liste, elle ne se contente pas d’afficher.
- [ ] Les fichiers non-image sont exclus.
- [ ] Les extensions en majuscules sont acceptées.
- [ ] `main.py` est chargé seulement d’appeler et d’afficher le résultat.

## Règle du jeu

Fais d’abord ton pseudo-code, puis une première tentative complète. Même imparfaite. Ensuite tu m’envoies `image_scanner.py` et `main.py` : je corrige le raisonnement, pas seulement les virgules.

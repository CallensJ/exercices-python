# Exercice Python 07 — Lire les métadonnées d’une image

## Énoncé

**WebAsset Optimizer** devra afficher des informations sur chaque image avant de la convertir. Pour cette première utilisation de Pillow, écris une fonction `get_image_metadata(image_path)` qui ouvre une image et retourne ses principales métadonnées.

La fonction doit retourner un dictionnaire contenant exactement ces clés :

- `name` : nom du fichier avec son extension ;
- `format` : format détecté dans le contenu de l’image ;
- `width` : largeur en pixels ;
- `height` : hauteur en pixels ;
- `mode` : mode colorimétrique de l’image ;
- `size_bytes` : poids du fichier en octets.

Avant de coder, rédige obligatoirement un pseudo-code structuré entre `DEBUT` et `FIN`. Identifie clairement l’entrée, les opérations et la valeur retournée.

## Données de départ

Installe Pillow dans l’environnement virtuel de ton projet :

```bash
python -m pip install Pillow
```

Crée ensuite un dossier `sample_images` et places-y :

- une véritable image PNG ;
- une véritable image JPG ou JPEG.

N’utilise pas de fichier vide : Pillow doit pouvoir lire le contenu réel de l’image.

Organisation minimale :

```text
webasset-optimizer/
├── sample_images/
│   ├── exemple.png
│   └── photo.jpg
├── image_metadata.py
└── main.py
```

## Contraintes

- Utilise `pathlib.Path` pour manipuler le chemin et récupérer le poids du fichier.
- Utilise Pillow uniquement pour ouvrir l’image et lire ses propriétés.
- La fonction doit accepter une chaîne de caractères ou un objet `Path`.
- La fonction doit retourner un dictionnaire, pas afficher elle-même le résultat.
- Place l’affichage uniquement dans `main.py`.
- Ouvre l’image avec un gestionnaire de contexte afin qu’elle soit correctement fermée après lecture.
- Le champ `format` doit provenir de Pillow, pas de l’extension du fichier.
- Les valeurs `width`, `height` et `size_bytes` doivent être des entiers.
- Ne convertis, ne redimensionne et ne modifie aucune image.
- Ne gère pas encore les fichiers inexistants ou invalides : la gestion d’erreurs fera l’objet d’un exercice séparé.
- N’ajoute aucune interface graphique.
- Ne copie pas de solution avant d’avoir produit ton pseudo-code et une tentative exécutable.

En JavaScript, un objet littéral et un dictionnaire Python jouent ici un rôle comparable. En Python, tu accéderas cependant aux informations de l’image à travers un objet fourni par Pillow, puis tu construiras explicitement le dictionnaire retourné.

## Résultat attendu

Un appel avec une image nommée `exemple.png` doit retourner une structure de cette forme, avec les vraies valeurs de ton fichier :

```text
{
    "name": "exemple.png",
    "format": "PNG",
    "width": 1200,
    "height": 800,
    "mode": "RGB",
    "size_bytes": 245678
}
```

Les nombres ci-dessus sont seulement illustratifs. Teste la fonction séparément avec ton PNG et ton JPG/JPEG, puis vérifie que le format retourné correspond bien au contenu de chaque image.

## Ce qui est évalué

- **Difficulté principale :** ouvrir une image avec Pillow et lire ses propriétés sans la modifier.
- Qualité du pseudo-code `DEBUT` → `FIN`.
- Utilisation conjointe de `Path` et de Pillow, chacun pour sa responsabilité.
- Construction et retour d’un dictionnaire cohérent.
- Séparation entre la logique métier dans `image_metadata.py` et l’affichage dans `main.py`.
- Fermeture propre de la ressource image.

Trace de progression à confirmer après correction :

- détection de fichiers avec `pathlib` : **première tentative fonctionnelle, consolidation en cours** ;
- paramètres et retours de fonction : **fragile, à consolider** ;
- pseudo-code algorithmique : **fragile** ;
- dictionnaires : **déjà travaillés, compréhension à confirmer** ;
- lecture d’image avec Pillow : **non acquise, introduite aujourd’hui** ;
- conversion et compression : **non acquises, pas encore abordées**.

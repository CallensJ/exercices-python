# Exercice Python 10 — Convertir une image en WebP

## Énoncé

Tu vas ajouter la première transformation réelle de **WebAsset Optimizer** : convertir une seule image PNG ou JPG/JPEG au format WebP.

Écris une fonction `convert_to_webp(input_path, output_path)` qui reçoit le chemin de l’image source et le chemin exact du fichier WebP à créer.

La fonction doit :

- ouvrir l’image source avec Pillow ;
- l’enregistrer au format WebP à l’emplacement demandé ;
- fermer correctement l’image ;
- retourner le chemin du fichier créé sous forme d’objet `Path`.

Avant de coder, réponds par écrit à ces cinq questions :

1. Quelles sont les deux entrées de la fonction ?
2. Quel objet faut-il créer à partir de chacun des deux chemins reçus ?
3. Quelle ressource doit être ouverte puis refermée ?
4. Quelle opération produit réellement le nouveau fichier ?
5. Quelle valeur la fonction doit-elle retourner ?

Transforme ensuite ces réponses en un pseudo-code court entre `DEBUT` et `FIN`. N’écris pas la syntaxe Python dans le pseudo-code.

## Données de départ

Réutilise l’environnement virtuel dans lequel Pillow est installé.

Prépare deux véritables images :

- `sample_images/photo.jpg` ;
- `sample_images/logo.png`.

Crée manuellement un dossier vide `output` avant de lancer le programme.

Organisation attendue :

```text
webasset-optimizer/
├── sample_images/
│   ├── photo.jpg
│   └── logo.png
├── output/
├── converter.py
└── main.py
```

Depuis `main.py`, effectue séparément ces deux conversions :

```text
sample_images/photo.jpg  -> output/photo.webp
sample_images/logo.png   -> output/logo.webp
```

## Contraintes

- Place la fonction dans `converter.py` et les appels dans `main.py`.
- Utilise `pathlib.Path` pour les deux chemins.
- La fonction doit accepter des chaînes de caractères ou des objets `Path`.
- Utilise Pillow pour ouvrir et enregistrer l’image.
- Ouvre l’image avec un gestionnaire de contexte afin qu’elle soit correctement fermée.
- Indique explicitement à Pillow que le format de sortie est WebP ; ne te fie pas uniquement à l’extension du nom.
- La fonction doit retourner l’objet `Path` correspondant au fichier créé.
- La fonction ne doit rien afficher.
- Affiche le chemin retourné uniquement depuis `main.py`.
- Le dossier `output` existe déjà : ne programme pas sa création aujourd’hui.
- Ne supprime, ne renomme et ne modifie jamais le fichier source.
- Ne règle pas encore la qualité de compression.
- Ne redimensionne pas l’image.
- Ne traite pas une liste ou un dossier complet.
- Ne gère pas encore les erreurs.
- N’ajoute ni AVIF, ni interface graphique, ni fonction IA.
- Consulte la documentation Pillow pour identifier la méthode d’enregistrement au lieu de chercher une solution complète à l’exercice.
- Ne copie pas de solution avant d’avoir écrit tes réponses, ton pseudo-code et une première tentative.

En JavaScript côté navigateur, la conversion d’image demanderait généralement une API comme Canvas ou une bibliothèque. Avec Pillow, l’image ouverte est un objet possédant ses propres opérations : observe cette logique objet, sans essayer de traduire mécaniquement du JavaScript.

## Résultat attendu

Après l’exécution de `main.py`, le dossier de sortie doit contenir :

```text
output/
├── logo.webp
└── photo.webp
```

Vérifie manuellement que :

- les deux fichiers WebP s’ouvrent correctement ;
- leur format détecté avec Pillow est `WEBP` ;
- les dimensions sont identiques à celles des sources ;
- les fichiers PNG et JPG d’origine existent toujours et n’ont pas changé de nom.

## Ce qui est évalué

- **Difficulté principale :** enregistrer avec Pillow une image ouverte dans un autre format.
- Qualité du raisonnement et du pseudo-code avant la tentative.
- Réutilisation de `Path` sans complexifier la construction des chemins.
- Utilisation correcte d’un gestionnaire de contexte.
- Respect de la séparation entre logique de conversion et affichage.
- Retour du chemin produit afin que le reste de l’application puisse l’utiliser plus tard.
- Vérification concrète du fichier généré, pas seulement absence d’erreur dans le terminal.

Trace de progression :

- filtrage de fichiers avec `pathlib` : **acquis sur un exercice, à consolider** ;
- lecture de métadonnées avec Pillow : **première réalisation fonctionnelle, en cours d’acquisition** ;
- recherche dans la documentation : **bonne démarche observée** ;
- pseudo-code : **fragile mais en progrès ; rédigé avant le code sur les exercices 06 et 07** ;
- paramètres et valeur de retour : **fragiles, encore travaillés aujourd’hui** ;
- conversion d’image : **non acquise, introduite aujourd’hui** ;
- qualité, redimensionnement et traitement par lot : **non acquis, pas encore abordés**.

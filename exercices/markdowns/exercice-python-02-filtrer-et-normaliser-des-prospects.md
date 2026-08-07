# Exercice Python 2 : filtrer et normaliser des prospects

Voici les données :

```python
prospects = [
    {
        "name": "  Boulangerie Martin ",
        "city": "NÎMES",
        "email": "CONTACT@MARTIN.FR",
        "active": True,
    },
    {
        "name": "Chez Luigi",
        "city": " alès ",
        "email": "",
        "active": True,
    },
    {
        "name": "Garage du Centre",
        "city": "Nîmes",
        "email": "garage@centre.fr ",
        "active": False,
    },
    {
        "name": "  Studio Nova",
        "city": "MONTPELLIER",
        "email": "hello@nova.fr",
        "active": True,
    },
]
```

Tu dois écrire une fonction :

```python
def prepare_prospects(prospects):
    ...
```

Elle doit retourner une **nouvelle liste** contenant uniquement les prospects :

- actifs ;
- ayant une adresse email non vide.

Chaque prospect retourné doit être normalisé ainsi :

- `name` : espaces supprimés au début et à la fin ;
- `city` : espaces supprimés, puis première lettre en majuscule ;
- `email` : espaces supprimés, puis texte en minuscules.

## Résultat attendu

```python
[
    {
        "name": "Boulangerie Martin",
        "city": "Nîmes",
        "email": "contact@martin.fr",
        "active": True,
    },
    {
        "name": "Studio Nova",
        "city": "Montpellier",
        "email": "hello@nova.fr",
        "active": True,
    },
]
```

## Contraintes

- Ne modifie pas la liste d’origine.
- N’utilise pas `pandas`.
- Utilise une boucle classique pour cette première version.
- Évite de mettre toute la logique dans une seule ligne.
- Donne un nom clair à chaque variable.
- Avant d’écrire le code, rédige ton pseudocode en 5 à 8 étapes maximum.

## Ce qui est évalué

- capacité à découper le problème ;
- manipulation de dictionnaires ;
- utilisation de `.strip()`, `.lower()` et `.capitalize()` ;
- création d’une nouvelle structure sans modifier l’originale ;
- clarté de la fonction.

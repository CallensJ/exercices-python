# Exercice Python 1 : nettoyer des prospects

Tu reçois cette liste brute :

```python
prospects = [
    {"name": "Pizza Roma", "city": "Nîmes", "email": " CONTACT@PIZZAROMA.FR "},
    {"name": "pizza roma", "city": "nîmes", "email": "contact@pizzaroma.fr"},
    {"name": "Chez Luigi", "city": "Alès", "email": ""},
    {"name": "Le Napoli", "city": "Nîmes", "email": "hello@lenapoli.fr"},
]
```

Écris une fonction :

```python
def clean_prospects(prospects):
    ...
```

Elle doit :

1. supprimer les espaces autour des chaînes ;
2. mettre les emails en minuscules ;
3. ignorer les prospects sans email ;
4. supprimer les doublons en considérant que deux prospects sont identiques lorsqu’ils ont le même nom et la même ville, sans tenir compte des majuscules ;
5. retourner une nouvelle liste sans modifier la liste d’origine.

## Résultat attendu

```python
[
    {
        "name": "Pizza Roma",
        "city": "Nîmes",
        "email": "contact@pizzaroma.fr"
    },
    {
        "name": "Le Napoli",
        "city": "Nîmes",
        "email": "hello@lenapoli.fr"
    }
]
```

## Contraintes

- Pas de bibliothèque externe.
- Pas de classe.
- Pas de `pandas`.
- Utilise au moins une fonction séparée pour construire la clé de déduplication.
- Avant de coder, écris ton raisonnement en pseudocode.

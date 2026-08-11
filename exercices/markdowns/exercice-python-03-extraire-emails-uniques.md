# Exercice Python 3 : extraire des emails uniques

Tu travailles sur une petite brique de `prospect_engine`.

Tu reçois une liste de prospects provenant de plusieurs sources. Certains n'ont pas d'email, certains emails contiennent des espaces, et certains apparaissent plusieurs fois avec des majuscules différentes.

```python
prospects = [
    {"name": "Pizza Roma", "email": " CONTACT@PIZZAROMA.FR "},
    {"name": "Boulangerie Martin", "email": "contact@martin.fr"},
    {"name": "Pizza Roma Nîmes", "email": "contact@pizzaroma.fr"},
    {"name": "Chez Luigi", "email": ""},
    {"name": "Garage du Centre", "email": " GARAGE@CENTRE.FR"},
    {"name": "Studio Nova", "email": None},
    {"name": "Garage Centre", "email": "garage@centre.fr "},
]
```

Écris une fonction :

```python
def extract_unique_emails(prospects):
    ...
```

La fonction doit :

1. parcourir tous les prospects ;
2. ignorer les emails vides ou égaux à `None` ;
3. supprimer les espaces au début et à la fin ;
4. convertir les emails en minuscules ;
5. ne conserver chaque email qu'une seule fois ;
6. retourner une liste contenant les emails uniques dans leur ordre de première apparition.

## Résultat attendu

```python
[
    "contact@pizzaroma.fr",
    "contact@martin.fr",
    "garage@centre.fr",
]
```

## Contraintes

- Utilise une boucle `for`.
- Utilise un `set` pour mémoriser les emails déjà rencontrés.
- Utilise également une `list` pour construire le résultat final.
- Ne modifie pas la liste `prospects`.
- N'utilise pas `pandas`.
- N'utilise pas de compréhension de liste pour cette version.
- La fonction doit retourner le résultat avec `return`.
- Avant d'écrire le code, rédige un pseudocode de 5 à 7 étapes maximum.

## Ce qui est évalué

- compréhension du rôle d'un `set` ;
- distinction entre « mémoriser ce qui a déjà été vu » et « construire le résultat à retourner » ;
- accès aux valeurs d'un dictionnaire ;
- gestion de `None` et des chaînes vides ;
- utilisation de `.strip()` et `.lower()` ;
- utilisation de `in` avec un `set` ;
- ajout dans une liste avec `.append()` ;
- ajout dans un `set` avec `.add()` ;
- capacité à expliquer pourquoi deux structures différentes sont utiles ici.

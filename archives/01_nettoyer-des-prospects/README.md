# 00 - Exemple

## Énoncé
soit le tableau suivant : 
```
prospects = [
    {"name": "Pizza Roma", "city": "Nîmes", "email": " CONTACT@PIZZAROMA.FR "},
    {"name": "pizza roma", "city": "nîmes", "email": "contact@pizzaroma.fr"},
    {"name": "Chez Luigi", "city": "Alès", "email": ""},
    {"name": "Le Napoli", "city": "Nîmes", "email": "hello@lenapoli.fr"},
]
``` 

Ecrire une fonction qui : 


supprimer les espaces autour des chaînes ;
mettre les emails en minuscules ;
ignorer les prospects sans email ;
supprimer les doublons en considérant que deux prospects sont identiques lorsqu’ils ont le même nom et la même ville, sans tenir compte des majuscules ;
retourner une nouvelle liste sans modifier la liste d’origine.

## Notes


def clean_prospects(prospects):

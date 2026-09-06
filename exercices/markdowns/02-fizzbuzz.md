# Exercice 02 — FizzBuzz

**Phase :** 1 — Fondamentaux de Python
**Concepts visés :** boucle `for`, `range()`, conditions `if`/`elif`/`else`, opérateur modulo `%`

## Contexte

Le FizzBuzz est l'exercice classique pour vérifier qu'on maîtrise l'enchaînement boucle + condition. C'est aussi mentionné explicitement dans ta roadmap comme premier exercice de la Phase 1.

## Objectif

Écris un script `fizzbuzz.py` qui parcourt les nombres de 1 à 100 et affiche, pour chaque nombre :

- `Fizz` si le nombre est divisible par 3
- `Buzz` si le nombre est divisible par 5
- `FizzBuzz` si le nombre est divisible à la fois par 3 et par 5
- le nombre lui-même sinon

## Contraintes

- Utilise `range()` pour générer la séquence de nombres.
- L'ordre des conditions dans ton `if/elif/else` a une importance — réfléchis à pourquoi.

## Piste de réflexion

- Quel opérateur Python permet de savoir si un nombre est divisible par un autre sans faire la division complète ?
- Si tu testes "divisible par 3" avant "divisible par 3 et 5", qu'est-ce qui se passe pour le nombre 15 ?

## Bonus (facultatif)

Une fois que ça fonctionne, essaie de réécrire la logique avec une seule condition combinée (`and`) au lieu de trois blocs séparés, pour voir si le code est plus lisible ou moins.

## Critère de validation

Le script affiche exactement 100 lignes, avec `Fizz`, `Buzz`, `FizzBuzz` et les nombres aux bons endroits (par exemple ligne 15 = `FizzBuzz`, ligne 3 = `Fizz`, ligne 5 = `Buzz`, ligne 7 = `7`).

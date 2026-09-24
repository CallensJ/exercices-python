'''
Écrire un script `fizzbuzz.py` qui parcourt les nombres de 1 à 100 et affiche, pour chaque nombre :

- `Fizz` si le nombre est divisible par 3
- `Buzz` si le nombre est divisible par 5
- `FizzBuzz` si le nombre est divisible à la fois par 3 et par 5
- le nombre lui-même sinon
'''

# NOTES
# Un nombre est divisible par 3 si la somme de ses chiffres est elle-même divisible par 3.
# Un nombre entier est divisible par 5 si et seulement si son chiffre des unités est 0 ou 5.
#Un nombre entier est divisible par 3 et 5 s'il est divisible par leur plus petit commun multiple, soit 15.(  un nombre est divisible par 3 et 5 s'il se termine par 0 ou 5 et que la somme de ses chiffres est un multiple de 3)

#ALGORITHME
# DEBUT
# POUR chaque nombre de 1 à 100 => for nb in range(1, 101):
# VERIFIER si le nombre est divisible par 3 => nb isDivisibleBy3
# isDivisibleBy3 = nb % 3 == 0
# SI nb est divisible par 3 ALORS afficher `Fizz` FINSI
# VERIFIER si le nombre est divisible par 5 => nb isDivisibleBy5
# isDivisibleBy5 = nb % 5 == 0
#
# SI nb est divisible par 5 ALORS afficher `Buzz` FINSI
# VERIFIER si le nombre est divisible par 3 et 5 => nb isDivisibleBy3And5
# isDivisibleBy3And5 = nb % 3 == 0 and nb % 5 == 0
# SI nb est divisible par 3 et 5 ALORS afficher `FizzBuzz` FINSI
#FIN
#
#
#


for nb in range(1, 101):
    isDivisibleBy3 = nb % 3 == 0
    isDivisibleBy5 = nb % 5 == 0
    isDivisibleBy3And5 = nb % 3 == 0 and nb % 5 == 0
    if isDivisibleBy3And5:
        print("FizzBuzz")
    elif isDivisibleBy3:
        print("Fizz")
    elif isDivisibleBy5:
        print("Buzz")
    else:
        print(nb)

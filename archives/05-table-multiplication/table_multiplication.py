# Écrire un script `table_multiplication.py` qui :

# 1. Demande à l'utilisateur un nombre entier `n` (entre 1 et 20).
# 2. Affiche la table de multiplication de `n`, de `n × 1` jusqu'à `n × 10`.
# 3. Affiche ensuite une grille complète (tableau) des tables de multiplication de 1 à `n`, bien alignée en colonnes.
'''
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 10 = 30

'''
#Algorithme table_multiplication
# DEBUT
# Demander à l'utilisateur un nombre entier `n` => user_number, int , input
# POUR chaque nombre de 1 à `n`
#   AFFICHER la table de multiplication de ce nombre#   POUR chaque multiplicande de 1 à 10
#     AFFICHER le résultat de la multiplication
# FIN POUR
# FIN POUR
# FIN
#
num = int(input("Entrez un nombre entier entre 1 et 20 : "))
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")


for i in range(1, num + 1):
    for j in range(1, num):
        print(f"{i * j:4}", end="")  # :4 pour aligner les colonnes
    print()  # Saut de ligne après chaque table

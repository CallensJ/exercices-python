'''
1. Demande à l'utilisateur deux nombres (via `input()`).
2. Demande une opération parmi `+`, `-`, `*`, `/`.
3. Effectue le calcul correspondant.
4. Affiche le résultat avec un message clair:
   `Résultat de 4.0 + 2.0 = 6.0`

'''


#calculatrice
#
# Algorithme calculatrice
# DEBUT
# DEMANDER a l'utilisateur de saisir deux nombres: => n1, n2
# DEMANDER a l'utilisateur de saisir l'operation a effectuer: => op
# n1,n2 = int ou float ( 2 decimales)
# SI op == "+" ALORS
#   EFFECTUER l'operation: => n1 + n2
# SINON SI op == "-" ALORS
#   EFFECTUER l'operation: => n1 - n2
# SINON SI op == "*" ALORS
#   EFFECTUER l'operation: => n1 * n2
# SINON SI op == "/" ALORS
#   EFFECTUER l'operation: => n1 / n2
# FIN SI
# AFFICHER le resultat: => "le resultat de n1 op n2 est resultat"
# FIN


from calendar import c


def calculatrice():
    n1 = float(input("Saisissez le premier nombre: "))
    n2 = float(input("Saisissez le second nombre: "))
    op = str(input("Saisissez l'operation a effectuer: "))
    resultat = 0
    if op == "+":
        resultat = n1 + n2
    elif op == "-":
        resultat = n1 - n2
    elif op == "*":
        resultat = n1 * n2
    elif op == "/":
        resultat = n1 / n2
    print(f"le resultat de {n1} {op} {n2} est {resultat}")



calculatrice()

# Le script demande a l'utilisateur du sapin et affiche un sapin centré fait d'étoiles `*`,
# Algorithme xmax.py
# DEBUT
# AFFICHER "Entrez la hauteur du sapin" => hauteur_sapin
# SI hauteur_sapin EST SUPERIEUR a 0 ALORS
# POUR i DE 1 A hauteur_sapin => for in range()
# AFFICHER " " * (hauteur_sapin - i) + "*" * (2 * i - 1)
# FINSI
#
# FIN



hauteur_sapin = int(input("Entrez la hauteur du sapin: "))
#verifie si la hauteur du sapin est positive
if hauteur_sapin > 0:
    #RANGE = start,stop,step
    for i in range(1, hauteur_sapin + 1): #genere les nombres de 1 jusque hauteur_sapin
        print(" " * (hauteur_sapin - i) + "*" * (2 * i - 1))
        '''
            " " * (hauteur_sapin - i) # cree des espaces d'indentations
            `"*" * (2 * i - 1)` : crée un nombre impair d'étoiles. Pour `i=1` → 1 étoile, `i=2` → 3 étoiles, `i=3` → 5 étoiles, etc. Le `2*i - 1` garantit toujours un nombre impair, essentiel pour que chaque ligne soit centrée symétriquement (une étoile "au milieu" avec le même nombre de chaque côté).
        '''
else:
    print("Hauteur du sapin doit être supérieure à 0")

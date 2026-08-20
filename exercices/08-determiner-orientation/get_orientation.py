#fonction qui determine l'orientation d'une image a partir de sa hauteur et de sa largeur.
#
# Algorithme orientation()
#
# DEBUT
#   VERIFIER si les valeurs sont bien des nombres entiers positifs
#        SI LARGEUR > HAUTEUR ALORS
#         AFFICHER "Largeur x Hauteur => paysage"
#       SINON SI LARGEUR < HAUTEUR ALORS
#       AFFICHER "Largeur x Hauteur => portrait"
#      SINON SI LARGEUR = HAUTEUR ALORS
#      AFFICHER "Largeur x Hauteur => carré"
#  FIN SI
# FIN

def orientation(width, height):
    if width > height:
        return "landscape"
    elif width < height:
        return "portrait"
    else:
        return "square"

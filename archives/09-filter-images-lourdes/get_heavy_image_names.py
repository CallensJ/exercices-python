from .data import images
# fonction qui retourne une nouvelle liste contenant uniquement les noms des images dont le poids est strictement supérieur à la limite

#Algoritme" image_filter
# DEBUT
#   Initialiser nouvelle liste vide "heavy_image_names"
#  POUR chaque image dans la liste "images"
#   SI le poids de l'image est strictement supérieur à la limite
#    ALORS ajouter le nom de l'image à la liste "heavy_image_names"
#  FIN POUR
# RETOURNER la liste "heavy_image_names"
# FIN

def image_filter(images, max_size_kb):
    heavy_image_names = []
    for image in images:
        if image["size_kb"] > max_size_kb:
            heavy_image_names.append(image["name"])
    return heavy_image_names

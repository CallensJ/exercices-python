# fonction pour filtrer les donnes d'une liste et renvoie une nouvelle liste avec les elements qui respectent le critere de filtrage (images)
#
# algorithme filter_images
#
# DEBUT
#
#CREER nouvelle liste vide
#CREER une liste d'extensions d'images valides (jpg, jpeg, png, gif)
#POUR chaque fichier dans la liste de fichiers
#   SI le fichier se termine par une extension d'image valide minuscule ou majuscule
#       AJOUTER le fichier à la nouvelle liste
#   FIN SI
#   SINON continuer
# FIN POUR
# RENVOYER la nouvelle liste
# FIN


def filter_images(files):
    image_extensions_allowed = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
    filtered_files = []

    for file in files:
        if any(file.lower().endswith(ext) for ext in image_extensions_allowed):
            filtered_files.append(file)

    return filtered_files

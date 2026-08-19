#fonction qui lit les métadonnées d'une image et retourne un dictionnaire contenant les informations pertinentes.
from PIL import Image
from pathlib import Path

# ALGORITHM image_metadata
#
# DEBUT
#   CREER un nouveau dictionnaire vide pour stocker les metadonnees
#   CREER chemin vers l'image
#   CREER une liste d'extensions d'images valides
#
#
#   SI fichier est un fichier et son extension est dans la liste d'extensions valides ALORS
#    OUVRIR l'image avec PIL
#    AJOUTER name, format, width, height, mode,size_bytes dans le nouveau dictionnaire
#   SINON SI le fichier n'est pas une image, afficher message d'erreur et continuer
#   FINSI
#
#  RETOURNER le dictionnaire contenant les metadonnees
# FIN
#

def get_image_metadata(image_path):
    metadata = {}
    file_path = Path(image_path)
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

    extension = file_path.suffix.lower()
    if extension in valid_extensions:
                with Image.open(file_path) as img:
                    metadata = {
                        'name': file_path.name,
                        'format': img.format,
                        'width': img.width,
                        'height': img.height,
                        'mode': img.mode,
                        'size_bytes': file_path.stat().st_size
                    }
    else:
        print(f"Le fichier {file_path} n'est pas une image valide. Extension: {extension}")
    return metadata

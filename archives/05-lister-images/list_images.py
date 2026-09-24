#Fonction qui reçoit le chemin d’un dossier et retourne une liste des fichiers image présents directement dans ce dossier.

#creer la fonction list_images
# convertir le chemin en chemin absolu
# initialiser les extensions de fichiers images autorises
# Initialiser une liste vide pour stocker les fichiers images
# parcourir le dossier
# si le fichier est un image
    #recuperer son extension en minuscule
    # si l'extension est dans la liste des extensions autorisées
        # ajouter le fichier à la liste des images
        # retourner la liste des images

#PSEUDO-CODE
#DEBUT
# fonction image_scanner
# convertir
from pathlib import Path

folder = Path('test_assets')
def list_images(folder):
    IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.webp']
    images = []
    for file in folder.iterdir():
        if file.is_dir():
            continue
        if file.suffix.lower() in IMAGE_EXTENSIONS:
            images.append(file)
            print(file)
    return images

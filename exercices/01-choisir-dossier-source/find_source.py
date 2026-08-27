#Fonction qui demande le chemin d'un dossier, récupère les images du dossier et les affiche avec leur nom

#DEBUT algorithme find_source

#LIRE chemin_utilisateur depuis input()

#SI chemin_utilisateur existe
    #SI chemin_utilisateur est un dossier
        #CREER list vide images = []

        #POUR chaque item dans le dossier (interdir)
             #SI item est un fichier (is_file)
                 #extension = recuperer l'extension en minuscule

                 #SI extension EST .png OU .jpg OU .jpeg
                      #AJOUTER nom du fichier dans images
                 #FINSI
             #FINSI
        #FINPOUR

        #SI images est vide
            #AFFICHER "Aucune image trouvee dans ce dossier"
        #SINON
            #AFFICHER " Nombre d'images trouvees:" + nombre d'images

            #POUR chaque image dans images
                #AFFICHER nom de l'image
            #FINPOUR
        #FINSI

        #SINON

            #AFFICHER "Erreur:Ce chemin n'est pas un dossier"
            #ARRETE PROGRAMME
        #FINSI

    #SINON
        #AFFICHER "Erreur: le chemin n'existe pas"
        #ARRETER PROGRAMME
    #FINSI

    #FIN





from pathlib import Path


def find_source():
    # Récupérer le chemin et le convertir en objet Path
    chemin_utilisateur = input("Quel est le chemin vers le dossier ? ")
    folder = Path(chemin_utilisateur)  # ← Créer l'objet Path, pas le string !

    # Vérifier que le chemin existe
    if not folder.exists():
        print("Erreur: le chemin n'existe pas")
        return

    # Vérifier que c'est un dossier
    if not folder.is_dir():
        print("Erreur: Ce chemin n'est pas un dossier")
        return

    # Créer une liste vide pour les images
    images_list = []
    extensions = [".jpg", ".jpeg", ".png"]

    # Parcourir les fichiers du dossier
    for item in folder.iterdir():
        if item.is_file() and item.suffix.lower() in extensions:
            images_list.append(item.name)  #  Garder juste le nom, pas tout l'objet

    # Afficher les résultats
    if not images_list:
        print("Aucune image trouvée dans ce dossier")
    else:
        print(f"Nombre d'images trouvées: {len(images_list)}")
        for image in images_list:
            print(f"  - {image}")


# Appel de la fonction
if __name__ == "__main__":
    find_source()



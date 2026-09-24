#Recuperer la liste des prospects

#Preparer une fonction prepare_prospects() qui prend en parametre une liste de prospects et qui renvoie une liste de prospects nettoyés
# retourner une liste de prospects nettoyes
# espaces supprimes dans names
# espaces supprimés, puis première lettre en majuscule pour city
#  espaces supprimés, puis texte en minuscules pour email

# fonction prepare_prospects()
# DEBUT
#   initialiser une liste vide
#   Liste_vide = []
#   Pour chaque prospect dans la liste prospects
#       SI le prospect est actif ET possede un email
#     Nettoyer le prospect
#       name = prospect.name.strip()
#       city = prospect.city.strip().capitalize()
#       email = prospect.email.strip().lower()
#     Ajouter le prospect nettoyé à la liste vide
#       Liste_vide.append((name, city, email))
#   Retourner la liste vide
# FIN


def prepare_prospects(prospects):
    cleaned_prospects = []
    for prospect in prospects:
        if prospect["active"] and prospect["email"] not in ["", None]:
            name = prospect["name"].strip()
            city = prospect["city"].strip().capitalize()
            email = prospect["email"].strip().lower()
            cleaned_prospects.append({"name": name, "city": city, "email": email})
    return cleaned_prospects

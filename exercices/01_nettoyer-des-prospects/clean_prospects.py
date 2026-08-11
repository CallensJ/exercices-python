# fonction pour nettoyer la liste des prospects
#PSEUDO CODE :
#Creer une liste vide pour stocker les prospects nettoyes
#recuperer la liste des prospects du dictionnaire prospects dans data.py
#supprimer les espaces inutiles avec la methode strip()
# Mettre les emails en minuscules
#Si un prospect ne possede pas d'email, je continue
# Si deux prospects ont  le même nom et la même ville ALORS je supprime le doublon
# je retourne la liste nettoyee sans modifier la liste originale
#

from data import prospects

def build_deduplication_key(name, city):
    """Construit une clé comparable, insensible aux majuscules."""
    return f"{name.strip().lower()}|{city.strip().lower()}"


def clean_prospects(prospects):
    cleaned_prospects = []
    seen_keys = set()

    for prospect in prospects:
        name = prospect["name"].strip()
        city = prospect["city"].strip()
        email = prospect["email"].strip().lower()

        if email == "":
            continue

        key = build_deduplication_key(name, city)

        if key in seen_keys:
            continue

        seen_keys.add(key)

        cleaned_prospect = {
            "name": name,
            "city": city,
            "email": email,
        }

        cleaned_prospects.append(cleaned_prospect)

    return cleaned_prospects

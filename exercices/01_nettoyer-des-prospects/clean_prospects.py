from prospects import prospects
# ecrire une fonction qui permet de :
#     supprimer les espaces autour des chaînes ;
#     mettre les emails en minuscules ;
#     ignorer les prospects sans email ;
#     supprimer les doublons en considérant que deux prospects sont identiques lorsqu’ils ont le même nom et la même ville, sans tenir compte des majuscules ;
#     retourner une nouvelle liste sans modifier la liste d’origine.
#



#PSEUDOCODE
#
# 1 - utiliser une boucle for pour parcourir la liste des prospects
# 2 - utiliser la methode strip() pour supprimer les espaces autour des chaines
# 3 - Verifier si le prospect a un email (SI prospect.email nest pas vide ALORS utiliser la methode lower(). SI prospect.email est vide Alors passer au prochain prospect )
# 4 - creer une fonction pour verifier les doublons.


# FONCTION clean_prospects(prospects)

#     créer une liste vide pour stocker les prospects nettoyés
#     créer une collection vide pour mémoriser les doublons

#     POUR chaque prospect dans prospects

#         SI le prospect n'a pas d'email
#             passer au prospect suivant

#         nettoyer le nom
#         nettoyer la ville
#         nettoyer l'email
#         mettre l'email en minuscules

#         créer une clé unique avec le nom et la ville

#         SI cette clé existe déjà
#             passer au prospect suivant

#         mémoriser cette clé

#         créer un nouveau prospect avec les données nettoyées
#         ajouter ce nouveau prospect à la liste résultat

#     retourner la liste résultat
#
# FONCTION create_prospect_key(prospect)

    # récupérer le nom
    # récupérer la ville

    # nettoyer le nom et la ville
    # les mettre en minuscules

    # retourner une clé construite avec nom + ville
    #

def create_prospect_key(prospect):
    cleaned_name = prospect["name"].strip().lower()
    cleaned_city = prospect["city"].strip().lower()
    cleaned_email = prospect["email"].strip().lower()
    return f"{cleaned_name}_{cleaned_city}_{cleaned_email}"


def clean_prospects(prospects):
    #creer une liste pour stocker les prospects nettoyés
    cleaned_prospects = []
    #créer une collection vide pour mémoriser les doublons
    seen_keys = set()


    for prospect in prospects:
        #si le prospect n'a pas d'email passer au prochain prospect
        if not prospect["email"]:
            continue

        #nettoyer le nom
        cleaned_name = prospect["name"].strip()
        #nettoyer la ville
        cleaned_city = prospect["city"].strip()
        #nettoyer l'email et mettre en minuscules
        cleaned_email = prospect["email"].strip().lower()

        #creer une cle unique avec le nom et la ville
        prospect_key = create_prospect_key(cleaned_name, cleaned_city , cleaned_email)

        #si cette cle existe deja, passer au prochain prospect
        if prospect_key in seen_keys:
            continue
        # memoriser cette cle
        seen_keys.add(prospect_key)
        # créer un nouveau prospect avec les données nettoyées

    return cleaned_prospects

#Ecrire une fonction qui extrait les emails uniques d'une liste de prospects
#1 - initialiser une liste vide pour stocker les emails uniques
#    utiliser la methode set() pour memoriser les emails deja rencontrés
#2 - parcourir la liste de prospects
#3 - pour chaque prospect:
#    supprimer les espaces autour de l'email
#    mettre l'email en minuscule
#    ne conserver chaque email qu'une seule fois
# 4 - retourner la liste des emails uniques

#PSEUDOCODE
#
# fonction extract_unique_emails(prospects)
#     emails_uniques = []
#     emails_rencontres = set()
#     pour chaque prospect dans prospects:
#         recuperer l'email du prospect
#         si l'email est None ou vide:
#             continuer
#         email = prospect.strip().lower()
#         si email n'est pas dans emails_rencontres:
#             ajouter email à emails_uniques
#             ajouter email à emails_rencontres
#     retourner emails_uniques
# FIN

def extract_unique_emails(prospects):
    email_unique = []
    email_rencontres = set()
    for prospect in prospects:
        email = prospect["email"]
        if email is None or email == "":
            continue
        email = email.strip().lower()
        if email not in email_rencontres:
            email_unique.append(email)
            email_rencontres.add(email)
    return email_unique

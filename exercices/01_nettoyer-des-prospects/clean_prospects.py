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




# CORRECTION EXERCICE 01_nettoyer-des-prospects par chatgpt.
# NOTE : 1er exercice , nouveau langage, pas reussi a le terminer.
# feeling = frustration

# FONCTION create_prospect_key(name, city)

#     nettoyer le nom
#         supprimer les espaces autour
#         mettre en minuscules

#     nettoyer la ville
#         supprimer les espaces autour
#         mettre en minuscules

#     retourner une chaîne contenant :
#         nom nettoyé + ville nettoyée


# FONCTION clean_prospects(prospects)

#     créer une liste vide cleaned_prospects
#     créer un set vide seen_keys

#     POUR chaque prospect dans prospects

#         récupérer l'email

#         SI l'email est vide
#             passer au prospect suivant

#         nettoyer le nom
#         nettoyer la ville
#         nettoyer l'email
#         mettre l'email en minuscules

#         créer une clé unique à partir du nom et de la ville

#         SI cette clé est déjà dans seen_keys
#             passer au prospect suivant

#         ajouter la clé dans seen_keys

#         créer un nouveau dictionnaire avec :
#             le nom nettoyé
#             la ville nettoyée
#             l'email nettoyé

#         ajouter ce nouveau dictionnaire dans cleaned_prospects

#     retourner cleaned_prospects

from prospects import prospects


def create_prospect_key(name, city):
    """
    Crée une clé permettant d'identifier un prospect.

    Exemple :
    "Pizza Roma" + "Nîmes"
    devient
    "pizza roma_nîmes"
    """

    # On retire les espaces inutiles et on met en minuscules.
    # Cela permet de considérer :
    # "Pizza Roma" et "pizza roma"
    # comme étant le même nom.
    cleaned_name = name.strip().lower()
    cleaned_city = city.strip().lower()

    # On assemble le nom et la ville pour créer une valeur
    # permettant d'identifier le prospect.
    return f"{cleaned_name}_{cleaned_city}"


def clean_prospects(prospects):
    """
    Retourne une nouvelle liste de prospects nettoyés,
    sans modifier la liste originale.
    """

    # Cette liste contiendra les prospects valides et nettoyés.
    cleaned_prospects = []

    # Ce set sert à mémoriser les prospects déjà rencontrés.
    #
    # Exemple :
    # {"pizza roma_nîmes", "le napoli_nîmes"}
    #
    # Un set ne contient pas de doublons.
    seen_keys = set()

    # On parcourt chaque dictionnaire de la liste prospects.
    for prospect in prospects:

        # On récupère l'email du prospect.
        email = prospect["email"]

        # Si l'email est vide, on ignore ce prospect.
        #
        # strip() permet aussi de considérer "   " comme vide.
        if not email.strip():
            continue

        # On nettoie les différentes valeurs.
        cleaned_name = prospect["name"].strip()
        cleaned_city = prospect["city"].strip()

        # Pour l'email :
        # - strip() enlève les espaces
        # - lower() met l'adresse en minuscules
        cleaned_email = email.strip().lower()

        # On fabrique une clé permettant de détecter les doublons.
        #
        # Exemple :
        # Pizza Roma + Nîmes
        # -> pizza roma_nîmes
        prospect_key = create_prospect_key(
            cleaned_name,
            cleaned_city
        )

        # Si cette clé a déjà été rencontrée,
        # ce prospect est considéré comme un doublon.
        if prospect_key in seen_keys:
            continue

        # Si ce n'est pas un doublon,
        # on mémorise sa clé.
        seen_keys.add(prospect_key)

        # On crée un NOUVEAU dictionnaire.
        #
        # C'est important car l'exercice demande
        # de ne pas modifier la liste originale.
        cleaned_prospect = {
            "name": cleaned_name,
            "city": cleaned_city,
            "email": cleaned_email,
        }

        # On ajoute le prospect nettoyé à la liste finale.
        cleaned_prospects.append(cleaned_prospect)

    # Une fois tous les prospects parcourus,
    # on retourne la nouvelle liste.
    return cleaned_prospects


result = clean_prospects(prospects)

print(result)

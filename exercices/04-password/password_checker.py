'''
# validateur de robustesse de mot de passe
# - Au moins 8 caractères
# - Contient au moins une lettre majuscule
# - Contient au moins une lettre minuscule
# - Contient au moins un chiffre
'''


# Algorithme password_checker
# DEBUT
#     DEMANDER à l'utilisateur de saisir un mot de passe: user_password

#     # Vérifier la longueur du mot de passe
#     SI longueur(user_password) < 8 ALORS
#         AFFICHER "Le mot de passe doit contenir au moins 8 caractères"
#         RETOURNER À LA SAISIE
#     FIN SI

#     # Initialiser des drapeaux pour les critères
#     a_majuscule = FAUX
#     a_minuscule = FAUX
#     a_chiffre = FAUX

#     # Parcourir chaque caractère du mot de passe
#     POUR CHAQUE char DANS user_password FAIRE
#         SI char est une lettre majuscule ALORS
#             a_majuscule = VRAI
#         FIN SI

#         SI char est une lettre minuscule ALORS
#             a_minuscule = VRAI
#         FIN SI

#         SI char est un chiffre ALORS
#             a_chiffre = VRAI
#         FIN SI
#     FIN POUR

#     # Vérifier si tous les critères sont satisfaits
#     SI NON(a_majuscule) OU NON(a_minuscule) OU NON(a_chiffre) ALORS
#         AFFICHER "Le mot de passe doit contenir :"
#         SI NON(a_majuscule) ALORS
#             AFFICHER "- Au moins une lettre majuscule"
#         FIN SI
#         SI NON(a_minuscule) ALORS
#             AFFICHER "- Au moins une lettre minuscule"
#         FIN SI
#         SI NON(a_chiffre) ALORS
#             AFFICHER "- Au moins un chiffre"
#         FIN SI
#         RETOURNER À LA SAISIE
#     SINON
#         AFFICHER "Mot de passe valide !"
#     FIN SI
# FIN

#METHODE 1
# def password_checker():
#     while True:
#         user_password = input("Entrez votre mot de passe : ")
#         #verifie la longueur du mdp
#         if len(user_password) < 8:
#             print("Le mot de passe doit contenir au moins 8 caracteres. ")
#             continue
#
#         #initisalisation des flags
#         a_majuscule = False
#         a_minuscule = False
#         a_chiffre = False
#
#         #Verifier chaque caractere du mdp
#         for char in user_password:
#             if char.isupper():
#                 a_majuscule = True
#             elif char.islower():
#                 a_minuscule = True
#             elif char.isdigit():
#                 a_chiffre = True
#
#         if not a_majuscule or not a_minuscule or not a_chiffre:
#             if not a_majuscule:
#                 print("Le mot de passe doit contenir au moins une lettre majuscule.")
#             if not a_minuscule:
#                 print("Le mot de passe doit contenir au moins une lettre minuscule.")
#             if not a_chiffre:
#                 print("Le mot de passe doit contenir au moins un chiffre.")
#             continue
#         else:
#             print("Mot de passe valide !")
#             break
#
# password_checker()

#METHODE 2
#
def password_checker():
    #dictionnaire : description du critere -> fonction de test

    criteria = {
        "au moins 8 caracteres": lambda mdp: len(mdp) >= 8,
        "au moins une lettre majuscule": lambda mdp: any(char.isupper() for char in mdp),
        "au moins une lettre minuscule": lambda mdp: any(char.islower() for char in mdp),
        "au moins un chiffre": lambda mdp: any(char.isdigit() for char in mdp),
    }

    while True:
        user_password = input("Entrez votre mot de passe : ")
        errors = []

        #on parcours le dictionnaire des criteres
        for description, test in criteria.items():
            if not test(user_password):
                errors.append(description)

        if errors:
            print("Erreurs :")
            for error in errors:
                print(f"- {error}")
        else:
            print("Mot de passe valide !")
            break

password_checker()

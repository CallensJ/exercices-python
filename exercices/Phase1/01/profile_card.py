#
# // ── DÉCLARATION DES VARIABLES ──────────────────────────
# VARIABLES
#     prenom, nom          : CHAÎNE
#     saisie_age           : CHAÎNE
#     saisie_taille        : CHAÎNE
#     age                  : ENTIER
#     taille               : FLOAT
#     loisir               : CHAÎNE
#     loisirs              : LISTE
#     lieu_naissance       : TUPLE (CHAÎNE, ENTIER)
#     competences          : ENSEMBLE
#     profile              : DICTIONNAIRE
#     is_adult             : BOOLÉEN
#     age_en_mois          : ENTIER
#     annee_naissance      : ENTIER
#     i                    : ENTIER
# DÉBUT
#
#     // ── 1. SAISIE UTILISATEUR ──────────────────────────
#     ÉCRIRE "Votre prénom :"
#     LIRE prenom
#     ÉCRIRE "Votre nom :"
#     LIRE nom
#     ÉCRIRE "Votre âge :"
#     LIRE saisie_age
#     age ← CONVERTIR_EN_ENTIER(saisie_age)      // input() renvoie une chaîne
#     ÉCRIRE "Votre taille en mètres (ex : 1.78) :"
#     LIRE saisie_taille
#     taille ← CONVERTIR_EN_RÉEL(saisie_taille)  // conversion explicite
# // ── 2. LISTE DE LOISIRS ─────────────────────────────
#   loisirs ← LISTE_VIDE
#   POUR i ← 1 À 3 FAIRE
#       ÉCRIRE "Saisissez le loisir n°", i, ":"
#       LIRE loisir
#       AJOUTER(loisirs, loisir)
#   FINPOUR
#
# #  // ── 3. TUPLE : DONNÉE IMMUTABLE ────────────────────
#    ÉCRIRE "Votre ville de naissance :"
#    LIRE ville
#    ÉCRIRE "Code postal :"
#    LIRE code_postal
#    lieu_naissance ← (ville, code_postal)
#    // NB : ce tuple ne pourra jamais être modifié ensuite
#
# #  // ── 4. SET DE COMPÉTENCES ───────────────────────────
#    competences ← ENSEMBLE {"Python", "Git", "Python", "SQL"}
#    // "Python" est volontairement en double :
#    // le set l'élimine automatiquement
#
#    ÉCRIRE "Nombre de compétences :", CARDINAL(competences)   // affiche 3
#    SI "Python" ∈ competences ALORS
#        ÉCRIRE "Python présent une seule fois (doublon supprimé)"
#    FINSI
#
#
# #   // ── 5. DICTIONNAIRE ────────────────────────────────
#   profile ← DICTIONNAIRE_VIDE
#   profile["first_name"]  ← prenom
#   profile["last_name"]   ← nom
#   profile["age"]         ← age
#   profile["height"]      ← taille
#   profile["hobbies"]     ← loisirs
#   profile["birth_place"] ← lieu_naissance
#   profile["skills"]      ← competences

#   // ── 6. RÉSUMÉ FORMATÉ ─────────────────────────────
#     SI age ≥ 18 ALORS
#         est_majeur ← VRAI
#     SINON
#         est_majeur ← FAUX
#     FINSI
#
#     age_en_mois     ← age × 12
#     annee_naissance ← 2025 − age
#
#     ÉCRIRE "Bonjour, je m'appelle ", prenom, " ", nom,
#            ", j'ai ", age, " ans."
#     ÉCRIRE "Âge en mois : ", age_en_mois,
#            " — année de naissance approximative : ", annee_naissance
#     ÉCRIRE "Majeur ? ", est_majeur
#     ÉCRIRE "Loisirs : ", loisirs
#     ÉCRIRE "Lieu de naissance : ", lieu_naissance
#     ÉCRIRE "Compétences : ", competences

#     // ── 7. VÉRIFICATION DES TYPES ──────────────────────
#     ÉCRIRE "Type de prenom  : ", TYPE(prenom)     // chaîne
#     ÉCRIRE "Type de age     : ", TYPE(age)        // entier
#     ÉCRIRE "Type de taille  : ", TYPE(taille)     // réel
#     ÉCRIRE "Type de est_majeur : ", TYPE(est_majeur)  // booléen
#
# FIN



prenom = str(input("Votre prenom : "))
nom = str(input("Votre nom : "))
saisie_age = int(input("Votre age : "))
saisie_taille = float(input("Votre taille : "))

loisirs = []
for i in range(3):
    loisir = str(input(f"Votre loisir {i+1} : "))
    loisirs.append(loisir)


lieu_naissance = (str(input("Votre ville de naissance : ")),
                  int(input("Code postal : ")))


competences = set(["Python", "Git", "Python", "SQL"])
if "Python" in competences:
    print("Python présent une seule fois (doublon supprimé)")


profile = {
    "first_name": prenom,
    "last_name": nom,
    "age": saisie_age,
    "height": saisie_taille,
    "hobbies": loisirs,
    "birth_place": lieu_naissance,
    "skills": competences,
}

print(profile)


if saisie_age >= 18:
    is_adult = True
else:
    is_adult = False

age_in_months = saisie_age * 12
year_of_birth = 2025 - saisie_age
print(f"Bonjour, je m'appelle {prenom} {nom}, j'ai {saisie_age} ans.")
print(f"Âge en mois : {age_in_months} — année de naissance approximative : {year_of_birth} et mon lieu de naissance est {lieu_naissance}")
print(f"Mes compétences : {competences} et mes loisirs sont : {loisirs}")

print(f"Majeur ? {is_adult}")


print(f"Type de prenom : {type(prenom)}")
print(f"Type de age : {type(saisie_age)}")
print(f"Type de taille : {type(saisie_taille)}")
print(f"Type de est_majeur : {type(is_adult)}")

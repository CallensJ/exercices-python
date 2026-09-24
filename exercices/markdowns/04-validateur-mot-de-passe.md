# Exercice 04 — Validateur de mot de passe

**Phase :** 1 — Fondamentaux de Python
**Concepts visés :** chaînes de caractères, `len()`, opérateurs logiques (`and`/`or`/`not`), conditions, boucle `while`

## Contexte

Petit clin d'œil à ton objectif cybersécurité final : un validateur de robustesse de mot de passe est un exercice simple mais qui te fait manipuler des chaînes et des conditions combinées — deux briques indispensables pour la suite (Phase 8 notamment).

## Objectif

Écris un script `password_checker.py` qui demande un mot de passe à l'utilisateur et vérifie qu'il respecte ces règles :

- Au moins 8 caractères
- Contient au moins une lettre majuscule
- Contient au moins une lettre minuscule
- Contient au moins un chiffre

Le script doit afficher clairement quelles règles sont respectées et lesquelles ne le sont pas.

## Contraintes

- Ne pas encore utiliser le module `re` (expressions régulières) — ce n'est pas encore au programme. Utilise uniquement des méthodes de chaînes comme `.isupper()`, `.islower()`, `.isdigit()` combinées à une boucle ou aux fonctions `any()`/`all()` si tu les connais déjà (sinon boucle `for` classique sur les caractères).
- Le script doit reboucler et redemander un mot de passe tant que celui-ci n'est pas valide (utilise une boucle `while`).

## Piste de réflexion

- Comment parcourir chaque caractère d'une chaîne un par un ?
- Quelle méthode de chaîne permet de savoir si un caractère précis est une majuscule ? Une minuscule ? Un chiffre ?

## Bonus (facultatif)

Ajoute une règle supplémentaire : au moins un caractère spécial parmi `!@#$%^&*`.

## Critère de validation

Le script rejette systématiquement les mots de passe invalides en expliquant pourquoi, et accepte (en sortant de la boucle) un mot de passe qui respecte toutes les règles.

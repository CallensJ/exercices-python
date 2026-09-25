# Apprentissage Python — Développement Web & Sécurité Applicative

Dépôt centralisant mon apprentissage de Python, structuré autour d'une roadmap en phases progressives (voir [`roadmap/roadmap.md`](roadmap/roadmap.md)), orientée développement web (FastAPI en priorité, aperçu de Flask et Django) avec une phase finale de cybersécurité applicative web (OWASP Top 10, hardening).

## But du repo

J'apprends Python. Le rôle de Claude se limite strictement à :
- me fournir les exercices (énoncés dans `roadmap/PhaseN/exoX-phaseN.md`) ;
- me guider si je bloque, par indices progressifs, jamais en me donnant la solution directement, sauf si je la demande explicitement.

**Objectif** : Avoir un socle Python solide, une bonne maîtrise de FastAPI (et des bases de Flask/Django), et une compréhension pratique de la sécurité applicative web.

## Roadmap

La progression suit 6 phases, détaillées dans [`roadmap/roadmap.md`](roadmap/roadmap.md) :

| Phase | Sujet |
|---|---|
| 1 | Socle Python moderne (POO, exceptions, décorateurs, typage, tooling) & fondations HTTP |
| 2 | Flask — fondamentaux du micro-framework |
| 3 | Django — fondamentaux du framework full-stack |
| 4 | FastAPI — spécialisation principale (async, Pydantic, sécurité, architecture) |
| 5 | Industrialisation, déploiement & DevOps |
| 6 | Cybersécurité web & hardening applicatif (OWASP Top 10) |

## Structure

```
roadmap/
├── roadmap.md                  # Roadmap complète, détaillée phase par phase
├── Phase1/
│   ├── Phase1.md                # Titres des exercices de la phase + suivi de progression
│   ├── exo1-phase1.md           # Énoncé de l'exercice 1
│   ├── exo2-phase1.md           # Énoncé de l'exercice 2
│   └── ...
├── Phase2/
│   └── ...
└── ...
exercices/
└── <a organiser au fur et à mesure : un dossier par exercice avec le script Python correspondant>
```

Chaque phase a son propre dossier dans `roadmap/`. Le fichier `PhaseN.md` ne contient que la liste des titres d'exercices et une section `## Progression` (cases à cocher) que je mets à jour moi-même au fur et à mesure. Chaque énoncé détaillé est fourni par Claude dans son propre fichier `exoX-phaseN.md`.

## Convention

Pour chaque nouvel exercice de la roadmap :
1. Claude ajoute l'énoncé dans `roadmap/PhaseN/exoX-phaseN.md`.
2. Je code la solution dans `exercices/PhaseN/exoX-nom-court/`.
3. Une fois l'exercice validé, je coche la case correspondante dans `roadmap/PhaseN/PhaseN.md`.
4. Si je bloque plus de deux jours sur le même exercice ou la même notion, Claude ne complexifie pas la suite : il me donne un autre exercice sur le même thème pour consolider avant d'avancer.

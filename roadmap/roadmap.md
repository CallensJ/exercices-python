# Roadmap : Développeur Python Web & Cybersécurité Applicative (2026)

Cette feuille de route détaille l'apprentissage progressif, de niveau **Débutant à Expert**, pour devenir un **Développeur Web Python accompli**. Elle met l'accent sur **FastAPI** comme framework principal, couvre les **fondamentaux de Django et Flask**, et se termine par une **phase complète de cybersécurité applicative web**.

---

## 📍 Phase 1 : Socle Python Moderne & Fondations du Web (Débutant)

### 1.1 Langage Python Core (3.12+)
* **Syntaxe & Structures de Données** : Types primitifs, listes, tuples, dictionnaires, ensembles, compréhensions de listes/dict.
* **Programmation Orientée Objet (POO)** : Classes, attributs, méthodes, héritage, polymorphisme, encapsulage, métaclasses.
* **Gestion des Exceptions & Ressources** : Blocs `try/except/finally`, exceptions personnalisées, gestionnaires de contexte (`with`).
* **Fonctionnalités Avancées** : Décorateurs, générateurs, itérateurs, pattern matching (`match/case`).

### 1.2 Typage Statique & Outillage Modern (2026)
* **Type Hints** : Annotations de type systématiques (`Union`, `Optional`, `TypedDict`, Generics).
* **Analyse Statique** : Validation avec `mypy` ou `pyright`.
* **Linting & Formatage** : Adoption du linter ultra-rapide `Ruff` (remplaçant Flake8, Black et isort).
* **Gestion de Projet & Dépendances** : Utilisation de `pyproject.toml`, gestionnaires modernes `uv` ou `Poetry` (abandon progressif de `pip` brut).

### 1.3 Fondations du Web & Protocole HTTP
* **Protocole HTTP/HTTPS** : Structure des requêtes/réponses, méthodes HTTP (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`), codes de statut (2xx, 3xx, 4xx, 5xx), en-têtes (headers), cookies.
* **Formats de Données** : Manipulation du JSON, Query Parameters, Form Data, Multipart uploads.
* **Architecture Client-Serveur & REST** : Principes RESTful, conception d'endpoints, statelessness.

---

## 📍 Phase 2 : Flask — Fondamentaux du Micro-Framework (Intermédiaire)

### 2.1 Philosophie Micro-Framework & WSGI
* **Standard WSGI** : Comprendre le rôle de la passerelle serveur/application (WSGI vs ASGI).
* **Design Minimaliste** : Approche "Bring Your Own Architecture" de Flask.

### 2.2 Core Flask & Templating
* **Routage & Requêtes** : Décorateurs `@app.route()`, gestion des paramètres d'URL, objet global `request`.
* **Moteur Jinja2** : Rendu de templates, héritage HTML, filtres, échappement automatique anti-XSS.

### 2.3 Écosystème & Extensions Clés
* **Base de Données & ORM** : `Flask-SQLAlchemy` pour les requêtes BDD, migrations avec Alembic (`Flask-Migrate`).
* **Formulaires & Validation** : `Flask-WTF` / WTForms (validation côté serveur, jetons CSRF intégrés).
* **Gestion des Utilisateurs** : Authentification par session avec `Flask-Login` ou par token avec `Flask-JWT-Extended`.
* **Sécurisation de Base** :
  * En-têtes HTTP de sécurité avec `Flask-Talisman`.
  * Limitation de débit avec `Flask-Limiter`.
  * Inspection dynamique des requêtes avec `flaskapi-guard`.

---

## 📍 Phase 3 : Django — Fondamentaux du Framework Full-Stack (Intermédiaire)

### 3.1 Architecture MVT (Model-View-Template)
* **Philosophie "Batteries Incluses"** : Structure opinionnée du projet, conventions de nommage et d'organisation.
* **Routage & Vues** : Cartographie d'URL (`urls.py`), vues basées sur des fonctions (FBV) et sur des classes (CBV).

### 3.2 Django ORM & Base de Données
* **Modélisation** : Définition des modèles, relations (`ForeignKey`, `OneToOne`, `ManyToManyField`).
* **Migrations Automatisées** : Commandes `makemigrations` et `migrate`, gestion de l'évolution des schémas BDD.
* **Optimisation des Requêtes** : Prévention du problème N+1 avec `select_related` et `prefetch_related`.

### 3.3 Fonctionnalités Natives & Écosystème
* **Interface d'Administration** : Personnalisation du Django Admin pour la gestion de contenu et de données.
* **Authentification & Permissions** : Système `django.contrib.auth`, gestion des rôles, groupes et autorisations.
* **Django REST Framework (DRF)** :
  * Sérialiseurs (`Serializers` / `ModelSerializers`).
  * APIViews, GenericViews, `ViewSets` et `Routers`.
* **Nouveautés Django 6.0 (2026)** :
  * Tâches d'arrière-plan intégrées (*Built-in background tasks*).
  * Support natif de la Politique de Sécurité du Contenu (`ContentSecurityPolicyMiddleware`).
  * Async complet (views, ORM, middleware).

---

## 📍 Phase 4 : FastAPI — Mastery du Framework Asynchrone & APIs (Spécialisation Principale)

### 4.1 Architecture Asynchrone & Serveurs ASGI
* **Asynchronisme Python** : Programmation concurrente I/O-bound avec `async` et `await`, boucles d'événements (`asyncio`).
* **Serveurs ASGI** : Exécution de haute performance avec Uvicorn et Gunicorn.

### 4.2 Validation de Données Stricte avec Pydantic V2
* **Modèles Pydantic** : Déclaration des schémas d'entrée et de sortie, parsing automatique, typage fort.
* **Performance V2** : Utilisation du moteur Pydantic Core écrit en Rust (5x plus rapide).
* **Validation Avancée** : Annotations `Field`, validateurs personnalisés, `Settings` pour la configuration applicative.

### 4.3 Injection de Dépendances (`Depends`) & BDD Async
* **Système de Dépendances** : Réutilisation de logique (authentification, vérification des rôles, transactions BDD).
* **ORM Async Moderne** : Intégration de `SQLAlchemy 2.x` (mode async) ou `SQLModel`.
* **Gestion des Sessions BDD** : Context managers asynchrones, pooling de connexions PostgreSQL.

### 4.4 Sécurité Intégrée & Documentation Automatique
* **Flux OAuth2 & JWT** : Utilisation de `OAuth2PasswordBearer`, génération et vérification des jetons JWT.
* **Gestion des Portées (Scopes)** : Contrôle d'accès fin avec `Security(get_current_user, scopes=[...])`.
* **OpenAPI & Swagger** : Documentation interactive générée automatiquement (`/docs` et `/redoc`).

### 4.5 Architectures Avancées & Frontend Léger
* **Découpage Modulaire** : Structuration d'applications à grande échelle avec `APIRouter`.
* **Tâches Asynchrones Légères & In-depth** : `BackgroundTasks` natives et intégration de Celery / Redis / RabbitMQ.
* **Arch Web Moderne "Python + HTMX"** :
  * Rendu de fragments HTML côté serveur via Jinja2 + FastAPI.
  * Alternative performante évitant la sur-ingénierie des SPA React/Next.js pour les dashboards et outils internes.

---

## 📍 Phase 5 : Industrialisation, Déploiement & DevOps (Avancé)

### 5.1 Containerisation & Orchestration
* **Docker pour Python** : Multi-stage builds avec images légères (`python:3.13-slim`), exécution sous utilisateur non-root, cache Docker optimisé.
* **Orchestration** : `docker-compose` pour les environnements locaux/staging, notions Kubernetes (Deployments, Services, Ingress).

### 5.2 Production BDD & Caching
* **Bases de Données Relationnelles** : PostgreSQL en production, pooling de connexions (`CONN_MAX_AGE`, PgBouncer).
* **Caching Distribué** : Invalidation et stockage de cache avec Redis.

### 5.3 CI/CD & Assurance Qualité
* **GitHub Actions** : Workflows de test, linters (`Ruff`), type-checkers (`mypy`), audits de sécurité (`pip-audit`).
* **Suite de Tests Pytest** :
  * Tests unitaires et d'intégration avec `pytest` et `pytest-asyncio`.
  * Mocks, fixtures, couverture de code (`pytest-cov` >= 80%).

### 5.4 Observabilité & Monitoring
* **Traces Distribuées & Métriques** : Intégration OpenTelemetry, exportation vers Prometheus / Grafana.
* **Logs Structurés** : Formatting JSON pour la centralisation des logs (Loki / ELK).

---

## 📍 Phase 6 : Cybersécurité Web & Hardening Applicatif (Expert Security)

### 6.1 Maîtrise des Risques OWASP Top 10 (Édition 2025/2026)

1. **Broken Access Control (BOLA / IDOR)** :
   * Risque : Accès ou modification d'objets sans vérification d'appartenance (ex: `/api/invoices/123`).
   * Réponse : Implémenter impérativement des contrôles d'accès au niveau objet (*Object-Level Authorization*) dans le service ou la vue en vérifiant la propriété (`user_id` / `tenant_id`).

2. **Security Misconfiguration (Erreurs de Configuration)** :
   * Risque : Mode `DEBUG = True` en production, exposition d'interfaces d'admin/OpenAPI publiques, ports BDD exposés.
   * Réponse : `DEBUG = False`, restriction des hôtes autorisés (`ALLOWED_HOSTS` / `TRUSTED_HOSTS` / `TrustedHostMiddleware`), masquage des schémas OpenAPI sensibles en production, isolation réseau Docker.

3. **Software Supply Chain Failures (Chaîne d'Approvisionnement)** :
   * Risque : Dépendances Python obsolètes ou compromises (ex: attaques par typosquatting sur PyPI).
   * Réponse : Verrouillage strict des versions (`uv.lock`, `poetry.lock`), audits continus avec `pip-audit` ou `Snyk` dans la CI/CD.

4. **Cryptographic Failures (Défaillances Cryptographiques)** :
   * Risque : Mots de passe mal hachés, secrets en dur dans le code.
   * Réponse : Hachage mémoire-difficile (`Argon2` via `argon2-cffi` ou `bcrypt`), gestion centralisée des secrets (`Pydantic Settings`, Vault, AWS Secrets Manager), HTTPS/TLS obligatoire avec HSTS.

5. **Injections (SQL, XSS, SSRF, Command Injection)** :
   * **SQL Injection** : Utilisation stricte des ORM paramétrés. Interdiction de la concaténation de chaînes brutes ou d'injection dynamique de dictionnaires dans les clauses de filtres/tri.
   * **XSS (Cross-Site Scripting)** : Échappement automatique dans Jinja2/Django Templates, évitement des filtres `mark_safe` ou `|safe`, mise en place de Content Security Policy (CSP).
   * **SSRF (Server-Side Request Forgery)** : Validation stricte des URL fournies par les utilisateurs, listes blanches de domaines autorisés, désactivation des redirections automatiques.

6. **Insecure Design & Threat Modeling** :
   * Risque : Défaut de conception sécurisée dès l'architecture initiale.
   * Réponse : Modélisation des menaces, principe du moindre privilège, "Deny by Default".

7. **Authentication Failures (Échecs d'Authentification)** :
   * Risque : Attaques par force brute, réutilisation de mots de passe.
   * Réponse : Intégration de MFA / Passkeys, limitation de débit (*Rate Limiting*), gestion sécurisée des cookies de session (`HttpOnly`, `Secure`, `SameSite=Lax`).

8. **Software & Data Integrity Failures** :
   * Risque : Altération de données en transit ou de bibliothèques CDN.
   * Réponse : Subresource Integrity (SRI) sur les scripts CDN, validation des signatures de jetons JWT.

9. **Security Logging & Alerting Failures** :
   * Risque : Absence de traçabilité en cas d'intrusion.
   * Réponse : Journalisation de tous les événements de sécurité (échecs et succès d'authentification/autorisation) avec horodatage et ID utilisateur.

10. **Mishandling of Exceptional Conditions (Mauvaise Gestion des Exceptions)** :
    * Risque : Blocs `try/except: pass`, fuites de stack trace ou états incohérents en BDD.
    * Réponse : Gestion explicite des exceptions, utilisation de transactions atomiques BDD, masquage des détails internes aux utilisateurs.

### 6.2 Outils de Hardening & Inspection Dynamique
* **Limitation de Débit (Rate Limiting)** : Protection des routes sensibles avec `slowapi` (FastAPI) ou `Flask-Limiter` / `django-ratelimit`.
* **Inspection Applicative Avancée** :
  * Utilisation de modules d'inspection de requêtes comme `fastapi-guard`, `djapi-guard` ou `flaskapi-guard` pour intercepter et bloquer automatiquement les tentatives d'injections SQL/XSS, traversées de répertoires (`../`), et scanners automatisés.
* **Configuration des En-têtes HTTP de Sécurité** :
  * Enforcement de `Strict-Transport-Security` (HSTS), `Content-Security-Policy` (CSP), `X-Frame-Options` (anti-clickjacking), `X-Content-Type-Options: nosniff`.
  * Utilisation de `Flask-Talisman` (Flask) ou `ContentSecurityPolicyMiddleware` (Django 6.0).
* **Audits & Tests de Pénétration (DevSecOps)** :
  * Analyse statique avec `Bandit` et `Corgea` / `Snyk`.
  * Tests d'API automatisés avec des scannables d'injections et fuzzer OWASP ZAP / Escape.

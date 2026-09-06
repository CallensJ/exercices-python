# Guide de Préparation aux Entretiens Techniques Python - Cybersécurité et Architecture

Ce document propose un ensemble de questions techniques, de snippets de code à analyser, de problèmes algorithmiques classiques et une simulation complète d'entretien. Il est conçu pour valider les compétences Python depuis les concepts fondamentaux jusqu'aux usages professionnels et à la spécialisation en cybersécurité, conformément aux sources de ce Notebook [1, 2, 3, 4, 5, 6, 7, 8].

---

## 1. Questions Techniques par Niveau

### Niveau : Junior

#### Question 1 : Comment sont définis les blocs de code en Python et quel est l'impact de l'indentation ?
*   **Réponse attendue** : Contrairement à de nombreux langages qui utilisent des accolades `{}` ou des mots-clés (`begin`/`end`), Python utilise l'**indentation** (les espaces ou tabulations en début de ligne) pour délimiter les blocs d'instructions [94, 129, 143]. Un nouveau bloc commence lorsqu'une ligne est plus indentée que la précédente, et se termine par un retour à un niveau d'indentation inférieur (appelé désindentation) [94, 126, 129]. La convention recommandée (PEP 8) est d'utiliser **4 espaces** par niveau d'indentation [13].
*   **Ce que cherche à vérifier l'interpréteur/l'intervieweur** : L'intervieweur veut s'assurer que le candidat comprend la syntaxe visuelle de Python, l'importance des espaces, et qu'il évite les erreurs classiques de type `IndentationError` lors du mélange d'espaces et de tabulations [2, 13, 94].

#### Question 2 : Quelle est la différence fondamentale entre une Liste (`list`) et un Tuple (`tuple`) ?
*   **Réponse attendue** : La différence majeure réside dans la **mutabilité** [111]. Une liste est **mutable** (on peut modifier, ajouter ou supprimer ses éléments après création avec des méthodes comme `.append()` ou `.pop()`) [2, 3, 111]. Un tuple est **immutable** (une fois créé, sa taille et ses éléments ne peuvent plus être modifiés) [111]. En conséquence, les listes sont stockées dans deux blocs de mémoire distincts (un pour l'enveloppe de l'objet et un pour les éléments réels, ce qui permet un redimensionnement dynamique), tandis que les tuples sont alloués en un seul bloc de mémoire fixe, ce qui les rend plus légers et légèrement plus rapides en accès [110, 111].
*   **Ce que cherche à vérifier l'intervieweur** : La compréhension de la gestion mémoire, de l'intégrité des données (utiliser un tuple pour s'assurer que des constantes ne soient pas modifiées par erreur), et de l'aptitude à choisir la bonne structure selon le cas d'usage [3, 111, 112].

#### Question 3 : Comment fonctionne la portée (scope) des variables en Python et comment utiliser le mot-clé `global` ?
*   **Réponse attendue** : Python gère la portée des variables selon la règle **LEGB** : *Local* (définie dans une fonction), *Enclosing* (dans une fonction englobante pour les closures), *Global* (au niveau du module), et *Built-in* (les fonctions natives du langage) [5, 120, 127]. Une variable locale n'existe que pendant l'exécution de sa fonction [120]. Si l'on souhaite modifier la valeur d'une variable globale depuis l'intérieur d'une fonction, Python lèvera une erreur ou créera une variable locale de même nom si l'on ne déclare pas explicitement la variable globale avec le mot-clé `global` au début de la fonction [111, 118, 121].
*   **Ce que cherche à vérifier l'intervieweur** : La maîtrise de l'isolation du code, de l'espace de noms (namespaces), et la capacité à éviter les effets de bord indésirables liés à l'utilisation non contrôlée de variables globales [5, 95, 127].

#### Question 4 : Expliquez le fonctionnement des exceptions et le rôle des clauses `else` et `finally`.
*   **Réponse attendue** : La gestion des exceptions en Python utilise un bloc `try/except` [2, 5, 13, 121]. 
    *   Le code à exécuter est placé dans le bloc `try` [121].
    *   Si une exception survient, l'exécution du bloc `try` s'interrompt et le contrôle passe au bloc `except` correspondant pour la traiter [5, 121].
    *   La clause optionnelle `else` est exécutée **uniquement si aucune exception** n'a été levée dans le bloc `try` [104].
    *   La clause `finally` est exécutée **dans tous les cas**, qu'une exception ait été levée, capturée, ou non, et même si une instruction `return` est rencontrée [112]. Elle est indispensable pour la libération propre de ressources (comme fermer un fichier ou une socket) [112].
*   **Ce que cherche à vérifier l'intervieweur** : La rigueur dans le traitement des erreurs, la capacité à écrire du code robuste qui ne crashe pas de manière inattendue, et le respect des patterns d'allocation/libération des ressources [13, 112, 121].

---

### Niveau : Intermédiaire

#### Question 5 : À quoi servent les paramètres `*args` et `**kwargs` dans la définition d'une fonction ?
*   **Réponse attendue** : Ils permettent de définir des fonctions qui acceptent un nombre variable d'arguments [70]. 
    *   `*args` récupère les arguments positionnels supplémentaires sous la forme d'un **tuple** [70].
    *   `**kwargs` récupère les arguments nommés supplémentaires sous la forme d'un **dictionnaire** [70].
    Ils sont extrêmement utiles pour écrire des fonctions génériques, des wrappers ou pour transférer dynamiquement des arguments à une autre fonction sous-jacente (par exemple dans l'héritage ou dans des décorateurs) [70, 72].
*   **Ce que cherche à vérifier l'intervieweur** : La maîtrise de la flexibilité des fonctions, de l'unpacking d'arguments, et de l'écriture d'interfaces API internes robustes et réutilisables [10, 70, 74].

#### Question 6 : Quelle est la différence entre les méthodes spéciales `__str__` et `__repr__` ?
*   **Réponse attendue** :
    *   `__str__` est conçue pour produire une représentation textuelle de l'objet qui soit **lisible et conviviale** pour l'utilisateur final [108, 109, 113]. Elle est appelée par la fonction `print()` ou `str()` [109].
    *   `__repr__` est conçue pour donner une représentation **non ambiguë** et souvent exécutable de l'objet, principalement destinée aux développeurs et au débogage (appelée dans l'interpréteur interactif ou par `repr()`) [108, 109, 113]. La règle générale est que, si possible, `repr(obj)` devrait retourner une chaîne qui permet de reconstruire l'objet via `eval(repr(obj))` [108, 113].
*   **Ce que cherche à vérifier l'intervieweur** : Le professionnalisme dans la modélisation objet et l'implémentation de bonnes pratiques de diagnostic pour simplifier la vie de l'équipe de développement [109, 113].

#### Question 7 : Expliquez ce qu'est un générateur (`generator`) et la différence entre le mot-clé `yield` et `return`.
*   **Réponse attendue** : Un générateur est un type d'itérable spécial qui évalue ses éléments de manière paresseuse (*lazy evaluation*) [11, 12, 110, 113]. Au lieu de calculer tous les éléments et de les stocker en mémoire d'un coup (comme le fait une liste), le générateur produit les valeurs une par une, uniquement à la demande [11, 12, 110, 113].
    *   Le mot-clé `return` termine définitivement l'exécution de la fonction et renvoie une valeur unique [11, 107, 126].
    *   Le mot-clé `yield` renvoie temporairement une valeur à l'appelant tout en suspendant l'état de la fonction (variables locales, pointeur d'instruction, stack d'appels) [11, 107, 108]. Lors de l'appel suivant de `next()`, la fonction reprend exactement là où elle s'était arrêtée [11, 107, 108].
*   **Ce que cherche à vérifier l'intervieweur** : L'optimisation des performances du code. C'est crucial lorsqu'on traite de très gros fichiers (ex: logs de serveurs de plusieurs gigaoctets) afin d'éviter une saturation de la mémoire RAM du système d'exécution [11, 110, 113].

#### Question 8 : Qu'est-ce qu'un gestionnaire de contexte (`context manager`) et comment fonctionne l'instruction `with` ?
*   **Réponse attendue** : Un gestionnaire de contexte est un objet qui définit les actions de configuration et de nettoyage à exécuter lors de l'entrée et de la sortie d'un bloc de code [13, 109, 122]. Il s'utilise avec l'instruction `with` [13, 98, 109, 122]. Il repose sur l'implémentation de deux méthodes spéciales (le protocole de contexte) :
    *   `__enter__()` : Initialise la ressource (ex: ouvre le fichier, établit une connexion) et en renvoie une référence [13, 99, 122].
    *   `__exit__(exc_type, exc_val, exc_tb)` : S'exécute automatiquement à la fin du bloc (ou si une exception est levée), permettant de libérer proprement la ressource (ex: fermeture automatique) [112, 122]. Elle peut également intercepter ou laisser propager les exceptions levées dans le bloc [13, 112].
*   **Ce que cherche à vérifier l'intervieweur** : La rigueur du candidat vis-à-vis de la fuite de descripteurs de fichiers, de connexions réseau, et son aptitude à utiliser les idiomes natifs de Python pour un code plus propre et plus sûr [6, 13, 98, 99].

---

### Niveau : Avancé

#### Question 9 : Comment fonctionnent les décorateurs (`decorators`) en Python ? Écrivez-en un simple.
*   **Réponse attendue** : Un décorateur est une fonction qui prend une autre fonction en argument, en modifie ou en étend le comportement (sans toucher à son code source), et renvoie une nouvelle fonction modifiée [10, 12, 71, 114]. Cela repose sur le fait qu'en Python, les fonctions sont des objets de "première classe" (on peut les passer en argument, les retourner et les imbriquer) [11, 74].

Exemple de décorateur simple pour journaliser les appels de fonctions :
```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de {func.__name__} avec args={args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} a retourné {result}")
        return result
    return wrapper

@log_decorator
def addition(a, b):
    return a + b
```
*   **Ce que cherche à vérifier l'intervieweur** : La maîtrise de la programmation fonctionnelle, du concept de fermeture (*closure*) [11, 74], et de la factorisation du code (principe DRY : Don't Repeat Yourself) appliquée à des problématiques transverses comme la sécurité, l'authentification ou les logs [12, 72].

#### Question 10 : Qu'est-ce que le Global Interpreter Lock (GIL) de CPython et quel est son impact sur les performances d'un programme multithread ?
*   **Réponse attendue** : Le GIL est un verrou mutuel utilisé par l'interpréteur CPython (l'implémentation de référence de Python) pour s'assurer qu'**un seul thread exécute du bytecode Python à la fois**, même sur une machine équipée de plusieurs cœurs de processeur [75, 100, 101, 102, 104, 105]. Le GIL a été mis en œuvre pour simplifier l'intégration des bibliothèques C et pour rendre la gestion mémoire interne (basée sur le comptage de références) totalement thread-safe [102, 103, 115, 116].
    Son impact est direct :
    *   Pour les tâches **CPU-bound** (calculs intensifs) : le multithreading ne fournit aucun gain de performance et peut même ralentir l'exécution à cause du surcoût de la commutation de contexte (*context switching*) [101, 103, 105].
    *   Pour les tâches **I/O-bound** (opérations d'entrée/sortie, réseau, lecture/écriture disque) : le multithreading reste très efficace car l'interpréteur relâche temporairement le GIL pendant les phases d'attente d'I/O, permettant à d'autres threads de s'exécuter [14, 17, 101, 102].
*   **Ce que cherche à vérifier l'intervieweur** : Si le candidat comprend les limites architecturales du langage et sait diagnostiquer les goulets d'étranglement de performance [75, 101, 103].

#### Question 11 : Dans quel cas privilégier le module `threading` plutôt que le module `multiprocessing` ?
*   **Réponse attendue** : 
    *   On utilise le module **`threading`** pour des tâches limitées par les entrées/sorties (**I/O-bound**), telles que des requêtes HTTP parallèles, l'attente de connexions sur des sockets ou le scan de ports réseau [14, 17, 28]. Les threads partagent le même espace mémoire au sein d'un seul processus, ce qui rend le partage de données extrêmement léger mais nécessite une synchronisation rigoureuse via des verrous (`Lock`) pour éviter les conditions de course (*race conditions*) [81, 82, 83].
    *   On utilise le module **`multiprocessing`** pour des tâches limitées par la puissance de calcul (**CPU-bound**), comme le craquage de hachages par force brute, le traitement lourd d'images ou d'analyses statistiques [81, 102]. Chaque processus possède son propre interpréteur Python indépendant et son propre espace de mémoire privée (contournant ainsi le GIL) [82, 103]. Cependant, le partage de données entre processus est plus lourd car il nécessite des mécanismes de communication inter-processus (IPC) comme des `Queue` ou des `Pipe` [133, 145].
*   **Ce que cherche à vérifier l'intervieweur** : L'aptitude du candidat à concevoir une architecture logicielle hautement performante et adaptée à la charge de travail ciblée [81, 82, 101, 102].

#### Question 12 : Expliquez comment fonctionne le ramasse-miettes (Garbage Collector) en Python.
*   **Réponse attendue** : Python (dans son implémentation CPython) utilise principalement un mécanisme de **comptage de références** (*reference counting*) [115, 116]. Chaque fois qu'un objet est référencé par une variable, son compteur de références augmente [115, 116]. Dès qu'une variable ne pointe plus sur cet objet (ou est détruite à la sortie d'un scope), le compteur diminue [115, 116]. Lorsque ce compteur atteint **zéro**, l'objet est immédiatement détruit et sa mémoire est libérée [115, 116].
    Pour gérer les cas de **références circulaires** (par exemple, un objet A qui référence un objet B, et l'objet B qui référence l'objet A, empêchant leurs compteurs d'atteindre zéro même s'ils sont devenus inaccessibles du reste du programme), Python intègre un ramasse-miettes cyclique basé sur un algorithme de détection de cycles [115, 116]. Ce dernier s'exécute périodiquement en arrière-plan en classant les objets par générations [115].
*   **Ce que cherche à vérifier l'intervieweur** : La connaissance du cycle de vie des objets en Python, des risques de fuite de mémoire liés aux références circulaires, et des mécanismes de bas niveau du langage [115, 116].

---

### Niveau : Confirmé

#### Question 13 : Dans le cadre de la programmation asynchrone (`asyncio`), quelle est la différence entre une Coroutine, une Tâche (Task) et une Future ?
*   **Réponse attendue** :
    *   Une **Coroutine** est une fonction spéciale définie avec `async def` [14, 15]. L'appel de cette fonction ne l'exécute pas immédiatement, mais renvoie un objet coroutine [15]. Pour l'exécuter, elle doit être programmée dans l'événement loop (via `await` ou `asyncio.run()`) [14, 15].
    *   Une **Tâche (Task)** est un objet de haut niveau fourni par `asyncio` qui encapsule une coroutine et planifie de manière autonome son exécution dans la boucle d'événements [15]. Elle hérite de `Future` et permet de suivre l'état d'avancement de la coroutine (si elle est en cours, terminée, annulée) et d'obtenir son résultat de manière non bloquante [15].
    *   Une **Future** est un objet de bas niveau représentant un résultat d'exécution qui n'est pas encore disponible mais qui le sera dans le futur [15]. C'est une promesse de résultat. En général, les développeurs manipulent des `Task` plutôt que des `Future` directement [15].
*   **Ce que cherche à vérifier l'intervieweur** : La maîtrise de la programmation asynchrone événementielle monothread, indispensable pour écrire des outils réseau modernes gérant des milliers de connexions asynchrones simultanées [14, 15].

#### Question 14 : Qu'est-ce que l'introspection (ou réflexion) en Python et comment l'utiliser ?
*   **Réponse attendue** : L'introspection est la capacité d'un programme à examiner le type, les propriétés, les attributs et les méthodes d'un objet au moment de son exécution [97, 98]. Python supporte pleinement l'introspection à l'aide de fonctions natives et d'attributs spéciaux [73, 74, 97, 98] :
    *   `type(obj)` : Renvoie le type d'un objet [18, 97].
    *   `dir(obj)` : Renvoie la liste de tous les attributs et méthodes associés à l'objet [97, 98, 140].
    *   `hasattr(obj, 'name')` / `getattr(obj, 'name')` : Vérifie la présence d'un attribut ou en extrait la valeur dynamiquement [97].
    *   `obj.__doc__` : Permet d'extraire la docstring de l'objet à la volée [73, 114].
    *   `callable(obj)` : Indique si l'objet peut être appelé comme une fonction [96].
*   **Ce que cherche à vérifier l'intervieweur** : La maîtrise de la programmation dynamique avancée. Par exemple, charger des modules de plugins à la volée ou écrire des outils d'analyse automatique de payloads et de binaires [73, 74, 98].

#### Question 15 : Quels sont les avantages du typage statique optionnel (`typing`) en Python et quels outils de static analysis l'accompagnent ?
*   **Réponse attendue** : Le typage statique (introduit via le module `typing` et les annotations de types de PEP 484) permet d'indiquer explicitement le type attendu des paramètres et des retours de fonctions [86, 91].
    Ses avantages majeurs sont :
    *   Une documentation vivante et auto-générée du code (meilleure lisibilité) [13].
    *   Une intégration étroite avec les IDE (auto-complétion plus intelligente, refactoring sûr).
    *   La détection précoce des bugs de type (ex: passer un entier là où une chaîne est attendue) avant même l'exécution du script, grâce à des analyseurs statiques comme **MyPy**, **PyLint** ou **Flake8** [114].
    Il est important de rappeler que les annotations n'ont **aucun impact sur les performances à l'exécution** (Python reste un langage à typage dynamique à l'exécution) [92].
*   **Ce que cherche à vérifier l'intervieweur** : La rigueur professionnelle, l'expérience dans la maintenance de grandes bases de code collaboratives et la mise en place de pipelines CI/CD intégrant de l'analyse de qualité de code [114].

---

### Niveau : Python appliqué à la cybersécurité

#### Question 16 : Comment implémenter une communication par Sockets réseau bas niveau en Python ? Expliquez la différence entre `SOCK_STREAM` et `SOCK_DGRAM`.
*   **Réponse attendue** : Le module standard `socket` est le socle de toute communication réseau en Python [16, 20, 139].
    *   `SOCK_STREAM` spécifie un socket orienté connexion utilisant le protocole **TCP** [16, 138, 141]. Il garantit la délivrance ordonnée, complète et sans erreur des données grâce à des accusés de réception [16, 21].
    *   `SOCK_DGRAM` spécifie un socket sans connexion utilisant le protocole **UDP** [16, 138, 141]. Les données sont envoyées sous forme de datagrammes isolés, ce qui est beaucoup plus rapide et léger, mais n'offre aucune garantie de réception ni d'ordre [16, 21, 22].

Exemple de client TCP simple en Python :
```python
import socket

# Création du socket TCP/IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connexion au serveur
client.connect(("127.0.0.1", 8080))
# Envoi de données sous forme de bytes encodés
client.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
# Réception de la réponse
response = client.recv(4096)
print(response.decode("utf-8"))
# Fermeture propre
client.close()
```
*   **Ce que cherche à vérifier l'intervieweur** : La compréhension des concepts réseau (couche transport du modèle OSI) et l'aptitude à développer des outils réseau sur-mesure (scanners, agents d'écoute, reverse-shells) sans dépendre de bibliothèques tierces [16, 20, 44].

#### Question 17 : Comment exécuter de manière sécurisée des commandes système via le module `subprocess` et éviter les failles d'injection ?
*   **Réponse attendue** : Le module `subprocess` sert à exécuter des processus système externes [32, 60]. Pour l'utiliser de manière sécurisée, il faut **impérativement éviter l'utilisation de `shell=True`** [33, 44].
    Lorsque `shell=True` est utilisé, la commande est transmise sous forme de chaîne de caractères au shell système (ex: `/bin/sh` ou `cmd.exe`) [33, 44]. Si des entrées utilisateur non assainies y sont concaténées, un attaquant peut exécuter des commandes arbitraires (injection de commande) [44].
    La bonne pratique consiste à passer la commande sous forme d'une **liste d'arguments** et à laisser `shell=False` (par défaut) :
```python
import subprocess

# SÉCURISÉ : Les arguments sont isolés, pas d'interprétation par le shell
result = subprocess.run(["ping", "-c", "4", "127.0.0.1"], capture_output=True, text=True)
print(result.stdout)
```
*   **Ce que cherche à vérifier l'intervieweur** : La sensibilité du candidat à la sécurité offensive/défensive de son propre code et sa maîtrise des fonctions d'exécution du système d'exploitation [32, 61].

#### Question 18 : Comment générer un hachage cryptographique SHA256 d'un fichier volumineux sans saturer la mémoire vive ?
*   **Réponse attendue** : Pour traiter des fichiers volumineux de manière efficace et sécurisée, il faut utiliser le module `hashlib` [64], ouvrir le fichier en mode de lecture binaire brut (`"rb"`) [64], et lire le contenu **par morceaux (chunks)** successifs à l'aide d'une boucle d'itération [64, 65]. Cela évite de charger l'intégralité du fichier en RAM d'un seul coup [64, 110].

Code recommandé :
```python
import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        # Lecture par blocs de 4096 octets jusqu'à la fin (chaîne vide b"")
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()
```
*   **Ce que cherche à vérifier l'intervieweur** : La capacité à allier manipulation de données binaires brutes (`bytes`), hashing de sécurité (pour du contrôle d'intégrité de fichiers ou d'analyse de malwares), et gestion optimale de la mémoire sur de grands ensembles de données [64, 65].

---

## 2. Snippets de Code à Analyser

### Snippet 1 : L'erreur classique des valeurs par défaut mutables

**Code à analyser :**
```python
def add_target_ip(ip_address, ip_list=[]):
    ip_list.append(ip_address)
    return ip_list

print(add_target_ip("192.168.1.1"))
print(add_target_ip("10.0.0.1"))
```

*   **Comportement observé** : 
    Le premier appel affiche `['192.168.1.1']`. Le second appel affiche `['192.168.1.1', '10.0.0.1']` au lieu de `['10.0.0.1']`.
*   **Explication technique** :
    En Python, les valeurs des arguments par défaut sont évaluées **une seule fois, lors de la définition de la fonction**, et non à chaque appel [100]. Si la valeur par défaut est un objet **mutable** (comme une liste `[]` ou un dictionnaire), tous les appels de fonction sans argument explicite partageront exactement la même instance d'objet en mémoire [100].
*   **Correction recommandée** :
    Il faut utiliser `None` comme valeur par défaut sentinelle et initialiser l'objet mutable au sein de la fonction :
```python
def add_target_ip(ip_address, ip_list=None):
    if ip_list is None:
        ip_list = []
    ip_list.append(ip_address)
    return ip_list
```

---

### Snippet 2 : Optimisation d'un scanner de ports synchrone inefficace

**Code de départ (synchrone et lent) :**
```python
import socket

def scan_ports_slow(target_ip, ports):
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} est ouvert !")
        s.close()
```

*   **Pourquoi est-il inefficace ?** :
    Ce script effectue les connexions de manière séquentielle [24, 27]. Si un port est fermé ou filtré, le script attend la fin du timeout (ici 1 seconde) avant de passer au port suivant [27, 28]. Pour scanner 1000 ports, cela peut prendre jusqu'à 15 minutes.
*   **Correction recommandée (multi-threadé avec `ThreadPoolExecutor`)** :
    Nous utilisons le module `concurrent.futures` pour paralléliser les requêtes sur un pool de threads, réduisant ainsi le temps de scan global à quelques secondes [27, 28].

```python
import socket
from concurrent.futures import ThreadPoolExecutor

def scan_single_port(target_ip, port):
    try:
        # Utilisation d'un gestionnaire de contexte pour garantir la fermeture du socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            # connect_ex renvoie 0 en cas de succès, évitant de lever une exception
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} est ouvert !")
    except socket.error:
        pass

def scan_ports_fast(target_ip, ports, max_threads=100):
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        # Soumission parallèle des tâches de scan de port
        executor.map(lambda p: scan_single_port(target_ip, p), ports)
```

---

## 3. Problèmes Algorithmiques Classiques

### Problème 1 : Calcul de la taille globale d'un répertoire (DFS récursif)

*   **Énoncé** : On souhaite écrire une fonction Python qui calcule la taille globale d'une entité de notre système de fichiers simulé [78, 79]. Si l'entité est un fichier, on renvoie directement sa taille [79]. Si c'est un dossier, on calcule récursivement la somme des tailles de tous ses enfants (fichiers et sous-dossiers) [78, 79].
*   **Solution algorithmique (DFS)** [78, 79] :

```python
class Entity:
    def __init__(self, entity_id, entity_type, name, size=0, children=None):
        self.id = entity_id
        self.type = entity_type  # 'file' ou 'directory'
        self.name = name
        self.size = size
        self.children = children if children is not None else []  # IDs des enfants

class FileSystem:
    def __init__(self, entity_dict):
        # Dictionnaire pour un accès en O(1) aux entités par leur ID
        self.entities = entity_dict

    def calculate_total_size(self, entity_id):
        entity = self.entities.get(entity_id)
        if not entity:
            return 0
        
        # Cas de base : si c'est un fichier, renvoyer sa taille individuelle
        if entity.type == 'file':
            return entity.size
            
        # Cas récursif : si c'est un dossier, parcourir en profondeur (DFS) tous les enfants
        total_size = 0
        for child_id in entity.children:
            total_size += self.calculate_total_size(child_id)
            
        return total_size
```
*   **Complexité** : 
    *   **Temporelle** : $O(N)$ où $N$ est le nombre total d'entités sous le répertoire racine, car chaque entité est visitée exactement une fois lors du parcours récursif [75, 79].
    *   **Spatiale** : $O(D)$ où $D$ est la profondeur maximale de l'arbre du système de fichiers, correspondant à la taille maximale de la pile d'appels récursive (*call stack*) [2, 5, 120].

---

### Problème 2 : Calcul du temps d'exécution exclusif des fonctions (Stack)

*   **Énoncé** : Dans un processeur monothread, on enregistre l'activité des fonctions sous forme d'une liste de logs structurés : `"{id}:{start|end}:{timestamp}"` [76, 77]. Une fonction peut appeler d'autres fonctions imbriquées [76]. Écrivez une fonction qui prend en entrée le nombre de fonctions `n` et la liste des `logs`, et retourne un tableau de taille `n` contenant le **temps d'exécution exclusif** de chaque fonction (c'est-à-dire le temps passé par la fonction elle-même, en excluant les temps passés dans les fonctions enfants) [76, 77].
*   **Solution algorithmique (Utilisation d'une Pile / Stack)** [76, 77] :

```python
def exclusive_time(n, logs):
    result = [0] * n
    stack = []  # Pile stockant les tuples (function_id, start_timestamp)
    prev_time = 0
    
    for log in logs:
        # Parsing des logs structurés
        fn_id_str, status, timestamp_str = log.split(":")
        fn_id = int(fn_id_str)
        timestamp = int(timestamp_str)
        
        if status == "start":
            # Si une fonction est déjà en cours d'exécution sur le CPU
            if stack:
                # On lui attribue le temps écoulé depuis le dernier événement
                result[stack[-1]] += timestamp - prev_time
            stack.append(fn_id)
            prev_time = timestamp
        else:  # status == "end"
            # Fin de la fonction actuellement au sommet de la pile
            current_fn = stack.pop()
            # On lui ajoute son temps d'exécution (la fin est inclusive, donc + 1)
            result[current_fn] += timestamp - prev_time + 1
            # On met à jour le marqueur de temps à l'instant suivant la fin de l'appel
            prev_time = timestamp + 1
            
    return result
```
*   **Exemple d'exécution** [77] :
    Pour `n = 2` et `logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]` [77] :
    *   À l'instant 0, la fonction 0 démarre.
    *   À l'instant 2, la fonction 1 démarre (la fonction 0 a donc tourné 2 unités exclusives : de 0 à 1).
    *   À l'instant 5, la fonction 1 s'arrête (la fonction 1 a tourné 4 unités exclusives : de 2 à 5).
    *   À l'instant 6, la fonction 0 s'arrête (la fonction 0 reprend et tourne 1 unité exclusive : l'instant 6).
    *   **Résultat** : `[3, 4]`.
*   **Complexité** : 
    *   **Temporelle** : $O(L)$ où $L$ est le nombre de lignes de logs, car nous lisons chaque log une seule fois et effectuons des opérations d'empilement/dépilement en $O(1)$.
    *   **Spatiale** : $O(N)$ pour stocker l'état dans la pile dans le pire des cas d'appels imbriqués.

---

## 4. Simulation d'Entretien Technique Réel (15 Questions Progressives)

*Cette section simule un entretien technique d'évaluation, alternant questions conceptuelles, validation d'architecture et questions d'orientations spécialisées.*

### Question 1 : Comment lancez-vous l'interpréteur Python en mode interactif et comment exécutez-vous un script ? [125, 143]
*   **Réponse attendue** : Pour lancer l'interpréteur interactif (REPL), on tape simplement `python` (ou `python3`) dans le terminal CLI [125, 143]. Pour exécuter un script enregistré, on tape la commande `python mon_script.py` [125, 143].
*   **Évaluation** : Valide la maîtrise minimale de l'environnement de travail par un candidat junior [125].

### Question 2 : Quelle est la différence entre un fichier `.py` et un fichier `.pyc` ? [125]
*   **Réponse attendue** : Le fichier `.py` contient le code source en texte brut écrit par le développeur [125]. Le fichier `.pyc` contient le **bytecode compilé** généré automatiquement par l'interpréteur Python [125]. Lors d'une exécution ultérieure, Python charge directement le `.pyc` pour éviter l'étape de compilation intermédiaire, accélérant ainsi le démarrage du programme [125].
*   **Évaluation** : Vérifie si le candidat comprend le processus d'exécution hybride de Python (compilation en bytecode puis interprétation par la machine virtuelle CPython) [125].

### Question 3 : Si une fonction ne contient pas d'instruction `return`, que renvoie-t-elle et est-ce valide ? [121, 126]
*   **Réponse attendue** : Oui, c'est parfaitement valide en Python [121, 126]. La fonction s'exécute jusqu'à sa dernière ligne indentée et retourne implicitement l'objet **`None`** (qui est l'instance unique du type `NoneType`) [121, 126].
*   **Évaluation** : Teste la rigueur sur le comportement par défaut des fonctions et la gestion des valeurs de retour [5, 126].

### Question 4 : Quelle est la différence entre `range` et `xrange` et comment cela a-t-il évolué entre Python 2 et Python 3 ? [96, 97, 106]
*   **Réponse attendue** : En Python 2, `range()` générait et stockait en mémoire une **liste complète** d'entiers d'un seul coup, ce qui était très inefficace pour de grandes plages de valeurs [96, 106]. `xrange()` renvoyait un objet générateur qui produisait les nombres à la demande (lazy-loading) [96, 97, 106]. En Python 3, l'ancienne fonction `range()` a été supprimée et remplacée par le comportement de `xrange()`, qui a pris le nom de `range()` [96, 97].
*   **Évaluation** : Connaissance de l'histoire du langage, des évolutions majeures de la version 3, et sensibilité à la consommation mémoire [96, 97].

### Question 5 : Comment testeriez-vous l'égalité de deux dictionnaires en Python ? [146]
*   **Réponse attendue** : En Python, on utilise simplement l'opérateur de comparaison d'égalité **`==`** [146]. Contrairement à d'autres langages où `==` compare les adresses mémoire des objets, Python surcharge l'opérateur d'égalité pour les dictionnaires afin de réaliser une comparaison de valeurs [146]. Deux dictionnaires sont considérés comme égaux si et seulement s'ils contiennent exactement les mêmes clés associées aux mêmes valeurs, quel que soit l'ordre d'insertion [146].
*   **Évaluation** : Maîtrise des structures de clés-valeurs et de la surcharge interne des opérateurs [146].

### Question 6 : Quelle est la différence entre une copie superficielle (`shallow copy`) et une copie profonde (`deep copy`) ? [106, 107]
*   **Réponse attendue** :
    *   Une **copie superficielle** (`copy.copy()`) crée un nouvel objet, mais insère dans celui-ci des références vers les objets originaux [106, 107]. Si l'objet original contient des objets mutables imbriqués (ex: une liste de listes), la modification d'un élément interne imbriqué affectera à la fois l'original et la copie [107].
    *   Une **copie profonde** (`copy.deepcopy()`) crée un nouvel objet et copie récursivement tous les objets imbriqués qu'il contient [106, 107]. L'original et la copie sont alors totalement indépendants en mémoire [107].
*   **Évaluation** : Compréhension des mécanismes de référencement d'objets en mémoire et prévention de bugs complexes de mutation accidentelle [106, 107].

### Question 7 : Comment pouvez-vous forcer une fonction à exiger des arguments uniquement nommés (*keyword-only*) ? [67]
*   **Réponse attendue** : On place un astérisque seul `*` dans la liste des paramètres de la fonction [70]. Tout paramètre défini après cet astérisque ne peut plus être passé comme argument positionnel, il doit obligatoirement être spécifié avec son nom lors de l'appel [70].
```python
def configure_firewall(*, status, log_traffic=True):
    pass

# configure_firewall("ON") -> Lève une TypeError
configure_firewall(status="ON", log_traffic=True)  # CORRECT
```
*   **Évaluation** : Compétence de niveau intermédiaire à avancé dans la conception d'API internes explicites et sûres [67, 70].

### Question 8 : À quoi sert l'instruction `assert` en Python et quel est l'impact de l'option d'optimisation `-O` ? [110, 105]
*   **Réponse attendue** : L'instruction `assert` est une aide au débogage permettant de tester si une condition est vraie [110]. Si la condition est fausse, Python lève immédiatement une exception `AssertionError` [110]. Elle est principalement utilisée pour documenter et valider des invariants internes de code durant le développement.
    Si l'on exécute Python avec l'option d'optimisation **`-O`** (ou `-OO`), toutes les assertions sont **complètement ignorées et retirées du bytecode à la compilation** [105]. Il ne faut donc jamais utiliser `assert` pour valider des entrées utilisateur ou des opérations de sécurité critiques (comme vérifier des mots de passe ou des droits d'accès) sous peine qu'elles soient purement contournées en production [105].
*   **Évaluation** : Connaissance des drapeaux système de l'interpréteur Python et sensibilisation à la sécurité applicative défensive [105, 110].

### Question 9 : Comment Python gère-t-il l'héritage multiple et qu'est-ce que le MRO (Method Resolution Order) ? [103]
*   **Réponse attendue** : Contrairement à d'autres langages, Python supporte l'héritage multiple (une classe fille peut hériter de plusieurs classes mères) [103]. Pour résoudre l'ordre d'appel des méthodes en cas d'ambiguïté (comme le "problème du diamant"), Python utilise l'algorithme de linéarisation C3 pour calculer le **MRO** [103]. Le MRO définit l'ordre exact dans lequel Python recherche un attribut ou une méthode dans l'arbre des classes héritées [103]. On peut visualiser cet ordre en appelant la méthode `.mro()` ou l'attribut `__mro__` sur la classe [103].
*   **Évaluation** : Maîtrise avancée des concepts de POO et de l'architecture objet interne du langage [103].

### Question 10 : Quelle est la manière la plus simple et élégante d'implémenter le pattern Singleton en Python ? [116, 84]
*   **Réponse attendue** : Bien que l'on puisse utiliser des métaclasses ou redéfinir la méthode `__new__` [115], la manière la plus idiomatique ("Pythonic") et simple d'implémenter un Singleton est d'utiliser la structure de **module** [116]. En Python, les modules sont importés une seule fois au cours de l'exécution (ils sont mis en cache dans `sys.modules`). Tout état ou variable globale défini dans le module se comporte naturellement comme une instance unique partagée à travers l'application.

Sinon, via un décorateur de classe :
```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class SecurityConfig:
    def __init__(self):
        self.api_key = "secret_key"
```
*   **Évaluation** : Capacité à intégrer des patrons de conception classiques en exploitant au mieux l'architecture de fichiers et d'importations native du langage [116].

### Question 11 : Pourquoi l'utilisation de `asyncio` est-elle souvent plus efficace que le multithreading classique pour concevoir un serveur réseau ? [14, 15, 17]
*   **Réponse attendue** : Le multithreading classique repose sur le scheduler du système d'exploitation pour commuter les threads (préemption), ce qui introduit un surcoût important de changement de contexte (*context switching*) et nécessite de la mémoire vive pour la pile d'appels de chaque thread [81, 84]. De plus, le développeur doit protéger les ressources partagées à l'aide de verrous compliqués [81, 83].
    `asyncio` utilise un **modèle asynchrone monothread basé sur une boucle d'événements (Event Loop)** [15]. Les tâches se cèdent volontairement le contrôle (coopératif) lors des attentes d'I/O via `await` [14, 15]. Il n'y a donc pas de changement de contexte OS lourd, la consommation mémoire est minime, et comme le code tourne sur un seul thread, il n'y a aucun risque de conflit d'accès mémoire direct sur les variables globales [14, 15].
*   **Évaluation** : Maîtrise architecturale de haut niveau en réseau et systèmes asynchrones [14, 15].

### Question 12 : Qu'est-ce qu'une condition de course (*race condition*) et comment la résoudre en programmation concurrente ? [81, 83, 141]
*   **Réponse attendue** : Une condition de course survient lorsque deux ou plusieurs threads accèdent et modifient une ressource partagée (par exemple, un compteur ou un fichier) de manière simultanée, sans synchronisation, rendant le résultat final dépendant de l'ordre d'ordonnancement imprévisible des threads par le système [81, 83, 84].
    On résout cela en utilisant un verrou mutuel (**`threading.Lock`**) [81, 86, 141]. Un thread doit acquérir le verrou avec `.acquire()` avant d'entrer dans la zone critique de modification, et le relâcher avec `.release()` une fois terminé, forçant les autres threads à attendre leur tour [132, 134, 141]. La bonne pratique est d'utiliser le gestionnaire de contexte `with lock:` pour garantir le relâchement automatique du verrou, même si une erreur survient [13, 112].
*   **Évaluation** : Capacité à écrire du code concurrent sécurisé de niveau confirmé, indispensable en réseau et cryptographie applicative [81, 83].

### Question 13 : Expliquez comment utiliser le module `subprocess` de manière sûre pour exécuter une commande sans passer par le shell, et comment récupérer son code de retour. [32, 33, 58]
*   **Réponse attendue** : On utilise la fonction `subprocess.run()` [33]. Pour éviter de passer par le shell, on transmet la commande sous forme d'une liste d'arguments et on s'assure que `shell=False` (par défaut) [33]. Pour récupérer la sortie standard et d'erreur, on utilise `capture_output=True` [59]. Pour forcer le décodage automatique des flux d'octets en chaînes de caractères, on ajoute `text=True` [59].

Exemple :
```python
import subprocess

try:
    result = subprocess.run(
        ["strings", "/bin/ls"],  # Commande et argument séparés
        capture_output=True,
        text=True,
        check=True  # Lève une exception si le code de retour est différent de 0
    )
    print("Code de retour :", result.returncode)
    print("Sortie :", result.stdout[:500])
except subprocess.CalledProcessError as e:
    print(f"Erreur d'exécution ({e.returncode}) :", e.stderr)
```
*   **Évaluation** : Rigueur technique dans l'interaction avec le système d'exploitation et la gestion propre des erreurs de processus [32, 33, 58, 59].

### Question 14 : Comment concevoir un script simple d'écoute réseau (honeypot factice) pour capturer les requêtes de connexion d'un malware potentiel sur un port particulier ? [51, 62]
*   **Réponse attendue** : On utilise le module `socket` pour créer un serveur TCP à l'écoute sur le port cible [16, 51]. On configure l'adresse d'écoute sur toutes les interfaces `""` ou `"0.0.0.0"`, on associe le socket à l'adresse avec `.bind()`, on l'ouvre à l'écoute avec `.listen()`, et on entre dans une boucle infinie pour accepter les connexions entrantes avec `.accept()` afin de journaliser les adresses IP et payloads reçus [51, 62].

Exemple de script d'écoute :
```python
import socket

def run_honeypot(port=8080):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Réutilisation de l'adresse pour éviter l'erreur "Address already in use"
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"[*] Honeypot actif et à l'écoute sur le port {port}...")
    
    try:
        while True:
            # Attente de connexion d'un client
            client_sock, client_addr = server.accept()
            print(f"[!] Connexion entrante détectée depuis {client_addr}")
            
            # Réception et journalisation du payload (ex: payload d'un malware ou fuzzer)
            payload = client_sock.recv(1024)
            if payload:
                print(f"[Payload reçu] : {payload.decode('utf-8', errors='replace')}")
                
            # Fermeture de la session client
            client_sock.close()
    except KeyboardInterrupt:
        print("\n[*] Honeypot arrêté.")
    finally:
        server.close()
```
*   **Évaluation** : Aptitude pratique à concevoir des scripts de détection défensive et d'investigation numérique dans un cadre de cybersécurité [51, 61, 62].

### Question 15 : Comment configureriez-vous un socket en Python pour qu'il établisse une connexion chiffrée SSL/TLS vers un serveur sécurisé ? [17, 20]
*   **Réponse attendue** : On utilise d'abord le module standard `socket` pour initier une connexion TCP standard [16, 20], puis on enveloppe ce socket avec le module standard `ssl` pour négocier la couche de chiffrement [17, 20].

```python
import socket
import ssl

target_host = "www.google.com"
target_port = 443

# 1. Création du contexte SSL par défaut (charge les autorités de certification système)
context = ssl.create_default_context()

# 2. Établissement de la socket TCP classique
raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Enveloppement du socket avec SSL pour négocier la poignée de main chiffrée
ssl_socket = context.wrap_socket(raw_socket, server_hostname=target_host)

# 4. Connexion chiffrée finale
ssl_socket.connect((target_host, target_port))
print("[*] Connexion sécurisée SSL/TLS établie avec succès.")

# 5. Envoi d'une requête HTTP sécurisée
ssl_socket.sendall(b"GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n")
response = ssl_socket.recv(1024)
print(response.decode("utf-8"))

ssl_socket.close()
```
*   **Évaluation** : Validation des compétences de niveau confirmé en sécurité réseau, garantissant que le candidat comprend les protocoles de chiffrement de transport et leur mise en œuvre en Python [17, 20, 21].

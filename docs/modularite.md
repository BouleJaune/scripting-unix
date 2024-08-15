# Modularité
## Python modules

En Python, un **module** est un fichier contenant du code Python, comme des fonctions, des classes et des variables, qui peuvent être importées et utilisées dans d'autres fichiers Python. Les modules permettent de structurer un programme Python en séparant le code en morceaux logiques, facilitant ainsi la réutilisation et l'organisation.

L'écosystème Python possède des milliers de modules externes entretenus par la communauté permettant de faciliter le développement de n'importe quel programme. Cette diversité de modules est l'une des plus grande force de Python.

### Types de Modules

1. **Modules intégrés** : Ces modules font partie de l'installation standard de Python et n'ont pas besoin d'être installés séparément. Exemples : `math`, `sys`, `os`.

2. **Modules tiers** : Ce sont des modules créés par la communauté Python et disponibles via le Python Package Index (PyPI). Ils doivent être installés avec des outils comme `pip`. Exemples : `requests`, `numpy`, `pandas`.

3. **Modules personnalisés** : Ce sont des modules que vous créez vous-même pour organiser votre propre code.

### Création d'un Module

Un module en Python est simplement un fichier Python (.py). Par exemple, un fichier `mymodule.py` pourrait contenir :

```python
# mymodule.py
def saluer(nom):
    return f"Bonjour, {nom}!"
```

### Utilisation des Modules
#### Importation de Modules

Pour utiliser un module, vous devez d'abord l'importer dans votre script Python. Il existe plusieurs façons de le faire :

- Importation complète :

```python
import mymodule

print(mymodule.saluer("Alice"))
```

- Importation avec un alias :

```python
import mymodule as mm

print(mm.saluer("Bob"))
```

- Importation de fonctions spécifiques :

```python
from mymodule import saluer, addition

print(saluer("Charlie"))
```

- Importation de toutes les fonctions (non recommandé) :

```python
from mymodule import *

print(saluer("Diana"))
```

Cette méthode n'est pas recommandée car elle peut porter à confusion la provenance d'une fonction. Cela rend le code peut lisible.

### Chemin d'accès aux Modules

Python va d'abord chercher le module dans les modules builtins, listés dans ``sys.builtin_module_names``. Si il ne le trouve pas dans cette liste il va chercher le fichier .py du module recherché dans les dossiers listés par ``sys.path``.

Cette liste contient les dossiers d'installation de modules externes mais aussi le dossier actuel (pour une exécution intéractive) ou le dossier du script .py appelé.

#### Exercice 

1. Créez un module Python nommé `calculs.py` qui contient deux fonctions :
    - `addition(a, b)` : retourne la somme de `a` et `b`.
    - `multiplication(a, b)` : retourne le produit de `a` et `b`.
    
2. Dans un autre script Python (par exemple, `main.py`), importez le module `calculs` et utilisez les deux fonctions pour :
    - Calculer et afficher la somme de `10` et `5`.
    - Calculer et afficher le produit de `10` et `5`.

??? Notes "Exemple de solution"

     `calculs.py`
    ```python
    # 1. Définition du module avec les fonctions

    def addition(a, b):
        return a + b

    def multiplication(a, b):
        return a * b
    ```
    ``main.py``

    ```python

    # 2. Importation et utilisation du module

    import calculs

    somme = calculs.addition(10, 5)
    produit = calculs.multiplication(10, 5)

    print("La somme de 10 et 5 est :", somme)
    print("Le produit de 10 et 5 est :", produit)
    ```

## pip : Le Gestionnaire de Paquets de Python

**pip** est l'outil officiel et le plus couramment utilisé pour installer et gérer les packages Python. Il permet aux développeurs de rechercher, installer, mettre à jour et désinstaller des packages disponibles dans le Python Package Index (PyPI).

``pip`` est généralement installé par défaut avec Python.

### Utilisation de base

Pour installer, désinstaller ou mettre à jour un package :

```sh
pip install nom_du_package
pip uninstall nom_du_package
pip install --upgrade nom_du_package
```

Pour voir tous les packages installés dans votre environnement Python, utilisez la commande pip list :

```sh
pip list
```
``pip search`` permet de rechercher un package, mais il est souvent plus judicieux d'aller les chercher directement sur [PyPI](https://pypi.org/).

### Fichier Requirements

``pip`` permet également d'installer des packages à partir d'un fichier de dépendances (généralement nommé requirements.txt). Ce fichier liste les packages nécessaires à un projet.

```
# Exemple de fichier requirements.txt
requests==2.25.1
numpy>=1.19.5
pandas
```

Pour installer les modules depuis ce fichier on peut faire :

```sh
pip install -r requirements.txt
```

On peut utiliser ``pip freeze`` pour lister tout les modules installés et leur version et donc générer ce fichier :
```sh
pip freeze > requirements.txt
```

## Les environnements virtuels (venv)

### Le problème de ``pip`` seul

Lorsque l'on installe un paquet avec ``pip`` celui-ci se retrouvera installé de manière globale sur le système. Cela peut vite être problématique d'un point de vue gestion des dépendances : 

- Deux projets pourraient utiliser le même module mais dans des versions différentes ce qui génèrera des conflits.
- ``pip freeze`` va récupérer les modules d'autres projets et mettre dans le ``requirements.txt`` des modules non voulus.
- Toucher à l'installation de modules Python globaux sur Linux peut entrainer des comportements non-prévisibles étant donné que Python est utilisé direcement par l'OS (exemple : Qtile)
- On a plutôt envie de gérer les modules Python installés globalement directement via le package manager de la distribution pour s'assurer de ne pas avoir de conflits à l'échelle de l'OS et pour garder une uniformité des méthodes de maintenance du système.


Les deux derniers points sont tellement importants que sur certaines distributions (Archlinux par exemple), il n'est par défaut même pas possible d'installer directement avec ``pip`` des paquets.


### La solution : les environnements virtuels 

Toutes ces raisons poussent à vouloir un système qui permet d'isoler les projets les uns des autres et les isoler aussi du système. Pour cela on utilise des environnements virtuels (venvs).

Python fourni la fonctionnalité par défaut, il n'y a pas besoin de solutions externes qui peuvent amener leur propre lot de problèmes.

Pour créer un environnement virtuel il suffit d'être positionné dans le dossier du projet et faire : 
```sh
python -m venv venv
```

``-m`` permet de dire qu'on va appeler un module python, module dénommé ``venv``, ce module appelé tel quel attends le nom de l'environnement virtuel à créer, nom qui ici est aussi ``venv`` (mais aurait pu être autre chose).

La commande va générer un dossier du nom du venv (ici simplement ``venv``) et va le remplir de tout le nécessaire pour avoir un Python isolé, notamment copier le binaire en lui même de python, fournir des méthodes pour activer et désactiver le venv et des dossiers d'installations des modules. Cela reste suffisamment léger (16Mo pour un venv vierge).

En faisant un ``pip freeze`` avant et après activation du venv on peut comparer les modules disponibles. Avant le ``pip freeze`` renverra une longue liste de modules tandis que sur un venv vierge il n'y aura rien.


Pour activer l'environnement virtuel dans le Shell actuel, et donc dire au shell que ``python`` doit pointer vers le venv il faut sourcer le script d'activation, et pour désactiver simplement faire ``deactivate``.

```sh
# En étant dans le dossier du projet où le dossier venv se situe
source ./venv/bin/activate

# Pour désactiver le venv
deactivate
```

Il faut ainsi penser à le réactiver à chaque nouveau Shell. 
Des éditeurs de texte comme Visual Studio Code permettent de s'occuper de la gestion des venvs et de leur activation aussi.

#### Exercice

1. **Créer un Environnement Virtuel :**
   - Dans un répertoire de votre choix, créez un environnement virtuel nommé `venv`.

2. **Activer l'Environnement Virtuel :**
   - Activez l'environnement virtuel `venv`.

3. **Installer un Package avec `pip` et faire le fichier de requirements**
   - Utilisez `pip` pour installer le package `requests` dans l'environnement virtuel.
   - Générer le fichier de requirements

4. **Vérifier l'Installation :**
   - Démarrez un interpréteur Python et importez le package `requests` pour vérifier qu'il est installé correctement.

??? Notes "Exemple de solution"
    ```bash
    # Allez dans le dossier voulu puis créer le venv
    python -m venv venv
    # L'activer 
    source ./venv/bin/activate
    # Installation de requests et génération requirements.txt
    pip install requests
    pip freeze > requirements.txt
    ```
    Test : 
    ```python
    python -m requests # Donnera une réponse claire sur la présence du module ou sinon :
    python # puis une fois dans l'interpréteur
    >>>import requests
    >>>print(requests.__version__)
    ```


### Un mot sur d'autres solutions

Il existe de multiples autres solutions pour résoudre ce problème, certaines très connues et apportant bien d'autres fonctionnalités comme ``conda``. Cependant je déconseille fortement leur utilisation pour un néophyte du langage, encore plus dans le cadre d'administration de système Unix, où l'installation de logiciels externes est souvent limitée sur les serveurs.

- Ces outils ne sont pas universels et ne seront pas forcément disponibles dans tout les écosystèmes professionels.
- Ces outils rajoutent souvent beaucoup de fonctionnalités qui peuvent rendre confus les néophytes.
- Ces outils ne sont pas installés par défaut avec Python sur toutes les machines Linux récentes.
- Ces outils rajoutent trop d'asbstraction et empêchent de comprendre les tenants et aboutissants de certaines choses, tels que l'intérêt des venvs.


Je recommande ainsi d'utiliser simplement des venvs Python classique, et qu'une fois habitué, si le besoin s'en fait sentir, aller chercher un de ces outils en ayant un besoin précis en tête où les venvs classiques ne suffisent pas.


## Une courte liste de modules Python connus

#### Siences
1. **NumPy** - Calcul scientifique et manipulation de tableaux multidimensionnels.
2. **Pandas** - Analyse de données et manipulation de structures de données.
3. **Matplotlib** - Visualisation de données avec des graphiques 2D.
4. **Seaborn** - Visualisation statistique basée sur Matplotlib.
5. **SciPy** - Calcul scientifique avancé, incluant l'optimisation et les statistiques.

#### Machine learning
6. **scikit-learn** - Apprentissage automatique et data mining.
7. **TensorFlow** - Apprentissage automatique et réseaux de neurones.
8. **Keras** - Interface de haut niveau pour TensorFlow, simplifiant la construction de modèles de deep learning.
9. **PyTorch** - Bibliothèque de deep learning développée par Facebook.
10. **NLTK** - Traitement du langage naturel.

#### Web
11. **Requests** - Requêtes HTTP simples.
12. **BeautifulSoup** - Analyse et extraction de données à partir de documents HTML et XML.
13. **Flask** - Micro-framework web léger.
14. **Django** - Framework web complet pour le développement rapide de sites web.

#### Traitement d'image
15. **Pillow** - Manipulation et traitement d'images.
16. **OpenCV** - Vision par ordinateur et traitement d'images.

#### Automatisation
17. **Selenium** - Automatisation de navigateurs pour les tests web.
18. **Scrapy** - Framework de scraping web rapide et hautement extensible.
19. **paramiko** - Connexions SSH via Python.

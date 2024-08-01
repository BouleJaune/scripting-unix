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

def addition(a, b):
    return a + b
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




## Biblios externes utiles
numpy, django, flask, pandas, matplotlib, scipy, requests, ansible, paramiko, 

## venv, requirements.txt, poetry

## mot sur modules ruby, perl, et non existence shell

cpan unix
cpan Chocolate::Belgian

On Windows:
$ ppm
ppm> search net-smtp
ppm> install Net-SMTP-Multipart


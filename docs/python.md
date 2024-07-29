# Python - Les bases

## Introduction

Python est un langage de programmation interprété polyvalent et facile d'accès. Sa grande force réside dans sa popularité, qui lui permet d'avoir une très grande communauté prolifique sur la production de modules externes. Python est utilisé pour faire un peu de tout, du WebDev aux sciences en passant par l'IA il existe toujours plusieurs frameworks pour chaque cas d'usage.

Python est donc aussi beaucoup utilisé dans le monde de l'administration système et du DevOps. Toutes les distribution Linux possèdent Python préinstallée. 
Que ce soit pour des scripts assez simples, des utilitaires déjà developpés ou encore même du Ansible (qui est basé sur Python), Python domine le marché avec Bash.

## L'interpréteur Python

Python est donc un langage interprété, on peut lancer des scripts sans compiler au préalable dirctement via l'éxécutable ``python``. Si on lance l'exécutable sans lui fournir de commande ou de script à exécuter celui ci ouvrira un shell interactif, un peu comme Bash.
Ce shell Python est utile pour tester rapidement des commandes, checker une syntaxe ou faire des actions précises rapidement. Mais il n'est pas réellement utilisé pour de la vraie production, contrairement au shell Bash qui est beaucoup pensé pour être utilisé de manière intéractive.

L'exécutable ``python`` est la plupart du temps un lien symbolique vers le vrai exécutable qui précisera la version actuelle de Python. Cela peut être important car certains scripts ne sont pas compatibles avec des versions antérieures de Python. Par exemple les ``f-strings`` (vues plus tard) n'ont été introduites qu'à partir de python 3.6. Les versions sont cependant rétrocompatibles, ainsi fait un script en python 3.6 sera compatible avec les versions supérieure à 3.6.

Cette rétrocompatiblité n'est valable que pour Python 3. Les scripts Python 2.7 ne sont pas compatibles python 3, néanmoins il est de plus en plus rare de trouver des scripts datant de cette époque. Python 3 étant sorti en 2008 et la dernière version de python 2 (2.7) en 2010. Pendant une période les distributions Linux fournissaient les deux versions mais de nos jours il n'y a plus que python 3 de supporté, le support de python 2.7 ayant fini en 2020.

```sh
❯ ls -l $(which python)
lrwxrwxrwx 1 root root 7  7 juin  08:33 /usr/bin/python -> python3
❯ ls -l $(which python3)
lrwxrwxrwx 1 root root 10  7 juin  08:33 /usr/bin/python3 -> python3.12
❯ ls -l $(which python3.12)
-rwxr-xr-x 1 root root 14384  7 juin  08:33 /usr/bin/python3.12
```

On peut quitter l'interpréteur intéractif python avec ``<Ctrl-D>``, ``exit()`` ou encore ``quit()``.

## Quelques types builtins essentiels

Python, contrairement à Bash, est un langage "strongly typed", c'est à dire qu'il ne fonctionne pas juste avec des chaines de caractères comme Bash mais avec des ``types``.
Ainsi tout objet possède un type. Un nombre entier est par exemple de type ``int`` (pour integer), une chaîne de caractères de type ``str``.
Il est important de savoir qu'en Python ces types sont dénommés des classes. On peut utiliser la fonction ``type()`` pour voir de quel type est un objet.

```python
type(2)
<class 'int'>
type("Hello World")
<class 'str'>
```

Il y a plusieurs classes de base en Python qui viennent avec des outils de manipulation pratique de ces objets.

### Les chaines de caractères, ``str``
Une chaîne de caractères de classe ``str`` peuvent être crées de deux manières différentes. Soit en l'écrivant directement entourée de guillemets, soit en tentant de traduire un autre objet en ``str``.
```python
>>>string = "Hello world"
>>>string2 = str(2)
```
Ici, ``str(2)`` permet de traduire l'``int 2`` en ``str`` en prenant sa représentation en chaîne de caractères (simplement ``"2"``). Il n'y a pas toujours de représentation possible sous forme de ``str`` d'un objet.

On peut aussi définir des strings avec des triples guillemets ce qui permet d'écrire des chaînes de caractères sur plusieurs lignes.

```python
>>>string = ```hello
world
!!!
'''
```

Chaque ``str`` (et autres objets) possède une liste de ``methods`` qui sont des fonctions applicables sur l'objet en question.
```python
>>>"hello".capitalize()
Hello
```

Une liste exhaustive des méthodes disponibles pour ``str`` est visible dans la documentation officielle sur les types ``builtins`` : [Méthodes ``str``](https://docs.python.org/3/library/stdtypes.html#string-methods)
On y retrouve aussi les autres ``builtins`` et leur documentation.

Les ``str`` supportent quelques opérations simples avec ``+`` et ``*``. Le premier permet de concaténer deux ``str`` en un et le second de répéter un certain nombre de fois un ``str``.

```python
>>>"Ce chat est " + "très " *3 + "beau."
'Ce chat est très très très beau.'
```

### Les nombres, ``int`` et ``float``

L'un des avantages simplistes le plus rapidement visible de Python par rapport au Bash est le support natif des nombres.Il y a deux principaux types ``builtins``, ``int`` et ``float``. Le premier sert à représenter des nombres entiers et le second des nombres à virgules. Il existe un autre type, ``complex`` mais est assez rare et nécessite des connaissances mathématiques pour le comprendre.
Attention c'est un ``.`` pour délimiter les décimales en Python, comme les anglais ! 

```python
>>>type(2)
<class 'int'>
>>>type(3.14)
<class 'float'>
```

Ces types supportent des opérations algébriques classiques :  ``+``, ``-``, ``*``, ``/``, ``//`` (quotient entier), ``%`` (modulo ou reste de la division), ``abs()`` (valeur absolue), ``**`` (puissance).

``int()`` et ``float()`` permettent aussi de convertir les nombres de ``float`` à ``int`` et inversement. La conversion de ``float`` à ``int`` arrondi au passage à l'entier inférieur.
Python est en mesure de convertir automatiquement les types si nécessaire pour par exemple additionner un ``int`` avec un ``float``.

```python
>>>int(2.5)
2
>>>2.5 + 1
3.5 # Ne renvoit pas d'erreurs
>>>2.5%1
0.5
```
Enfin, on peut convertir des ``str`` vers des nombres de la même manière avec ``int()`` et ``float()``. Cela est par exemple utile à la lecture d'un fichier texte où le type par défaut sera ``str``.

```python
>>>int("2")
2
```

### Les booléens, ``bool``

Le type ``bool`` en Python représente les valeurs booléennes, qui peuvent être soit ``True`` soit ``False``. Ces valeurs sont utilisées pour exprimer des conditions logiques et sont le résultat d'expressions de comparaison ou d'opérations logiques.

Par exemple :

```python
>>> a = 5
>>> b = 10
>>> a < b
True
>>> a > b
False
```

Les booléens sont souvent utilisés dans les structures de contrôle, comme les instructions ``if``, pour prendre des décisions dans le code. 


## Types built-ins de structures de données

### Les listes, ``list``

L'un des types d'objets les plus manipulé en Python est la liste. Une liste est formé d'une succession d'objets indéxés. On peut en construire en listant des objets séparés par une virgule et en les entourants de ``[]``.

Une liste indexée, on peut donc récupérer un élément précis via son placement dans la liste. L'indexe commence à 0. Le type d'une liste est ``list``.

```python
>>>ma_liste = ["hello", 2, 2+3, "world"]
>>>ma_liste[0] # Renverra "hello"
>>>ma_liste[3] # Renverra "world"
>>>ma_liste[-1] # Renverra "world"
>>>ma_liste[0:2] # Renverra une liste avec les éléments de 0 à 2 exclus ['hello', 2]
```

Les listes comme la plupart des objets supportent des méthodes par défaut. Les méthodes les plus courantes permettent d'ajouter un élément à la liste, d'en enlever, de l'inverses etc ...

```python
ma_liste.append(3) # Ajoute à la fin de la liste un 3
ma_liste.pop(i) # Enlève l'objet à la position i
ma_liste.count(x) # Compte le nombre d'occurence de x dans la liste
ma_liste.reverse() # Inverse l'ordre de la liste
```




### tuples / sequences
### Les dictionnaires (hash map)

Une autre structure de données utile est le *dictionnaire* (de type ``dict``). Un dictionnaire est une liste où les index sont des clés compréhensibles et non juste un numéro.
```python
mon_dict = {"pays": "France", "ville": "Paris", "Rivière": "Seine"}
mon_dict["pays"] # Retournera 'France'
```

Les éléments d'un dictionnaire peuvent être ajoutés ou modifiés en utilisant la clé entre crochets.
```python
mon_dict["ville"] = Nice  # Modifie la valeur associée à la clé "ville"
mon_dict["region"] = "PACA"  # Ajoute une nouvelle paire clé-valeur
```
On peut supprimer des éléments à l'aide de la fonction ``del`` ou de la méthode ``pop()``.
```python
del d["ville"]  # Supprime la paire clé-valeur avec la clé "ville"
region = d.pop("region")  # Supprime et retourne la valeur associée à "region"
```

Methodes utiles:

- ``keys()`` : Retourne un objet vue contenant toutes les clés.
```python
cles = mon_dict.keys()   # Retourne dict_keys(['pays', 'ville', 'Rivière'])
```

- ``values()`` : Retourne un objet vue contenant toutes les valeurs.

```python
valeurs = mon_dict.values() # Retourne dict_values(['France', 'Paris', 'Seine'])
```

- ``items()`` : Retourne un objet vue contenant toutes les paires clé-valeur.

```python
paires = mon_dict.items()  # Retourne dict_items([('pays', 'France'), ('ville', 'Paris'), ('Rivière', 'Seine')])
```

Ces objets (``dict_items``, ``dict_values`` et ``dict_keys``) peuvent être convertis facilement en ``list`` :
```python
valeurs = list(mon_dict.values())
print(list) # ['France', 'Paris', 'Seine']
```

### Sets

## Structures de contrôle

### Conditons ``if``

``if`` est l'une des structures les plus connue et utile en informatique. Sur Python la syntaxe est la suivante :

```python
x = int(input("Entrez un nombre")) # Demande à l'utilisateur d'entrer un nombre (initialement en str) et le convertit en int.
if x < 0:
    print("Le nombre est négatif")
elif x > 0:
    print("Le nombre est positif")
else:
    print("Le nombre est égal à 0")
```

L'indentation en python est essentielle et est ce qui permet de définir le début et la fin des blocs de code.



### Boucles ``for``

Les boucles ``for`` en python permettent d'itérer sur un itérable, comme une liste par exemple.

```python
animaux = ["Chien", "Chat", "Poisson"]
for animal in animaux:
    print(animal)
```

Pour itérer de manière plus classique un certain nombre de fois on doit créer un itérable de cette longueur. ``range()`` est très pratique pour cela.

```python
for i in range(10)
    print(i)
```

Cette boucle itèrera 10 fois avec ``i`` allant de 0 à 9.


### Boucles ``while``

La boucle ``while`` est aussi présente en python et possède comme syntaxe : 

```python
n = 0
while n < 10: 
    print(n)
    n+=1 # équivalent plus rapide de n = n + 1
```


### Mots clés ``break`` et ``continue``

Le mot clé ``break`` permet de finir plus tôt une boucle dans son entièreté tandis que le mot clé continue permet de sauter directement à l'itération suivante.

```python
for n in range(10):
    if n == 2:
        continue
    if n == 5:
        break
    print(n)
```

Cette boucle renverra : 

```python
0
1
3
4
```


## Fonctions

Une fonction en Python est définie avec le mot clé ``def``, il est suivi du nom de la fonction et de parenthèses définissant des paramètres pour la fonction.

```python
def carre(nombre):
    if type(nombre) is int or type(nombre) is float:
    # if isinstance(nombre, (int, float)): serait plus propre
        return nombre**2
    else:
        print("Ce n'est pas un nombre")
```

Une fonction peut être terminée avec le mot clé ``return``, ce mot clé permet de renvoyer le résultat de l'expressiion du ``return`` à l'appel de la fonction. Si la fonction ne passe pas par un ``return`` elle sortira naturellement et renverra ``None``.

On appel une fonction via son nom avec des parenthèses et dans les parenthèses les paramètres voulus. Comme en mathématiques ``f`` représente la fonction et ``f(paramètres)`` représente l'image de la fonction, sa valeur traitée.

```python
>>> carre
<function carre at 0x77943898a2a0>
```
```python
>>>n = 4
>>>n2 = carre(n)
>>>print(n2)
16
```
```python
>>>n = "hello"
>>>n2 = carre(n)
Ce n'est pas un nombre
>>>print(type(n2))
<class 'NoneType'>
```

## Lire et écrire dans des fichiers

### Ouverture d'un fichier

Pour ouvrir un fichier en Python, on utilise la fonction ``open()``. Cette fonction prend deux arguments principaux : le nom du fichier et le mode d'ouverture.


```python
# Ouverture d'un fichier en lecture
fichier = open('mon_fichier.txt', 'r')

# Ouverture d'un fichier en écriture (crée le fichier s'il n'existe pas)
fichier = open('mon_fichier.txt', 'w')

# Ouverture d'un fichier en mode ajout (ajoute à la fin du fichier)
fichier = open('mon_fichier.txt', 'a')
```

### Lecture de fichier

Pour lire le contenu d'un fichier, on peut utiliser différentes méthodes :

```python

# Lire tout le contenu
contenu = fichier.read()

# Lire ligne par ligne
ligne = fichier.readline()

# Lire toutes les lignes dans une liste
lignes = fichier.readlines()
```
Exemple :

```python
with open('mon_fichier.txt', 'r') as fichier:
    contenu = fichier.read()
    print(contenu)
```

### Écriture dans un fichier

Pour écrire dans un fichier, on utilise la méthode ``write()``.

```python

with open('mon_fichier.txt', 'w') as fichier:
    fichier.write('Bonjour, monde!\n')
    fichier.write('Voici une autre ligne.')
```

En mode ``'w'``, si le fichier n'existe pas, il est créé. Si le fichier existe déjà, son contenu est écrasé.

### Fermeture d'un fichier

Il est crucial de fermer un fichier après avoir fini de l'utiliser pour libérer les ressources. Cela peut se faire avec la méthode ``close()`` ou automatiquement avec une clause ``with`` :

```python
fichier.close()
```

Cependant, l'utilisation de ``with`` est préférable car elle assure que le fichier est correctement fermé même si une erreur survient pendant les opérations de lecture ou d'écriture.




## Erreurs et exceptions

La gestion des exceptions en Python est une partie essentielle du langage, permettant de gérer les erreurs de manière élégante et de maintenir le bon fonctionnement du programme. Voici un aperçu des concepts et pratiques de base pour gérer les exceptions.

Une exception est une erreur détectée lors de l'exécution d'un programme. Python utilise un modèle basé sur la levée et la gestion d'exceptions pour gérer ces erreurs.

### Structure try-except

Pour capturer et gérer les exceptions, on utilise les blocs ``try-except``. Le code susceptible de provoquer une exception est placé dans le bloc ``try``, et le bloc ``except`` est utilisé pour gérer l'erreur.

```python
try:
    # Code pouvant provoquer une exception
    result = 10 / 0
except ZeroDivisionError:
    # Code exécuté si une exception de type ZeroDivisionError est levée
    print("Erreur : division par zéro.")
```
Dans cet exemple, la division par zéro lève une exception ``ZeroDivisionError``, qui est ensuite capturée par le bloc ``except``.

### Gestion de Plusieurs Exceptions

Il est possible de gérer plusieurs types d'exceptions en utilisant plusieurs blocs ``except``.

```python
try:
    fichier = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé.")
except IOError:
    print("Une erreur d'entrée/sortie est survenue.")
```

Ici, on gère spécifiquement les exceptions ``FileNotFoundError`` et ``IOError``.

### Utilisation de ``else`` et ``finally``

Le bloc ``else`` est exécuté si aucune exception n'est levée dans le bloc ``try``. Le bloc ``finally`` est exécuté en toutes circonstances, qu'une exception ait été levée ou non, et est typiquement utilisé pour le nettoyage, comme la fermeture de fichiers ou la libération de ressources.

```python
try:
    fichier = open('mon_fichier.txt', 'r')
    contenu = fichier.read()
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé.")
else:
    print("Le fichier a été lu avec succès.")
finally:
    if 'fichier' in locals():
        fichier.close()
    print("Le fichier est fermé.")
```

### Levée d'Exceptions

Il est possible de lever des exceptions manuellement avec l'instruction ``raise``.

```python
def verifie_age(age):
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif.")
    return age

try:
    verifie_age(-1)
except ValueError as e:
    print(e)
```

Dans cet exemple, une exception ``ValueError`` est levée si l'âge est négatif.

## Classes
### Ptite prez POO
### Class objet
### Instance objet
### Héritage
### Iterators / generators

## Modules => voir si c'est pas une autre partie entière
modules internes d'un projet (multi fichiers)
modules externes
standard modules
import * bad


## Librairie standard
OS interface, math, compression
...




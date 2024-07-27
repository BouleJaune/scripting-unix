# Python - Les bases

## Présentation de Python
## Variables et expressions
## Les tableaux, les chaînes de caractères
## Les instructions de contrôle
## Les dictionnaires (hash)


https://docs.python.org/3/tutorial/index.html

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

### Les nombres, int et float

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


## Structures de données

### Listes

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

Une autre structure de données utile est le *dictionnaire* (de type ``dict``). Un dictionnare est une liste où les index sont des clefs compréhensibles et non juste un numéro.

```python
>>>mon_dict = {"pays": "France", "ville": "Paris", "Rivière": "Seine"}
>>>mon_dict["pays"] # Retournera 'France'
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

L'indentation en python est essentiel et est ce qui permet de définir le début et la fin des blocs de code.



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


### Mots clefs ``break`` et ``continue``

Le mot clef ``break`` permet de finir plus tôt une boucle dans son entièreté tandis que le mot clef continue permet de sauter directement à l'itération suivante.

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


### Match
## Fonctions

## Input et output
### strings format
f strings, .format, 
### Lire et écrire dans des fichiers

## Errors et exceptions

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




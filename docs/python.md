# Python - Les bases

## Présentation de Python
## Variables et expressions
## Les tableaux, les chaînes de caractères
## Les instructions de contrôle
## Les dictionnaires (hash)


https://docs.python.org/3/tutorial/index.html

## Introduction rapide

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

### Nombres, texte, lists

## Structures de contrôle
### if
### for
### range
### break, continue, else on loops, pass
### Match
## Fonctions
## Types
## Data structures 
new vs bash parceque avant tout strings

### Listes
as stacks as queues
### tuples / sequences
### Sets
### Les dictionnaires (hash)

## Modules => voir si c'est pas une autre partie entière
modules internes d'un projet (multi fichiers)
modules externes
standard modules
import * bad


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

## Librairie standard
OS interface, math, compression
...




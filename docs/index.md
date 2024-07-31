# Introduction

Les objectifs de la formation

Connaître les caractéristiques des principaux outils de scripting Unix/Linux

Savoir lire des scripts Unix/Linux écrits en Shell, Perl, Python Ruby ou AWK

Être capable d'écrire des scripts simples d'exploitation Unix/Linux

Comprendre comment choisir l'outil le plus adapté pour résoudre un problème particulier


Prez perso et demander le niveau des gens




# Le langage Perl - les bases
Prez, utilité de nos jours, spécifité

Présentation de Perl

Les variables scalaires, les tableaux, les opérateurs

Les instructions de contrôle

Les tableaux associatifs (hash)

# Le langage Ruby - les bases
Présentation de Ruby
Les variables
Les chaînes de caractères\\
Les structures de contrôle\\
Les tableaux, les itérateurs - Les hash\\

# Le langage Python - les bases
Python est un langage de programmation interprété à usage extrêmement populaire de nos jours.
Sa facilité facilité d'apprentissage et de lecture est ce qui a fait sa popularité initiale, aujourd'hui c'est la communauté qui en fait sa force avec les milliers de modules et programmes Python disponibles.

Pour un administrateur système et/ou un devops Python est un langage très attirant, son principal défaut, la potentielle lenteur au runtime, n'est pas un problème dans nos cas d'usage. Python est aussi ce qui est derrière Ansible et permet la création de modules Ansible customs, le plus important outil d'infrastructure as code (IAC) du moment.
Il est aussi par défaut installé sur la très grande majorité des distributions Linux.

## Syntaxe
Variables et expressions\\
Les tableaux, les chaînes de caractères\\
Les instructions de contrôle\\
Les dictionnaires (hash)\\

## Exercices Python



# Les expressions régulières (RegExp)
regex car tout est texte
Importance de grep et sed 
RegExp en Shell (via grep et sed)\\
RegExp en Perl (normes)\\
RegExp en Python (module re mais osef)\\

# La modularité en Shell, Perl, Python et Ruby

parler de direnv, de requirements.txt, de venv python, de classes python (osef un peu)
y a des trucs pour shell (bpkg) mais pas le but, illogique, shell = spécifique task

Les fonctions => dans les parties syntaxes\\
Les paquetages=> oui\\
L'approche objet => syntaxe\\
Utilisation de bibliothèques externes=> oui\\



# La programmation parallèle en Shell, Perl, Python et Ruby

différentes concurrency
xargs pipes et parallel et & + wait pour shell
multi-threading et async pour python

# Résoudre des problèmes avec le Shell, Perl, Python et Ruby

Ecrire des scripts d'exploitation (activer une application, les signaux, ...)\\
Manipuler des fichiers\\
Faire des calculs\\
Ecrire des CGI Web\\
Accéder à des bases de données\\
Manipuler des fichiers XML (parsing, validation, création)\\
Créer des applications réseaux TCP/IP\\

Ptit serveur web
Génération de fichier dans un dossier
service shell filewatcher qui trigger un truc
xargs et des pipes pour multiprocessing
perl ou grep pour regex
awk pour un truc

9 - AWK : un sous-ensemble POSIX/ISO du langage Perl

10 - Conclusion


# Quel outil pour quoi faire?

## Intérets des Shells Unix
Le shell malgré sa syntaxe archaique et ses fonctionnalités limitées vis à vis de langages interprétés à usage général a tout de même encore des avantages.

## Actions uniques
Utile lorsque l'on veut faire une tâche relativement simple que quelques fois. 
Maitriser le shell permet d'être beaucoup plus rapide dans un environnement Unix
Exemple: extraire des données textes et les process sommairement
``cat / sed / cut / tr`` ...

### Manipulation de binaires

L'une des force de Bash par rapport à d'autres langages et sa facilité à manipuler directement des binaires. En python, par exemple, on peut aussi manipuler des binaires, mais on sent clairement que cela est moins pensé pour.
Exemple : Utiliser un exécutable propriétaire (import baroc), utiliser l'output d'un script python et l'injecter ailleurs etc


### Manipulation de texte

Tout est texte
Exemple : lire des logs

### Manipulation OS linux
les deux derniers ~= Manipulation linux pur car linux déjà tout fichiers et texte + binaires unix


Philo kiss, pleins de petits binaires linux avec une seule tache, trop complexe go python

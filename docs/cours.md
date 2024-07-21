# Introduction

Les objectifs de la formation

Connaître les caractéristiques des principaux outils de scripting Unix/Linux

Savoir lire des scripts Unix/Linux écrits en Shell, Perl, Python Ruby ou AWK

Être capable d'écrire des scripts simples d'exploitation Unix/Linux

Comprendre comment choisir l'outil le plus adapté pour résoudre un problème particulier


Prez perso et demander le niveau des gens

# Le Shell - les bases

## Qu'est ce qu'un shell

Un shell Unix est une interface homme machine (IHM) en ligne de commande (CLI). Il fournit à la fois un langage de commandes interactives et un langage de scripting. Le shell traite des commandes ou scripts.

Il ne faut pas confondre un shell avec un terminal. Un terminal était initialement physiquement un écran et un clavier. Aujourd'hui lorsque l'on parle de terminal on parle d'émulateur de terminal, c'est une catégorie de logiciels permettant de fournir un GUI pour lancer des shells (bash, python, zsh, fish, powershell, ruby ...).  
Émulateur de terminaux connus : alacritty, Windows Terminal, urxvt, GNOME Terminal, PuTTY.

La confusion est courante car sur Windows historiquement le nom du shell et de l'émulateur de terminal étaient les mêmes (cmd, powershell...), ce n'est plus le cas avec Windows 11 et le Windows Terminal.


## Différents shells Unix

"sh" (shell command langage) est un spécification de langage défini par POSIX mais n'est pas une implémentation en lui même. Il y a diverses implémentations, la plus connue étannt Bash.
Le fichier ``/bin/sh`` est en réalité un lien symbolique vers une implémentation sur la plupart des systèmes Linux, souvent bash. ``ls -l /bin/sh``
Bash est l'implémentation la plus connue et utilisée, nous utiliserons donc Bash au cours de cours.
Quelques autres implémentations connues sont Ksh (Korn Shell), qui est une implémentation plus ancienne que Bash et surtout présente sur des systèmes moins récents.
Zsh est l'implémentation par défaut sur MacOS et offre aussi des fonctionnalités pratiques en mode intéractif (complétion tab avec un menu naviguable ou encore une forte customisabilité par exemple).

Quasiment tout les shells Unix suivent a minima ce qui est décrit par POSIX, la plupart rajoutent ensuite diverses fonctionnalités. Lorsque l'on fait un script qui serait amené à être utilisé sur divers systèmes qui n'auraient pas forcément le même shell il peut être judicieux de se contenter d'utiliser ce que POSIX décrit.
Exemple de fonctionnalité disponible sur Bash et qui n'est pas "POSIX compliant" : 
``test`` et ``[]`` sont POSIX compliant mais ``[[]]`` ne l'est pas. Les deux premiers sont strictements pareils, ``[`` étant un alias de test, le dernier permet notamment d'utiliser des "Wildcards Patterns" comme ``*``.

Pour information lancer un script via /bin/sh avec /bin/sh étant un symlink vers bash va lancer bash en mode posix ce qui rendra bash le plus POSIX compliant possible.
[Bash POSIX Mode](https://www.gnu.org/software/bash/manual/html_node/Bash-POSIX-Mode.html)

En pratique il est rare d'utiliser des fonctionnalités non disponibles sur d'autres shell tout comme il est au final rare d'utiliser autre chose que Bash, néanmoins il peut être utile de garder ceci dans un coin de la tête.

## Rappels Linux essentiels pour le scripting

Il y a plusieurs aspects de Linux qui sont importants à comprendre pour mieux comprendre le scripting sous Unix.

stdin / stdout / stderr
recup stdout et in des process dans /proc/pid/fd/1 et 2

return code, 
droits fichiers, +x, shebang

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


## Détails syntaxiques
### Redirections et charactères spéciaux

Les flux standards sur Linux sont le standard out (``stdout``), standard error (``stderr``) et standard input (``stdin``). Normalement chaque process Linux possède un flux de chaque par défaut.

Ces flux servent à transmettre des données entre une source et une sortie. 
Les données sur linux sont toujours du texte et la commande lancée représente une des extrémités de ces flux.

Le ``stdin`` est le flux d'entrée dans la commande lancée, le ``stdout`` la sortie normale de la comande et le ``stderr`` est le canal pour les erreurs.\\
Par défaut le ``stdout`` et le ``stderr`` sont envoyés dans le terminal en cours. On peut rediriger ces sorties vers d'autres scripts, commandes ou fichiers.\\

Sur Linux tout est un fichier, même ces trois flux, ils sont dénommés ``0`` pour le ``stdin``, ``1`` pour le ``stdout`` et ``2`` pour le ``stderr``. Ces fichiers sont situés dans ``/proc/PID/fd``. 


Redirection vers un fichier: 

On peut utiliser ``>`` et ``>>`` pour rediriger le stdout vers un fichier, les doubles chevrons permettent d'ajouter à la fin d'un fichier déjà existant tandis que le simple chevron écrase le fichier. Dans les deux cas si le fichier n'existait pas il sera créé.

Cela ne redirige pas le ``stderr`` par défaut.
Script d'exemple : 
```sh
\#!/bin/sh
echo hello world
cat nexistepas 
```

```sh
chmod +x test.sh
./test.sh > out
```


On peut expliciter ce qui est redirigé en précisant le numéro du fichier correspondant.
```sh
./test.sh 2> errors
./test.sh 1> out
./test.sh 1> out 2> errors
```

Si on veut rediriger à la fois le ``stdout`` et le ``stderr`` vers le même fichier avec une syntaxe plus courte que d'écrire deux fois le fichier on peut faire : 
```sh
./test.sh > out 2>\&1
```
Cela dit au shell de rediriger ``2`` (``stderr``) vers la même sortie que ``1`` (``stdout``). 

Le ``stdin`` est un peu plus complexe à visualiser sans redirection, par défaut celui ci étant le clavier.

On peut aussi le rediriger, donc ne plus avoir le clavier comme input mais un fichier ou la sortie d'autre processus.

Commençons par créer un fichier d'inputs: 
```sh
seq 10 > input
```

La commande ``grep PATTERN FILE`` permet de récupérer dans du texte les lignes matchant un pattern.
Elle accepte le nom d'un fichier en entrée, on peut donc faire ``grep 5 input`` pour récupérer la ligne où le ``5`` est présent. Néanmoins si aucun fichier n'est fourni il va chercher à match dans le stdin.

```sh
grep 5
```


On peut donc lui rediriger le stdin pour lui fournir notre fichier input de cette manière. Pour cela on utilise encore une fois des chevrons, mais cette fois ci dans l'autre sens.
grep 5 < input

Il est à noter que ces redirections peuvent être placées n'importe où dans la commande, cela est aussi vrai pour les redirections de stderr et stdout.
```sh
< input grep 5
grep < input 5
grep 2>err 1>out < input 5
```
On peut aussi rediriger la même sortie vers plusieurs fichiers différents.
```sh
cat input >out >out2
```

# Pipelines linux

Les pipes Linux permettent de rediriger le ``stdout`` d'une première commande vers le ``stdin`` d'une seconde commande. Cela permet de chaîner des processus et de gagner beaucoup de temps.

```sh
ls / | grep dev
systemctl | grep service
```

Ou encore une un peu plus élaborée : 
```sh
systemctl | grep service | cut -d "." -f 1 | xargs
```

Il est possible de rediriger aussi le ``stderr`` dans une pipe, soit en le redirigeant simplement vers le ``stdout`` soit en utilisant ``|&``
```sh
❯cat nexistepas | grep "Aucun fichier" -c
cat: nexistepas: Aucun fichier ou dossier de ce nom
0
```
```sh
❯cat nexistepas |& grep "Aucun fichier" -c
1
```
```sh
❯cat nexistepas 2>&1 | grep "Aucun fichier" -c
1
```

L'option ``-c`` de ``grep`` permet de compter le nombre correspondance avec le pattern voulu. On voit que dans le premier cas le ``stderr`` est affiché dans le terminal tandis que dans les suivants il est envoyé dans le ``stdin`` du ``grep``.

Un point important qui sera revu dans la partie _parallélisme_ est le fait que chacun des processus d'une série de pipes est lancé dès le début. Les process n'attendent pas que le précédent soit fini pour démarrer.
La plupart des commandes linux classiques vont traiter les données en entrée (``stdin``) ligne par ligne et envoyer en sortie (``stdout``) aussi ligne par ligne. Le temps d'exécution est donc minoré par le processus le plus long et n'est donc pas la somme du temps d'exécution de chaque processus.

La commande ``time`` permet de mesurer le temps d'exécution d'une commande et donc de visualiser cette parallélisation.

```sh
❯time (sleep 5 | sleep 5)
( sleep 5 | sleep 5; )  0,00s user 0,00s system 0% cpu 5,002 total
```

On voit bien que la pipeline s'est exécutée en 5.002 secondes, soit le temps d'un ``sleep 5`` et non la somme des deux (à 0.001s près). Dans cet exemple les deux processus sont indépendants et il n'y a pas d'intérêts à la connexion du ``stdout`` du premier processus au ``stdin`` du second.

## Commande et process subsitutions

### Substitution de commandes

Parfois on peut avoir envie de remplacer une partie d'une commande par le résultat d'autres commandes. On peut faire ceci via une substitution de commandes qui a pour syntaxe ``$(commandes)`` ou ``` `commandes` ```, les deux syntaxes sont fonctionnellement pareils.

```sh
echo Le chemin du dossier actuel est $(pwd)
```
La commande ``pwd`` signifie "print working directory" et affiche donc le chemin complet du dossier actuel.

On peut aussi substituer une pipeline de commandes qui renverra le ``stdout`` final.
```sh
echo "Le système d'exploitation est `uname -a | cut -d ' ' -f 1`"
```

### Substitution de processus

La substitution de commande permet de remplacer par le ``stdout`` de la commande mais parfois on ne veut pas directement ce ``stdout`` mais on veut plutôt un fichier contenant ce contenu. 
On peut faire cela via une substitution de processus qui a pour syntaxe ``<(commande)``.


Ici la variable ``--kubeconfig`` attends un nom de fichier et pas directement son contenu, cependant nous possédons le contenu du kubeconfig dans une variable. On utilise donc une substitution de process. 

```sh
kubectl --kubeconfig <(echo $CONTENU_KUBECONFIG) apply -f dep.yml
```


## Code de retour et opérateurs && et ||

Lorsqu'une commande finit de s'éxécuter elle va renvoyer un code de retour qui dépendra de son état de sortie.
Si tout s'est bien passé celui ci sera égal à ``0``, sinon, il sera souvent ``1`` ou un autre nombre en fonction de la commande en elle même.
Ce code est automatiquement stocké dans la variable ``$?`` pour chaque commande et permet donc de faire des actions en fonction de sa valeur.
Naturellement on peut imaginer utiliser une structure de contrôle tel qu'un ``if else`` pour manipuler ces codes de retour. Cependant Bash fournit une alternative plus pratique pour des cas simples avec ``&&`` et ``||``.

L'opérateur Bash AND ``&&`` permet d'éxécuter la commande à droite de l'opérateur si et seulement si la commande à gauche a un code de retour à ``0``, tandis que l'opérateur OR ``||`` exécutera la commande à droite si et seulement si la commande à gauche a un code de retour différent de ``0``.

```sh
❯ls && echo "La commande est passée" || echo "La commande n'est pas passée"
Vos fichiers
La commande est passée
```

```sh
❯cat nexistepas && echocat: nexistepas: Aucun fichier ou dossier de ce nom
La commande n'est pas passée "La commande est passée" || echo "La commande n'est pas passée"
```

Ces opérateurs ont une associativité par la gauche. Cela permet donc d'utiliser en premier ``&&`` puis ``||`` pour traiter tout les cas en une ligne.
Rappel associativité gauche : ``a ~ b ~ c = (a ~ b)~c``

Cela implique qu'il faut donc mettre le ``&&`` *avant* le ``||``.

```sh
❯cat nexistepas || echo "La commande n'est pas passée" && echo "La commande est passée" 
cat: nexistepas: Aucun fichier ou dossier de ce nom
La commande n'est pas passée
La commande est passée
```

### charac spéciaux

Les caractères spéciaux (jokers, échappements)

### Structures de contrôle

#### Les tests
La commande ``test`` permet de tester si une expression est vraie ou fausse. Test renverra un code de retour de ``0`` si vraie et ``1`` si faux.

```sh
❯test a = a
echo $?
0
```

Les expressions se construisent via des opérateurs de test qui sont, notamment : 

-  ``a = b`` et ``a != b`` testent si les chaines de charactères ``a`` et ``ab`` sont respectivement égales et inégales
- ``-z a`` et ``-n a`` respectivement testent si la chaine de charactères ``a`` est vide et ne l'est pas
- ``n1 -eq n2`` et ``n1 -ne n2`` testent l'égalité et l'inégalité de deux nombres
- ``n1 -lt n2`` et ``n1 -gt n2`` testent si ``n1`` est strictement plus petit que ``n2`` pour ``-lt`` et strictement plus grand pour ``-gt``.
- ``n1 -le n2`` et ``n1 -ge n2`` pareil mais inférieur/supérieur ou égal.

Il y aussi des opérateurs purement logiques qui permettent de combiner plusieurs expressions entre elles:
``! e`` si ``e`` renvoi vrai si ``e`` est fausse et inversement.
``e1 -a e2``  renvoi vrai si et seulement si ``e1`` et ``e2`` sont vrais.
``e1 -o e2`` renvoi vrai si ``e1`` ou ``e2`` ou les deux sont vrais.

Exemples : 
```sh
❯test  5 -eq 2 -a 5 -eq 5
echo $?
1
```
```sh
❯test 5 -eq 2 -o 5 -eq 5
echo $?
0
```
Plus d'opérateurs pour construire des expressions sont disponibles sur le manuel de la commande (``man test``).

La plupart du temps la commande ``test`` n'est pas utilisée avec cette syntaxe. Son autre syntaxe plus commune est ``[`` : 
```sh
[ "hello" = "world" ] 
```
Les espaces après ``[`` et avant ``]`` sont importants. Ce serait comme écrire ``test"hello" = "world"`` ce qui ne peut pas fonctionner.

Il existe aussi une autre notation ``[[`` qui apporte plus de fonctionnalités cependant cette version de ``test`` n'est pas POSIX. L'une de ces fonctionnalités est notamment le support du joker ``*``.

```sh
A="VARIABLE_TEST"
[ $A = *TEST* ] => ne fonctionnera pas
[[ $A = *TEST* ]] => fonctionne
```

#### Structure if

Les ``test`` sont le plus souvent utilisés avec la structure de contrôle ``if``. Cette structure permet d'exécuter des actions si et seulement si la commande à droite de ``if`` a un code de retour de ``0``. 

La syntaxe est la suivante : 
```sh
A="VARIABLE_TEST"
if [[ $A = *TEST* ]]
then
    echo $A contient TEST
fi
```

On peut rajouter des ``else`` pour faire une action dans le cas où le code de retour n'est pas ``0`` et même refaire directement un autre ``if`` avec ``elif``.

```sh
A="VARIABLE_TEST"
if [[ $A = *HELLO* ]]
then
    echo $A contient HELLO
elif [[ $A = *WORLD* ]]
then
    echo $A contient WORLD
else
    echo $A ne contient ni HELLO ni WORLD
fi
```

#### Switch case

Parfois on veut faire plusieurs tests en une seule fois, par exemple si l'on veut traiter les options d'entrée d'un script ou encore comparer une variable avec plusieurs autres.
On peut faire ceci avec un ``switch case``. On peut ainsi réécrire l'exemple précédent de cette manière :

```sh
A="VARIABLE_TEST"
case $A in
    HELLO) 
        echo $A contient HELLO
        ;;
    WORLD) 
        echo $A contient WORLD
        ;;
    *)
        echo $A ne contient pas HELLO ni WORLD
        ;;
esac
```

Ces ``switch case`` sont très souvent utilisés pour traiter les options d'entrées d'un script.

#### Les boucles
Les boucles sont des structures de contrôles permettant d'itérer plusieurs fois une même action. 
Il y a divers types de boucles. L'une d'elles est la boucle ``while``. Celle si itèrera tant que la condition à sa droite sera vraie.

```sh
n=0
while [ $n -ne 10 ]
do
    n=$(seq 10 | shuf -n 1)
    echo Nombre aléatoire  $n
done
```

``seq 10`` permet de générer une liste de 1 à 10, ``shuf -n 1`` permet d'en sélectionner un aléatoirement. Cette boucle ``while`` tournera donc tant que l'on ne tombe pas aléatoirement sur ``n=10``.

Une boucle très similaire est ``until``, qui fait exactement l'opposé et itère tant que sa condition n'est *pas* vraie.

```sh
n=0
until [ $n -eq 10 ]
do
    n=$(seq 10 | shuf -n 1)
    echo Nombre aléatoire  $n
done
```

Le dernier type de boucle est la boucle ``for``, celle ci permet d'itérer au travers de, par exemple, une liste.
Cela permet soit de parcourir une liste et avoir une variable fixée sur la valeur en cours :


```sh
for i in bash linux script
do
    echo "Cette boucle listera les mots de la liste : $i"
done
```

Soit de contrôler le nombre d'itération d'une action :

```sh
for i in {1..5}
do
    echo "Cette boucle s'exécutera 5 fois, $i"
done
```

```sh
for i in {1..5}
do
    echo "Cette boucle s'exécutera 5 fois, $i"
done
```


Parfois on veut pouvoir sortir plus tôt d'une boucle ou bien passer directement à l'itération suivante. On peut faire cela respectivement grâce à ``break`` et ``continue``.

```sh
for i in {1..8}
do
    if [ $i -eq 3 ] 
    then
        continue #Permet de skipper le reste de cette itération
    fi
    if [ $i -eq 5 ]
    then
        break #Sortira définitivement de la boucle
    fi
    echo "Le nombre est $i"
done
```
Donnera : 
```sh
Le nombre est 1
Le nombre est 2
Le nombre est 4
```

### Variables
((var++))
$? et $1..3


### Fonctions


## Binaires utiles

Force et efficience des binaires linux
cut, cat, echo, grep, tr, sed, xargs, tail, df, ls
diff

man ! RTFM

## Exercices

Récupérer la liste des pourcentages de remplissages des filesystems

### Script

### Sans scripts

```sh
df | tail -n +2 | tr -s " " | cut -d " " -f 5
```


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

Quel outil pour quoi faire?


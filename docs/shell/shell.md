# Le Shell - les bases

## Qu'est ce qu'un shell

Un shell Unix est une interface homme machine (IHM) en ligne de commande (CLI). Il fournit à la fois un langage de commandes interactives et un langage de scripting. Le shell traite des commandes ou scripts.

Il ne faut pas confondre un shell avec un terminal. Un terminal était initialement physiquement un écran et un clavier. Aujourd'hui lorsque l'on parle de terminal on parle d'émulateur de terminal, c'est une catégorie de logiciels permettant de fournir un GUI pour lancer des shells (bash, python, zsh, fish, powershell, ruby ...).  
Émulateur de terminaux connus : alacritty, Windows Terminal, urxvt, GNOME Terminal, PuTTY.

La confusion est courante car sur Windows historiquement le nom du shell et de l'émulateur de terminal étaient les mêmes (cmd, powershell...), ce n'est plus le cas avec Windows 11 et le Windows Terminal.


## Différents shells Unix

``sh`` (shell command langage) est une spécification de langage définie par POSIX mais n'est pas une implémentation en elle même. Il y a diverses implémentations, la plus connue étannt Bash.
Le fichier ``/bin/sh`` est en réalité un lien symbolique vers une implémentation sur la plupart des systèmes Linux, souvent bash. ``ls -l /bin/sh``
Bash est l'implémentation la plus connue et utilisée, nous utiliserons donc Bash au cours de cours.
Quelques autres implémentations connues sont Ksh (Korn Shell), qui est une implémentation plus ancienne que Bash et surtout présente sur des systèmes moins récents.
Zsh est l'implémentation par défaut sur MacOS et offre aussi des fonctionnalités pratiques en mode intéractif (complétion tab avec un menu navigable ou encore une forte customisabilité par exemple).

Quasiment tout les shells Unix suivent a minima ce qui est décrit par POSIX, la plupart rajoutent ensuite diverses fonctionnalités. Lorsque l'on fait un script qui serait amené à être utilisé sur divers systèmes qui n'auraient pas forcément le même shell il peut être judicieux de se contenter d'utiliser ce que POSIX décrit.
Exemple de fonctionnalité disponible sur Bash et qui n'est pas "POSIX compliant" : 
``test`` et ``[]`` sont POSIX compliant mais ``[[]]`` ne l'est pas. Les deux premiers sont strictements pareils, ``[`` étant un alias de test, le dernier permet notamment d'utiliser des "Wildcards Patterns" comme ``*``.

Pour information lancer un script via /bin/sh avec /bin/sh étant un symlink vers bash va lancer bash en mode posix ce qui rendra bash le plus POSIX compliant possible.
[Bash POSIX Mode](https://www.gnu.org/software/bash/manual/html_node/Bash-POSIX-Mode.html)

En pratique il est rare d'utiliser des fonctionnalités non disponibles sur d'autres shell tout comme il est au final rare d'utiliser autre chose que Bash, néanmoins il peut être utile de garder ceci dans un coin de la tête.

## Rendre un script exécutable

Pour qu'un script soit éxécutable sur Linux, que ce soit un script Shell, Python ou autre, il faut que celui-ci ait des droits d'exécution.
Pour vérifier qu'un fichier possède ces droits on peut utiliser ``ls -l script.sh`` pour lister ses permissions.

Si un script de ne les possède pas on peut les rajouter avec ``chmod +x script.sh``. Cela rajoutera pour tout le monde les permissions. Par défaut sur linux les permissions sont gérables à trois niveau, le propriétaire du fichier, le groupe du fichier et tout le monde.

Si l'on veut rajouter le ``x``, l'exécution, sur un type précis on peut le préciser avec la lettre correspondante. ``o`` pour tout le monde (others), ``g`` pour groupe et ``u`` pour le propriétaire (user).



```sh
❯ ls -l script.sh
-rw-r--r-- 1 root root 0 23 mai 23:00 script.sh
```
Le script n'a pas de x dans ses permissions
```
❯ chmod ug+x script.sh
❯ ls -l script.sh
-rwxr-xr-- 1 root root 0 23 mai 23:00 script.sh
```
Le script a des permissions d'exécution sur l'user et le groupe.

Une fois un script rendu exécutable on peut le lancer en mettant directement son chemin dans le shell.

Soit de manière absolue ou encore de manière relative.
```sh
/chemin/vers/le/script.sh
./script.sh
```
La méthode relative est, justement, relative à la position actuelle du terminal. ``.`` représente dans le shell le dossier actuel, donc si vous ne vous situez pas au bon endroit cela ne fonctionnera pas.

``..`` représente le dossier avant le dossier actuel, on peut utiliser les deux pour atteindre n'importe quel fichier du système mais il est parfois plus simple d'utiliser le chemin entier.


Lorsque le script est appelé le shell va chercher un logiciel avec lequel lire notre script. Cela peut par exemple être python ou bash. Par défaut Linux va tenter d'exécuter le script avec le shell actuel, donc bash si c'est un shell bash par exemple. Ce qui n'est pas très fiable ni possible pour un script autre que bash.

Pour cela on peut ``#!`` tout au début du script suivi du binaire voulu, ceci est appelé un ``shebang``.
```sh
#!/usr/bin/python3

...contenu du script....
```

Enfin une autre manière d'utiliser un script sans shebang ni permissions d'exécution et de directement l'appeler avec le binaire voulu.
```sh
bash script.sh
python script.py
```

### Exercice
Créer un fichier script.sh utilisant la commande ``echo`` et l'exécuter via la commande ``bash`` et directement grâce au shebang.

??? Note "Exemple de solution"
    Ouvrir un éditeur de texte en ligne de commande
    ```sh
    vim script.sh
    ```
    Contenu du script : 
    ```sh
    #!/bin/bash
    echo Premier script !
    ```
    ``i`` pour rentrer en mode insertion, ``esc`` pour revenir en mode normal, ``:wq`` pour enregistrer et quitter.
    ```sh
    ❯bash script.sh
    Premier script !
    ❯chmod +x script.sh
    ❯./script.sh
    Premier script !
    ```

## Caractères spéciaux

Dans un shell Linux certains caractères ont une signification spéciale, en voici une liste non exhaustive. 

- ``~`` "Tilde". Répertoire personnel, la plupart du temps /home/user.
- `` ` `` "Backtick". Utile pour ouvrir et fermé des substitutions de commandes.
- `` # `` Marque le début d'un commentaire.
- `` | `` Caractère pipe, permet de faire des pipes Unix.
- `` * `` Caractère joker (wildcard), permet de se substituer n'importe quelle suite de caractères. (``ls fichiers_* `` par exemple)
- `` ? `` Permet de se substituer à un seul caractère.
- ``'`` et ``"`` Permet de délimiter des chaînes de caractères, utile par exemple pour des chaînes comportant des espaces. (``ls "/fichier/avec/un espace"``)
- `` ; `` Défini la fin d'une commande. Utile pour faire plusieurs commandes sur une seule ligne sans lien logique entre elles.
- `` \ `` Permet d'échapper un caractère pour lui enlever son effet "spécial". (``echo L\'apostrophe peut se mettre comme ceci``)

## Redirections 

Les flux standards sur Linux sont le standard out (``stdout``), standard error (``stderr``) et standard input (``stdin``). Normalement chaque processus Linux possède un flux de chaque par défaut.

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

Enfin parfois on veut entièrement caché quelque chose. Il existe pour cela un fichier ``/dev/null`` sur Linux pensé pour ceci. Un exemple d'utilisation et de ``grep`` dans un dossier ne contenant pas que des fichiers textes ce qui renverra des erreurs inutiles, qui peuvent être cachées en redirigeant ``stderr`` vers ``/dev/null``.

```sh
grep -r PATTERN . 2>/dev/null
```

## Pipelines linux

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

Un point important qui sera revu dans la partie _parallélisme_ est le fait que chacun des processus d'une série de pipes est lancé dès le début. Les processus n'attendent pas que le précédent soit fini pour démarrer.
La plupart des commandes linux classiques vont traiter les données en entrée (``stdin``) ligne par ligne et envoyer en sortie (``stdout``) aussi ligne par ligne. Le temps d'exécution est donc minoré par le processus le plus long et n'est donc pas la somme du temps d'exécution de chaque processus.

La commande ``time`` permet de mesurer le temps d'exécution d'une commande et donc de visualiser cette parallélisation.

```sh
❯time (sleep 5 | sleep 5)
( sleep 5 | sleep 5; )  0,00s user 0,00s system 0% cpu 5,002 total
```

On voit bien que la pipeline s'est exécutée en 5.002 secondes, soit le temps d'un ``sleep 5`` et non la somme des deux (à 0.001s près). Dans cet exemple les deux processus sont indépendants et il n'y a pas d'intérêts à la connexion du ``stdout`` du premier processus au ``stdin`` du second.

## Commande et processus subsitution

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
*Vos fichiers*
La commande est passée
```

```sh
❯cat nexistepas && echo "La commande est passée" || echo "La commande n'est pas passée"
cat: nexistepas: Aucun fichier ou dossier de ce nom
La commande n'est pas passée
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


## Structures de contrôle

### Les tests
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

### Structure if

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

### Switch case

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

### Les boucles
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

## Variables

On peut définir une variable de cette manière : 

```sh
VARIABLE="contenu de la variable"
```

If faut noter qu'il n'y a pas d'espace de part et d'autre du ``=`` et que toutes les variables sont stockées en tant que chaîne de caractères.

On peut aussi définir des variables en demandant dynamiquement à l'utilisateur de les remplir grâce à ``read``. 

```sh
read VARIABLE
```

Pour utiliser une variable il faut rappeler son nom avec un ``$`` devant. Cependant dans certains cas il peut être nécessaire d'encapsuler le nom de la variable dans ``{}``.

```sh
KERNEL="Linux-6.9.9"
echo Le kernel est $KERNEL
echo Créons un fichier nommé $KERNEL_file # Renverra une variable vide
echo Créons un fichier nommé ${KERNEL}_file # Fonctionnera
touch ${KERNEL}_file
```

Certaines variables sont déjà assignées par Bash, voici une liste non exhaustive:

- ``$SHELL`` : Le chemin du binaire du shell actuel
- ``$$`` Le PID de la session Bash
- ``$?`` Le dernier code de retour
- ``$@`` La liste des arguments d'entrée du script
- ``$#`` Le nombre de ces arguments
- ``$n`` avec ``n`` un chiffre. L'argument numéro ``n``


Les trois derniers sont particulièrements utiles pour utiliser des arguments d'entrée de script :
```sh 
#!/bin/sh
echo $#
echo $@
echo $3
```
Renverra : 

```sh
❯./script.sh 1 2 5
3
1 2 5
5
```

## Fonctions

Une fonction permet d'encapsuler une série de commandes et actions au sein d'une seule avec ses propres arguments.
Il a y deux syntaxes pour définir une fonction :

```sh
function ma_fonction {
    contenu de la fonction
}
```
et

```sh
ma_fonction () {
    contenu de la fonction
}
```

Le mot reservé ``function`` est donc optionnel mais si celui est omis alors les ``()`` deviennent obligatoires tandis qu'elles ne le sont pas dans le premier cas.
Les parenthèses ne servent fonctionnellement à rien si ce n'est s'assurer qu'il n'y a pas d'ambiguiter et que l'on veut bien faire une fonction. Je recommande donc d'utiliser la première syntaxe plus explicite.

Si l'on veut utiliser des arguments on peut utiliser les variables built-ins $n pour récupérer ces arguments au moment de l'appel de la fonction.

```sh
function ma_fonction () {
	echo "Les arguments sont : $1 $2"
}
ma_fonction arg1 arg2
```

Enfin, les variables sont de base globales dans une fonction. C'est à dire qu'une variable définie à l'intérieur ou à l'extérieure sera disponible à l'intérieur ou à l'extérieur par défaut. On peut cependant définir des variables locales qui n'existeront que dans la fonction.

```sh
var1="A"
var2="B"
function ma_fonction {
    local var1="C"
    var2="D"
    echo "Les variables dans la fonction sont var1: $var1, var2: $var2"
}
ma_fonction
echo "Les variables après la fonction sont var1: $var1, var2: $var2"
```

On voit bien que après la fonctin la ``$var1`` s'est remise sur sa valeur précédente tandis que la ``$var2`` reste sur la valeur définie dans la fonction.

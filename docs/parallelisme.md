# La programmation parallèle en Shell, Perl, Python et Ruby

## Différentes types de concurrency

La **concurrence** (concurrency) en programmation désigne la capacité d'un système à gérer plusieurs tâches ou processus en même temps, ce qui améliore l'efficacité et la réactivité. Cela ne veut pas nécessairement dire que les tâches s'éxécutent exactement en même temps, juste que ces tâches *existent* en même temps. Le **parallélisme** quant à lui désigne l'éxécution simultannée de plusieurs tâches, notamment grâce à des processeurs multicoeurs.

Le parallélisme est donc une sous catégorie de concurrence mais nécessite un processeur multicoeurs.

Une manière de faire de la concurrence sans faire du parallélisme est de faire de la programmation asynchrone. En programmation asynchrone une tâche sera non bloquante et permettra donc de passer à l'étape suivante, contrairement à la programmation classique (synchrone) où une tâche est bloquante tant qu'elle n'est pas finie. Ceci est utile lorsque la tâche en question ne nécessite aucune actions du processeur.

On peut imaginer une commande ``sleep 10`` qui attendra 10 secondes et bloquera le programme, pendant ces 10 secondes le processeur ne fera rien, c'est donc du temps perdu. Ainsi on peut lancer ce ``sleep 10``, le passer "en arrière plan", faire d'autres tâches puis attendre si nécessaire que ce ``sleep 10`` finisse. 

Les implémentations exactes des méthodes de concurrence varient grandement d'un langage à un notre.


## Concurrence sur Bash

Le shell Unix étant bien plus proche du système Linux la gestion de la concurrence est quasiment directement celle du kernel Linux. 
Un processus possède minimum un thread mais peut en posséder plus.

Quand un coeur du processeur est libre, le système choisi un thread en attente de traitement et s'en occupe.
Après un certain temps ce thread peut être remis en attente et/ou déplacer vers un autre coeur pour optimiser le système, mais ce n'est pas quelque chose à prendre en compte en tant que développeurs.

Ainsi, faire du multiprocessing en Bash revient à lancer plusieurs processus et laisser Linux s'en occuper.
On ne peut pas faire du multithreading en Bash.


### Processus en arrière plan

Il existe de multiples manières de faire du multiprocessing, l'une des manières les plus basiques est d'utiliser ``&`` qui permet de passer une commande en arrière plan et la rendre non bloquante.

```sh
sleep 10 &
echo Hello
```

Parfois on veut attendre que tout les jobs en arrière plan soient finis avant de continuer, ceci peut être fait avec la commande ``wait``. 

```sh
sleep 10&
sleep 10&
echo Waiting !
wait
echo Fin !
```

On peut aussi lister les jobs en arrière plan avec ``jobs`` et remettre un job au premier plan avec ``fg`` (pour *foreground*).

Parfois on se rends compte qu'une commande est longue à s'éxécuter et on aurait aimé la mettre en arrière plan. C'est possible via la combinaison de ``CTRL+Z`` suivi de la commande ``bg`` (pour *background*).
``CTRL+Z`` permet de suspendre un job et rendre la main dans le shell et ``bg`` permet d'arrêter la suspension et de continuer l'exécution du processus.

```sh
sleep 10 &
jobs # Affichera le processus sleep en arrière plan
fg  # Renverra le shell dans le process sleep
*CTRL+Z* # Suspend et rend la main
bg # Continue l'éxécution en arrière plan
```


### Pipes

L'utilisation de pipes sur Linux est, nativement, du multiprocessing.
Tout les processus d'une série de pipes sont lancés en même temps au début. La plupart des commandes Linux traitent ligne par ligne et renvoient ligne par ligne les données, ce qui permet une exécution concurrente de la plupart des commandes.

Ainsi, le temps d'exécution d'une série de pipes est le temps d'éxécution du processus le plus long du lot, et non la somme de tout les temps.

```sh
sleep 10 | sleep 10
# Ne prendra que 10 secondes pour s'exécuter
```


### Xargs

``xargs`` est une commande Unix puissante permettant la manipulation d'arguments. Cette commande perment notamment de récupérer puis grouper ou dégrouper des arguments et de les placer où on veut dans une commande à exécuter.

Exemple simple :

```sh
❯seq 6 | xargs -n 2
1 2
3 4
5 6
```

Par défaut si aucune commande n'est fournis, ``xargs`` fera un ``echo`` des arguments. Sinon ``xargs`` les rajoutera à la fin de la commande.
Le ``-n 2`` permet de préciser de grouper 2 par 2 les arguments.

On peut utiliser ``-I {}`` pour placer où on veut les arguments et pas seulement à la fin.

```sh
❯seq 3 | xargs -I {} echo "L'argument de valeur {} est au milieu du texte"
L'argument de valeur 1 est au milieu du texte
L'argument de valeur 2 est au milieu du texte
L'argument de valeur 3 est au milieu du texte
```

Dans l'état ``xargs`` est très pratique, cependant une autre force de xargs et la possibilité de facilement faire du multiprocessing.
En effet il suffit de rajouter simplement ``-P N`` avec ``N`` le nombre de processus.
```sh
seq 3 | xargs -P 3 -I {} echo "L'argument de valeur {} est au milieu du texte"
```

Ici, il y aura 3 processus, un pour chaque exécution de ``echo``. On peut aussi mettre ``N=0`` pour utiliser le maximum possible de processus automatiquement.



### Exercice

Utilisez ces méthodes pour optimiser le ping d'une longue liste d'ip.

```sh
for i in {1..200}
   do
   ping -c 1 192.168.1.$i &
   done
```

```sh
echo 192.168.1.{1..200} | xargs -n 1 -P 200 ping -c 1
```


## Python
Voici les principaux types de concurrence en Python :

- Le multi-processing implique l'exécution de plusieurs processus indépendants, chacun ayant sa propre mémoire. Cela évite les problèmes de sécurité des données associés au multi-threading, mais la communication inter-processus est plus complexe et coûteuse. 

**Utilisation typique** : Tâches computationnelles intensives où l'isolation entre les tâches est importante.

- Le multi-threading consiste à exécuter plusieurs threads (fils d'exécution) au sein d'un seul processus. On peut par exemple visualiser un programme avec deux threads faisant des écritures en base de données. Lorsqu'un thread commence son écriture, il peut laisser la main au second thread pour gagner du temps, sans pour autant que physiquement le processeur traite les actions en simultannée. Le multi-threading peut poser des problèmes de sécurité de données, les threads ayant souvent accès à la mémoire des autres threads.

**Utilisation typique** : Applications nécessitant des opérations d'E/S non bloquantes ou des tâches pouvant être exécutées indépendamment.

- La programmation asynchrone utilise des événements, des callbacks ou des futures/promesses pour gérer des tâches concurrentes. Les opérations peuvent être déclenchées de manière non bloquante, permettant à un programme de continuer à fonctionner pendant l'attente de la finalisation d'une tâche. 

**Utilisation typique** : Gestion d'opérations E/S, telles que les appels réseau ou l'accès aux fichiers, où le temps d'attente peut être long.

La programmation asynchrone est assez similaire au multi-threading

## Python

## En perl et ruby

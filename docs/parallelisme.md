# La programmation parallèle en Shell, Perl, Python et Ruby

## Différentes types de concurrence

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

Utilisez de la concurrence pour optimiser le ping d'IPs allant de 192.168.1.1 à 192.168.1.254.

??? note "Exemples de solutions"

    ```sh
     for i in {1..254}
        do
        (ping -c 1 192.168.1.$i > /dev/null && echo "192.168.1.$i") &
        done
    ```

    ```sh
    echo 192.168.1.{1..254} | xargs -n 1 -P 0 ping -c 1 | grep -B 1 "1 reçus" | grep stat
    ```

    ```sh
    echo 192.168.1.{1..254} | xargs -n 1 -P 0 ping -c 1 | awk '/1 reçus/ {print prev} {prev=$0}'
    ```



## Python

Il existe sur Python trois manières principales de faire de la programmation concurrentielle, via les modules ``threading``, ``asyncio`` et ``multiprocessing``. Les trois permettent de la concurrence mais il y a des subtilités entre elles.

On peut mesurer le temps d'exécution de fonctions grâce au module ``time`` et sa fonction ``time()``. C'est essentiel de mesurer lorsque l'on cherche à optimiser des temps d'exécution.

```
import time

n = 100000000

def carre(debut, fin):
    for i in range(debut, fin):
        k = i**2
        del k

t1 = time.time()
carre(0, n)
t2 = time.time()

print('Time taken in seconds -', t2 - t1)
```

Ce code permet de mesurer le temps d'exécution du calcul de chaque carré entre 0 et 100000000-1. Il prend 4.8s à s'exécuter sur mon système.


### threading

La librairie ``threading`` permet le multithreading dans Python. Cependant à cause de la manière dont Python est implementé il ne peut y avoir qu'un seul thread qui a le controle (lock) de l'interpréteur Python à un instant ``t``. Cela est causé par le Pytho Global Interpreter Lock ou encore GIL.

Ainsi une application Python utilisant ``threading`` et deux threads ne sera pas toujours plus rapide qu'avec un seul. Les tâches *CPU-bound* ne verront pas de gain car le GIL bloquera l'exécution des threads en même temps sur le CPU.  En revanche les tâches *I/O-bound* pourront voir des gains significatifs car la tâche n'est pas limitée par le CPU, mais autre chose, par exemple la réponse d'un serveur distant à un ping, ou de l'écriture disque. 


```python
import threading
import time

n = 100000000

def carre(deb_fin):
    debut = deb_fin[0]
    fin = deb_fin[1]
    for i in range(debut, fin):
        k = i**2
        del k


thread1 = threading.Thread(target=carre, args=((0, n // 2),))  # S'occupera de la moitié des carrés
thread2 = threading.Thread(target=carre, args=((n // 2, n),))  # Et ce thread de l'autre moitié

t1 = time.time()

thread1.start()
thread2.start()
thread1.join()
thread2.join()

t2 = time.time()


print('Time taken in seconds -', t2 - t1)
```

Cette version du code précédent prends 4.9s à s'exécuter malgré qu'il y ait deux threads faisant les calculs.

Pour utiliser ``threading``, une manière simple est de définir chaque threads avec ``threading.Thread`` en rajoutant comme argument la tâche à effectuer avec ses arguments. Juste définir un objet ``Thread`` ne l'exécute pas. Il faut utiliser la méthode ``.start()`` sur l'objet pour le lancer.

La méthode ``.join()`` permet de bloquer l'avancée dans le script jusqu'à ce que les threads aient fini de s'exécuter.

Malgré les résultats peu engageants ``threading`` peut gagner du temps lorsque ce n'est pas le CPU qui limite, par exemple si l'on fait de multiples ping et que l'on attends la réponse des serveurs.


### multiprocessing

Lorsque l'on veut donc accélérer une tâche limitée par le CPU on peut utiliser la librairie ``multiprocessing`` qui permet la création de différents processus qui iront sur des coeurs différents.

```python
import time
import multiprocessing

n = 100000000


def carre(deb_fin):
    debut = deb_fin[0]
    fin = deb_fin[1]
    for i in range(debut, fin):
        k = i**2
        del k


t1 = time.time()

with multiprocessing.Pool() as pool:
    pool.map(carre, [(0, n // 2), (n // 2, n)])

t2 = time.time()

print('Time taken in seconds -', t2 - t1)
```


Pour faire fonctionner ``multiprocessing`` on peut définir un objet ``Pool`` et y maper une fonction et une liste d'arguments, la librairie s'occupera d'appliquer ces arguments à la fonction et d'exécuter ceci dans des processus différents.
Le temps d'exécution est ici quasiment deux fois plus rapide. 

Cependant il est important de noter que créer un processus est une tâche prenant un peu de temps, il est donc peu judicieux d'utiliser du multiprocessing lorsqu'il y a des milliers et des milliers de tâches n'étant pas limitées par le CPU par exemple. 

De plus la communication entre les processus est plus compliquée que la communication inter-threads de ``threading``.

### asyncio

``asyncio``


### Utiliser la concurrence du Shell pour Python !

```sh
echo 0 50000000 50000000 100000000 | xargs -P 2 -n 2 python script.py
```

```python
#!python
import sys
import time

deb_fin = (int(sys.argv[1]), int(sys.argv[2]))

def carre(deb_fin):
    debut = deb_fin[0]
    fin = deb_fin[1]
    for i in range(debut, fin):
        k = i**2
        del k


t1 = time.time()
carre(deb_fin)
t2 = time.time()

print('Time taken in seconds -', t2 - t1)
```

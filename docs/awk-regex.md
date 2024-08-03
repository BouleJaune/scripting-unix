# Introduction à ``awk`` et aux Regex

## Awk

``awk`` est un puissant langage de programmation et un utilitaire en ligne de commande dans les systèmes Unix et Linux. Il est conçu pour la manipulation de texte et le traitement de données basées sur des fichiers texte ou des flux d'entrée. ``awk`` permet de rechercher des motifs, extraire et transformer des données.


Les fichiers de tests sont récupérables ici :

```sh
curl fichier.txt numbers.txt
```

Ils ont étés générés pour ``numbers.txt`` avec :
```sh
awk 'BEGIN { for (i = 1; i<= 10; i++) print int(100*rand()),  int(100*rand()), int(100*rand()) }' > numbers.txt
```

### Structure de Commande

La syntaxe de base de ``awk`` est la suivante :
```bash
awk 'pattern { action }' fichier
```

   - pattern : Un motif qui, s'il est vrai pour une ligne donnée, déclenche l'exécution de l'action.
   - action : Une série d'instructions entre {} qui sont exécutées lorsque le motif est trouvé.

### Variables par défaut

Awk fournit une liste de variables déjà initialisées, en voici une partie: 

   - ``NR`` : Numéro de ligne global (cumulé à travers tous les fichiers d'entrée (Number of Rows).
   - ``$0`` : La ligne entière actuelle.
   - ``$1``, ``$2``, ..., ``$n`` : Les n-ièmes champs d'une ligne, où le séparateur de champs par défaut est l'espace ou la tabulation.
   - ``FS`` : Le séparateur de champs (par défaut, espace ou tabulation).
   - ``OFS`` : Le séparateur de champs de sortie (par défaut, espace).
   - ``RS`` : Le séparateur d'enregistrements (par défaut, nouvelle ligne).
   - ``ORS`` : Le séparateur d'enregistrements de sortie (par défaut, nouvelle ligne).
   - ``FNR`` : Le numéro de ligne actuel dans le fichier d'entrée actuel (File Number of Rows).
   - ``NF`` : Le nombre de champs dans la ligne courante (Number of Fields).
   - ``FILENAME`` : Le nom du fichier d'entrée actuel.

On peut changer le délimiteur par défaut avec ``-F``, ``-F,`` utilisera ``,`` comme délimiteur au lieu de tab ou espace.

Awk permet aussi de déclarer ses propres variables dans les actions :

```sh
awk '{ n = 0; print n}' fichier.txt
```


### Imprimer des Colonnes Spécifiques

Pour imprimer le premier et le troisième champ de chaque ligne d'un fichier :

```bash
awk '{ print $1, $3 }' fichier.txt
```
Si aucun pattern n'est fourni alors ``awk`` matchera chaque ligne.

On peut fournir plusieurs commandes à awk en lui fournissant d'autres patterns et actions.

```bash
awk '{ print $1, $3 } { print $5 }' fichier.txt

# Ou bien en séparant sur plusieurs lignes :
awk '{ print $1, $3 } \
{ print $5 }' \
fichier.txt
```


### Filtrer par Motif

Pour afficher les lignes contenant le mot "Erreur" :

```bash
awk '/ERROR/ { print $0 }' fichier.txt
```

### Calculs et Opérations sur les Champs

Pour calculer la somme des valeurs des troisième et quatrième champs de chaque ligne:

```bash
awk '{ somme = $1 + $2; print somme }' numbers.txt
```

### Mots clés BEGIN et END 

``BEGIN { action }`` permet d'exécuter une action avant la lecture de la première ligne. De manière symétrique ``END { action }`` permet d'éxécuter une action après la lecture de la dernière ligne.

```sh
awk 'BEGIN { print "Début de traitement" } \
/ERROR/ { print $0 } \
END { print "Fin de traitement" }' fichier.txt
```

```bash
# Somme de la première colonne
awk 'BEGIN {n=0} {n += $1} END {print n}' numbers.txt
```

### Fonctions Intégrées

- **`length([string])`** : Renvoie la longueur d'une chaîne ou du champ courant.
- **`substr(string, start, length)`** : Extrait une sous-chaîne de `string` à partir de `start` sur `length` caractères.
- **`tolower(string)`** : Convertit la chaîne en minuscules.
- **`toupper(string)`** : Convertit la chaîne en majuscules.
- **`split(string, array, [separator])`** : Divise `string` en éléments dans `array`, séparés par `separator`.
- **`match(string, regex)`** : Renvoie l'indice de départ et la longueur de la correspondance de `regex` dans `string`.
- **`gsub(regex, replacement, [target])`** : Remplace toutes les occurrences de `regex` par `replacement` dans `target` (ou `$0` si omis).
- **`sub(regex, replacement, [target])`** : Remplace la première occurrence de `regex` par `replacement` dans `target`.
- **`srand([expr])`** : Initialise le générateur de nombres aléatoires avec `expr` ou l'heure actuelle.
- **`rand()`** : Renvoie un nombre aléatoire entre 0 et 1.


### Exercice
Attraper la ligne précédent un match
??? Note "Exemple de solution"
    ```sh
    echo 192.168.1.{1..254} | xargs -n 1 -P 0 ping -c 1 | awk '/1 reçus/ {print prev} {prev=$0}'
    ```

## Expression Régulières

Les expressions régulières (regex) sont un puissant outil de recherche et de manipulation de texte basé sur des motifs. Elles sont utilisées pour correspondre à des chaînes de caractères suivant des règles spécifiques.

Il y a plusieurs variantes de regex. Ces variantes diffèrent dans leurs syntaxes et possibilités et certains outils utilisent certaines variantes. Les variantes principales sont : 

- Simple Regular Expressions (``sed``, ``grep``)
- Extended Regular Expressions (``awk``, ``-E``)
- Perl-Compatible Regular Expressions (Perl, Python, PHP, Java)
 

### Simple Regular Expressions

Les expressions régulières simples sont principalement utilisés par des outils Unix pour la rétrocompatibilité. Ainsi des outils tels que ``sed`` et ``grep`` les utilisent par défaut.


### Extended Regular Expressions



### Perl-Compatible Regular Expressions



#### Caractères Littéraux

Les caractères simples correspondent à eux-mêmes :

- ``a`` : Correspond à la lettre "a".

#### Métacaractères

Certains caractères ont des significations spéciales :

- ``.`` : Correspond à n'importe quel caractère sauf un saut de ligne.
- ``^`` : Début de la ligne.
- ``$`` : Fin de la ligne.
- ``*`` : Correspond à 0 ou plusieurs répétitions du caractère précédent. ``.*`` permet donc de matcher n'importe quel série de caractères.
- ``+`` : Correspond à 1 ou plusieurs répétitions du caractère précédent.
- ``?`` : Correspond à 0 ou 1 répétition du caractère précédent.
- ``[]`` : Définit une classe de caractères. ``[abc]`` correspond à "a", "b" ou "c".
- ``|`` : OU logique. ``a|b`` correspond à "a" ou "b".

#### Séquences d'Échappement

Certains caractères doivent être échappés avec une barre oblique inverse ``\`` :

- ``\.`` : Correspond à un point littéral.
- ``\d`` : Correspond à un chiffre (0-9).
- ``\D`` : Correspond à un caractère non numérique.
- ``\w`` : Correspond à un caractère de mot (lettres, chiffres, et underscore).
- ``\W`` : Correspond à un caractère non-mot.
- ``\s`` : Correspond à un espace blanc (tab, espace, saut de ligne ...).
- ``\S`` : Correspond à un caractère non-espace blanc.

### Quantificateurs

- ``{n}`` : Correspond exactement à n répétitions.
- ``{n,}`` : Correspond à au moins n répétitions.
- ``{n,m}`` : Correspond entre n et m répétitions.


### Groupes et Références

- ``(abc)`` : Correspond à "abc" et capture ce groupe pour une référence ultérieure.

#### Références à des Groupes

- ``\1``, ``\2``, ... : Référencent les groupes capturés par leur numéro.

### Assertions

#### Assertions Positives

- ``(?=abc)`` : Correspond à une position suivie par "abc".

#### Assertions Négatives

- ``(?!abc)`` : Correspond à une position non suivie par "abc".

### Exemples Pratiques

#### Correspondance Simple

- ``hello`` : Correspond à la chaîne "hello".

#### Correspondance de Chiffres

- ``\d{3}`` : Correspond à exactement trois chiffres.

#### Correspondance d'Emails

- ``\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b`` : Correspond à une adresse email.

#### Remplacement de Texte

En Python, vous pouvez utiliser des regex pour rechercher et remplacer des motifs dans une chaîne grâce au module ``re``.

```python
import re

texte = "Bonjour, je m'appelle Alice."
nouveau_texte = re.sub(r"Alice", "Bob", texte)
print(nouveau_texte)  # Bonjour, je m'appelle Bob.
```


## Regex
Cours global regex
### Regex sur Unix
sur awk
sur grep
sur sed
### Regex en Python
### Regex en Perl
### Regex en Ruby

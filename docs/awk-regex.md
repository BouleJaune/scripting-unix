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
`
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

## Regex
Cours global regex
### Regex sur Unix
sur awk
sur grep
sur sed
### Regex en Python
### Regex en Perl
### Regex en Ruby

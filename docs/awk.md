
# Awk

``awk`` est un puissant langage de programmation et un utilitaire en ligne de commande dans les systèmes Unix et Linux. Il est conçu pour la manipulation de texte et le traitement de données basées sur des fichiers texte ou des flux d'entrée. ``awk`` permet de rechercher des motifs, extraire et transformer des données.


Vous pouvez générer le fichier ``numbers.txt`` utilisé dans cette partie avec :
```sh
awk 'BEGIN { for (i = 1; i<= 10; i++) print int(100*rand()),  int(100*rand()), int(100*rand()) }' > numbers.txt
```

Vous pouvez récupérer ``fichier.txt`` et ``numbers.txt`` dans le dossier ``awk_files`` du repo Github.

## Structure de Commande

La syntaxe de base de ``awk`` est la suivante :
```bash
awk 'pattern { action }' fichier
```

   - pattern : Un motif qui, s'il est vrai pour une ligne donnée, déclenche l'exécution de l'action.
   - action : Une série d'instructions entre {} qui sont exécutées lorsque le motif est trouvé.

## Variables par défaut

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


## Imprimer des Colonnes Spécifiques

Pour imprimer le premier et le troisième champ de chaque ligne d'un fichier :

```bash
awk '{ print $1, $3 }' fichier.txt
```
Si aucun pattern n'est fourni alors ``awk`` récupèrera chaque ligne.

On peut fournir plusieurs commandes à awk en lui fournissant d'autres patterns et actions.

```bash
awk '{ print $1, $3 } { print $5 }' fichier.txt

# Ou bien en séparant sur plusieurs lignes :
awk '{ print $1, $3 } \
{ print $5 }' \
fichier.txt
```

Ces actions fonctionnent par bloc d'accolades ``{}``, entre chaque bloc il peut y avoir un pattern pour matcher quelque chose, un bloc ``{}`` ne cherchera à match qu'avec le pattern *juste* avant lui même.

Si on veut deux commandes qui utilisent le même pattern il faut les mettre dans le même bloc.

```sh
awk 'pattern1 { action1 } pattern2 {action2}' fichier # Action 2 s'appliquera que sur les lignes matchant pattern2
awk 'pattern1 { action1 } {action2}' fichier # Action 2 s'appliquera sur TOUTES les lignes et pas seulement celles matchant pattern1
awk 'pattern1 { action1 ; action2}' fichier # Action 2 s'appliquera que sur les lignes matchant pattern1
```


## Filtrer par Motif

``awk`` permet de rechercher par expressions régulières (vues plus bas) du texte.
Pour afficher les lignes contenant le mot "ERROR" :

```bash
awk '/ERROR/ { print $0 }' fichier.txt # Permet de récupérer les lignes contenant ERROR.
awk '!/ERROR/ { print $0 }' fichier.txt # Permet de ne PAS récupérer les lignes contenant ERROR.
```

#### Exercice

Cherchez avec ``awk`` dans ``fichier.txt`` toutes les alertes provenant du serveur numéro 3.

??? Note "Exemple de solution"

    ```sh
    awk '/Server3/ {print $0}' fichier.txt
    ```


## Opérations sur les champs

``awk`` permet aussi de faire des opérations arithmétiques sur les champs si ceux-ci sont numériques.

Pour, par exemple, calculer la somme des valeurs des troisième et quatrième champs de chaque ligne:

```bash
awk '{ somme = $1 + $2; print somme }' numbers.txt
```

On peut aussi remplacer le contenu des variables (champs ou lignes par exemple):

```bash
awk '{$0 = "Toutes les lignes seront les mêmes !"} {print $0}' fichier.txt
```

#### Exercice

Récupérer les alertes de l'infogérant A qui ne sont pas des ``INFO`` et remplacer le nom de l'infogérant A par ``nouveau_infogérant`` et afficher le tout.

??? Note "Tips"
    On peut faire plusieurs pattern de matching avec ``&&`` (``ET`` logique) et ``||`` (``OU`` logique): ``awk 'pattern1 && pattern2 { commande }'``

??? Note "Exemple de solution"
    ```bash
    awk '/InfogérantA/ && !/INFO/  { $5 = "nouveau_infogérant" ; print $0 }' fichier.txt
    ```

## Mots clés BEGIN et END 

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

PS: Ici le ``BEGIN {n=0}`` n'est pas nécessaire car en pratique ``awk`` initialisera tout seul la variable à 0 avant la première incrémentation.

#### Exercice

Comptez pour ``Server3`` et ``Server2`` le nombre d'alertes qu'ils possèdent chacun et afficher ces nombres et la somme de ceux-ci.

??? Note "Exemple de solution"
    ```sh
    awk '/Server3/ {n1+=1} /Server2/ {n2+=1} END {print n1, n2, n1+n2}' fichier.txt
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

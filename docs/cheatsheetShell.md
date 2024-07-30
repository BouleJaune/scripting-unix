man ! RTFM

# Cheatsheet des Commandes Unix

Le manuel, souvent appelé "man", est une collection de pages de documentation pour les commandes Unix et les programmes. Chaque page fournit une description détaillée de l'utilisation, des options, des exemples et de la syntaxe d'une commande ou d'un programme spécifique.

La commande man est utilisée pour afficher ces pages de manuel. Par exemple, man ls affiche la documentation pour la commande ls. Cette documentation est essentielle pour comprendre les différentes options et usages des commandes disponibles dans le système Unix.


#### Commandes de Base
- ``pwd`` : Affiche le chemin du répertoire de travail actuel.
- ``cd [répertoire]`` : Change le répertoire courant.
- ``ls`` : Liste les fichiers et répertoires.
  - ``ls -l`` : Liste détaillée, avec notamment les droits.
  - ``ls -a`` : Inclut les fichiers cachés.

#### Gestion des Fichiers et Répertoires
- ``cp [source] [destination]`` : Copie des fichiers.
  - ``cp -r [source] [destination]`` : Copie récursive pour les répertoires.
- ``mv [source] [destination]`` : Déplace ou renomme des fichiers/répertoires.
- ``rm [fichier]`` : Supprime des fichiers.
  - ``rm -r [répertoire]`` : Supprime des répertoires et leur contenu.
- ``mkdir [répertoire]`` : Crée un nouveau répertoire.
    - ``mkdir -p [répertoire]`` : Crée un nouveau répertoire et les répertoires parents si nécessaires et ne renvoit pas d'erreur si le répertoire existe.

#### Visualisation et Edition de Fichiers
- ``cat [fichier]`` : Affiche le contenu d'un fichier.
- ``less [fichier]`` : Affiche le contenu d'un fichier page par page.
- ``head -n [nombre] [fichier]`` : Affiche les premières lignes d'un fichier ou du ``stdin`` sans fichier.
- ``tail -n [nombre] [fichier]`` : Affiche les dernières lignes d'un fichier ou du ``stdin`` sans fichier.
- ``vim [fichier]`` : Editeur de texte modal.
- ``diff [fichie1] [fichier2]`` : Affiche la différence entre deux fichiers.

#### Filtrage de Texte
- ``grep [motif] [fichier]`` : Recherche un motif dans un fichier ou dans le ``stdin`` sans fichier.
  - ``grep -r [motif] [répertoire]`` : Recherche récursive dans les fichiers d'un répertoire.
- ``uniq`` : Supprime les doublons (nécessite un tri préalable).
- ``sort [fichier]`` : Trie le contenu d'un fichier ou du ``stdin`` sans fichier.
  - ``sort -u [fichier]`` : Trie le conteu et supprime les doublons.
- ``cut -d [délimiteur] -f [champs] [fichier]`` : Coupe les champs d'un fichier texte.
 - ``sed 's/[motif]/[remplacement]/g' [fichier]`` : Stream Editor pour filtrer et transformer le texte; ici, remplace tous les occurrences de "motif" par "remplacement". Sans fichier fourni il prendra le ``stdin``

#### Gestion des Processus
- ``ps`` : Affiche les processus en cours.
  - ``ps aux`` : Affiche tous les processus avec détails.
- ``top`` : Affiche en temps réel les processus les plus gourmands.
- ``kill [PID]`` : Termine le processus avec le PID spécifié.

#### Permissions et Propriétés
- ``chmod [permissions] [fichier]`` : Change les permissions d'un fichier.
  - ``chmod 755 [fichier]`` : Donne les permissions `rwxr-xr-x`.
- ``chown [utilisateur]:[groupe] [fichier]`` : Change le propriétaire et le groupe d'un fichier.
- ``chgrp [groupe] [fichier]`` : Change le groupe d'un fichier.

#### Réseau et Connexions
- ``ping [adresse]`` : Vérifie la connectivité vers une adresse IP.
- ``ifconfig`` : Affiche les configurations réseau des interfaces.
- ``wget [URL]`` : Télécharge un fichier depuis une URL.

#### Autres Utilitaires
- ``echo [texte]`` : Affiche un texte.
- ``date`` : Affiche ou modifie la date et l'heure système.
- ``history`` : Affiche l'historique des commandes.
- ``alias [alias]='[commande]'`` : Crée un alias pour une commande.
- ``xargs`` : Construit et exécute des commandes à partir du ``stdin``, utilisé pour manipuler des arguments.
- ``tr 'car1' 'car2'`` : Transcode les caractères, ici remplace les occurrences de 'car1' par 'car2' dans le ``stdin``.


#### Redirection et Pipes
- ``command1 > fichier`` : Redirige la sortie standard de `command1` vers `fichier`.
- ``command1 >> fichier`` : Ajoute la sortie standard de `command1` à `fichier`.
- ``command1 2> fichier`` : Redirige les erreurs (stderr) de `command1` vers `fichier`.
- ``command1 | command2`` : Utilise la sortie de `command1` comme entrée pour `command2`.


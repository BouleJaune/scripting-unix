# Travaux Pratique


## Générer des données factices

Faites un script Python générant des données de supervision factices. 
Ces données seront sous la forme d'un fichier texte/csv et représenteront des alertes avec comme champs : 

- Timestamp 
- Serveur concerné
- Criticité de l'alerte (critique, informations, erreur...)
- Message de l'alerte
- Infogerant à la charge de l'alerte
- Application concernée
- Environment (prod, hors-prod, testing etc)


Exemples d'alertes possibles :

```python
"INFO": ["System running smoothly.", "Routine check completed.", "Backup successful.", "Restart performed successfully", "Update was successful"],
"WARNING": ["Disk space running low.", "High memory usage detected.", "Unusual login activity detected.", "Load average running high", "MySQL response time slow"],
"ERROR": ["Application crashed.", "Service unavailable.", "Database connection lost.", "FileSystem saturated", "Server unresponsive"],
"CRITICAL": ["System overload imminent.", "Critical security vulnerability detected.", "Data corruption detected.", "System bricked", "Server is on fire"]
```
Vous pouvez utiliser la librairie ``pandas`` ou ``csv`` pour enregistrer au format ``csv`` les données mais ce n'est pas forcément nécessaire.

Une fois le script fait, générez un fichier csv avec plusieurs milliers d'alertes (1000 par exemple).

## Exploration de données

Utilisez directement la ligne de commande pour explorer un peu les données pour récupérer notamment : 

- Le nombre de serveurs différents
- Le nombre d'alertes pour un serveur donné
- La liste des alertes critiques
- Toutes les alertes non-INFO
- D'autres choses selon vos idées

## Processing des données


Faites un script Bash qui va récupérer toutes ces données de supervision et générer un fichier pour chaque alerte.
Le fichier sera de la forme :

```
Date :
Serveur :
Criticité :
Message : 
Infogerant :
Application :
Environnement :
```

## Django Rest API

Utilisez la librairie Django Rest framework pour créer une Rest API simple qui sera en mesure de recevoir les alertes dans une base de données SQlite.

- Sur l'URL ``/api/alert`` on pourra récupérer via ``GET`` les alertes et via ``POST`` on pourra en rajouter
- Sur l'URL ``/api/alert/[id d'une alerte]`` on pourra récupérer via ``GET`` une alerte précise, la supprimer via ``DELETE`` ou la modifier via ``POST``.

Django Rest Framework permettra d'avoir une interface web pratique.

## Connecteur de données

Faire un script qui lit le dossier contenant les fichiers d'alertes et les injecte dans la base de données via la Rest API.

Si la donnée est bien injectée dans la base de données alors supprimez le fichier d'alerte, sinon afficher le code de retour et le nom du fichier.

## Intégrer ces scripts au système

Il peut être intéressant d'intégrer proprement les scripts dans le système pour avoir une meilleure gestion et monitoring de ceux-ci.

Pour cela on peut utiliser Systemd :

- Faire un service systemd pour le serveur Django.
- Faire un timer systemd + service systemd pour le script lisant les données.

## Pour aller plus loin

Vous pouvez faire une petite interface graphique web qui permet de visualiser les alertes stockées dans la base de donnée SQLite. Et y rajouter quelques fonctionnalités selon votre imagination. Comme par exemple un bouton d'acquittement d'alerte. Ou encore des filtres.

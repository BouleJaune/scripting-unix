# Travaux Pratique Shell

Gérer un peu des users
Récupérer la liste des pourcentages de remplissages des filesystems
Generate logs (?) with errors and what not
Logrotate
Parsing log et trouver les warnings, criticals etc
Save dans un fichier dans un dossier

plus tard python s'en occupera


## Script

## Sans scripts

```sh
df | tail -n +2 | tr -s " " | cut -d " " -f 5
```

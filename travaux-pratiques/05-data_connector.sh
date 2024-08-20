#!/bin/bash
# Simple script observant un dossier en continu et lisant les fichiers pour les injecter dans une restAPI
data_dir='a_traiter'
for file in "$data_dir"/*
do
	if [ -f "$file" ]; then # Vérifie que file est un fichier
		while IFS=":" read -r champ contenu # IFS permet de séparer les lignes par : (input field separator)
		do
			case "$champ" in
			    "Date")
				date_heure=$contenu
				;;
			    "Serveur")
				serveur=$contenu
				;;
			    "Criticité")
				criticity=$contenu
				;;
			    "Message")
				message=$contenu
				;;
			    "Infogerant")
				infogerant=$contenu
				;;
			    "Application")
				application=$contenu
				;;
			    "Environnement")
				env=$contenu
				;;
			esac
		done < "$file" # Input redirection de toute la boucle while
	fi

	# Faire bien attention aux singles quotes qui empêche l'utilisation des $variables
	data='{"date":"'$date_heure'", "serveur": "'$serveur'", "criticity": "'$criticity'", "message": "'$message'", "infogerant": "'$infogerant'", "application": "'$application'", "environnement": "'$env'"}'

	## Envoi dans la rest API pas en bg sinon on casse sqlite ! Et on récupère le code de retour dans r
	r=$(curl --request POST -H "Content-Type:application/json" http://127.0.0.1:8001/api/alert --data "$data" -s -o /dev/null -w "%{http_code}")

	## Traitement du code de retour, on notifie si on a pas 201
	if [ ! "$r" -eq 201 ];then
		echo Code retour : $r, alerte:  $file, $data
	else
		rm $file # Le fichier est bien en base on peut le supprimer !
	fi
done

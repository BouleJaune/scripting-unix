Petit serveur web django qui stock les données dans une db sqlite avec une rest api pour ingérer les données
Les données sont des données factices de supervision



## Préparations initiales

### Installation de Django et création du projet

Dans un environnement virtuel Python (venv) installons ``djangorestframework`` et créons un projet vierge: 

```sh
pip install djangorestframework 
django-admin startproject djangorestapi .
cd djangorestapi
django-admin startapp quickstart
```

Maintenant on peut synchroniser la db et créer un super utilisateur : 

```
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com
```

Enfin dans les paramètres du projet rajoutons le module ``rest_framework`` :

Ouvrir ``settings.py`` et rajoutez le module dans la liste ``INSTALLED_APPS``

```python
INSTALLED_APPS = [
    'rest_framework', # <= cette ligne
    ...
]
```

Le projet est maintenant créé et prêt à recevoir sa première application.

### Création d'une application Django

Un projet Django contient des "app", des applications web qui ont chacune leur propre but et utilité. Chaque projet peut contenir plusieurs apps, ceci est utile dans le cadre de gros projets où plusieurs fonctionnalités sont disponibles (blog, webshop, forum sur le même site...).

On peut créer une nouvelle application :

```
python manage.py startapp myapp
```

Cela va créer un nouveau dossier nommé ``myapp``, c'est dans celui que l'on va définir tout ce qui est nécessaire pour notre Rest API.

Ce dossier contient :
```
./admin.py 
./models.py 
./migrations
./migrations/__init__.py
./views.py
./tests.py
./apps.py
```

Les fichiers qui nous intéresseront ici sont ``models.py``, ``views.py`` et deux que l'on va créer ``urls.py`` et ``serializers.py``.


Une fois tout ceci fait dans le fichier  ``djangorestframework/settings.py`` il faut rajouter notre nouvelle application dans la liste ``INSTALLED_APPS`` :

```python
INSTALLED_APPS = [
    'myapp`, # <= cette ligne
    'rest_framework', 
    ...
]
```
## Model the data

Les models dans Django sont des classes Python qui définient la structure des tables de notre base de données.

Il nous faut donc définir un modèle pour nous permettre de stocker les alertes dans la base de données.

Pour cela il faut modifier le fichier ``models.py`` et définir une classe, qu'on peut nommer, ``Alert`` :

```python
from django.db import models


class Alert(models.Model):
    date = models.CharField(max_length=200)
    serveur = models.TextField()
    criticity = models.TextField()
    infogerant = models.TextField()
    message = models.TextField()
    application = models.TextField()
    environnement = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serveur
```

Une fois le modèle défini il faut le propager dans la base de données, pour cela on utilise ces deux commandes : 

```sh
python manage.py makemigrations
python manage.py migrate
```

Cela va créer les tables vierges dans la base de données SQLite.

Ces modèles nous permettent d'abstracter la partie SQL.

## Serializer

Le serializer va permettre de transformer les Json reçues via l'API en données ingérées dans la BDD SQL, et inversement transformer le SQL en Json. Il faut un serializer pour chaque modèle de données.

Ici le serializer hérite d'une classe Django Rest Framework qui permet de n'avoir à quasiment rien faire pour avoir un serializer fonctionnel de notre model. On crée juste une classe héritant de ceci et on lui dit quel est le modèle et quels champs il faut prendre.

On met le serializer dans le fichier ``myapp/serializers.py`` :

```python
from rest_framework import serializers
from .models import Alert

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
```

Il est important de noter que ``models.py`` est importé ici de manière relative avec ``.models`` pour bien s'assurer de ne pas rentrer en conflit avec par exemple d'autres applications Django ou encore même avec ``django.db.models``.

## API Views

Une vue sur Django permet de créer des actions ou encore des pages web. Ces vues seront à rattacher à une URL. Ici les vues que l'on veut sont les actions que l'on souhaite faire soit : 

- Ajouter des données et pouvoir tout afficher, action rattachée sur ``/api/alert``.
- Afficher, supprimer, modifier une donnée précise, action rattachée sur ``/api/alert/id_alert``.

Pour cela on va donc créer une vue pour chaque action. On peut encore une fois utiliser des Classes Python déjà existantes dans le framework car ce sont des actions basiques.

Les deux classes sont disponibles dans ``rest_framework.generics`` et sont ``ListCreateAPIView`` et ``RetrieveUpdateDestroyAPIView``.

Elles n'auront besoin que de savoir sur quel type de donnée on veut faire les actions (``.models.Alert``) et comment traduire Json``<=>``SQL (``.serializers.AlertSerializer``).


Le fichier ``views.py`` contient donc :

```python
# from django.shortcuts import render
from rest_framework import generics
from .models import Alert
from .serializers import AlertSerializer


class AlertCreateList(generics.ListCreateAPIView):
    """
    Permet de créer des instances d'Alert via POST
    et de les lister via GET
    """
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


class AlertRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Permet de récupérer une instance d'Alert via GET,
    ou d'uppdate via POST
    ou de détruire via DELETE
    """
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

```


Maintenant toute la partie logique est faite, il ne reste plus qu'à créer les URLs.

## URL Routing
### URL de l'app dans le projet

Notre application ``myapp`` au sein du projet ``djangorestapi`` a besoin de sa propre URL, elle sera disponible sur ``/api``. Pour cela il faut renseigner cette URL dans le projet. On peut utiliser la fonction ``include`` de ``django.urls``.

Dans ``djangorestapi/urls.py`` rajouter l'url de ``myapp`` : 

```python
from django.contrib import admin
from django.urls import path, include  # Rajout de include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),  # Rajout de l'url /api/ qui pointera vers notre Rest API
]
```

### URLs des appels API

Une fois l'url de ``myapp`` mise en place on peut définir les URLs de nos ``views``.

Dans le fichier ``myapp/urls.py`` il faut rajouter les URLs des appels API et les rattacher aux ``views`` en question.

Les views étant simplement des Classes Python, elles ne sont pas des objets views, cependant ces classes ont la méthode ``.as_view()`` héritée ce qui perment de la considérer comme tel.

```python
from django.urls import path
from .views import AlertCreateList, AlertRetrieveUpdateDestroy

urlpatterns = [
    # Rattache l'url /alert à AlertCreateList
    path('alert', AlertCreateList.as_view(), name='alert-list-create'),
    # Rattache l'URL /alert/[id d'une Alert] à AlertRetrieveUpdateDestroy
    path('alert/<int:pk>', AlertRetrieveUpdateDestroy.as_view(), name='alert-detail'),
]
```

## Informations complémentaires


Pour flush la base de donnée on peut  : 
```
python manage.py flush
```
Ou encore supprimer le fichier de BDD SQLite et remigrer.

Pour lancer le serveur Django : 
```
python manage.py runserver
```

Petit serveur web django qui stock les données dans une db sqlite avec une rest api pour ingérer les données
Les données sont des données factices de supervision



## Préparations initiales

### Installation de Django et création du projet

Dans un Python venv installons ``djangorestframework`` et créons un projet vierge: 
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

Un projet Django contient des apps, des applications web qui ont chacune leur propre but et utilité. Chaque projet peut contenir plusieurs apps, ceci est utile dans le cadre de gros projets où plusieurs fonctionnalités sont disponibles (blog, webshop, forum sur le même site...).

On peut créer une nouvelle application :
```
python manage.py startapp myapp
```

Cela va créer un nouveau dossier nommé ``myapp``, c'est dans celui que l'on va définir tout ce qui est nécessaire pour notre Rest API.

Ce dossier contient :
```
./__init__.py
./admin.py 
./models.py 
./migrations
./migrations/__init__.py
./views.py
./tests.py
./apps.py
```

## Model the data

Les models dans Django sont des classes Python qui définie la structure des tables de notre base de données.

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


## Serializer
```python
from rest_framework import serializers
from .models import Alert


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'
```
## API Views

``myapp/views.py``
```python
from django.urls import path
from .views import AlertCreate
# , AlertRetrieveUpdateDestroy

urlpatterns = [
    path('alert-create', AlertCreate.as_view(), name='alert-create'),
    # path('hello/', AlertRetrieveUpdateDestroy, name='alert-retriev'),
]
```

## URL Routing
### URL de l'app dans le projet

Dans ``djangorestapi/urls.py`` rajouter l'url de notre app RestAPI : 

```python
from django.contrib import admin
from django.urls import path, include  # Rajout de include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),  # Rajout de l'url /api/ qui pointera vers notre Rest API
]
```

### URLs des appels API

Dans le fichier ``myapp/urls.py`` il faut rajouter les URLs des appels API et les rattacher aux ``views`` en question.

```python
from django.urls import path
from .views import AlertCreate
# , AlertRetrieveUpdateDestroy

urlpatterns = [
    path('alert-create', AlertCreate.as_view(), name='alert-create'),
    # path('hello/', AlertRetrieveUpdateDestroy, name='alert-retriev'),
]
```

## Auth and perms

Pour reset la base de donnée à zéro
python manage.py flush
## 

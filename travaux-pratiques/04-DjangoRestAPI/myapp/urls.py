from django.urls import path
from .views import AlertCreateList, AlertRetrieveUpdateDestroy

urlpatterns = [
    # Rattache l'url /alert à AlertCreateList
    path('alert', AlertCreateList.as_view(), name='alert-list-create'),
    # Rattache l'URL /alert/[id d'une Alert] à AlertRetrieveUpdateDestroy
    path('alert/<int:pk>', AlertRetrieveUpdateDestroy.as_view(), name='alert-detail'),
]

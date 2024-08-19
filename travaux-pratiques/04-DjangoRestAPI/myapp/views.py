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

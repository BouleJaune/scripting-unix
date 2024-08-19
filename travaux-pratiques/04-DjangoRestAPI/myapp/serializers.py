from rest_framework import serializers
from .models import Alert


class AlertSerializer(serializers.ModelSerializer):
    """
    Permet de convertir les json en données SQLite
    """
    class Meta:
        model = Alert
        fields = '__all__'

from django.db import models


class Alert(models.Model):
    """
    Défini le format de la donnée Alert
    """
    date = models.TextField()
    serveur = models.TextField()
    criticity = models.TextField()
    infogerant = models.TextField()
    message = models.TextField()
    application = models.TextField()
    environnement = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serveur

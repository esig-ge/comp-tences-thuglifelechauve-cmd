from django.db import models

class Musique(models.Model):
    artiste = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    duree = models.PositiveIntegerField(help_text="Durée en secondes")
    style = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.titre} - {self.artiste}"

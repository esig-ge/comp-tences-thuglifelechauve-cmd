from django.db import models

class Musique(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    duration = models.CharField(max_length=10, blank=True, null=True)  # optionnel
    genre = models.CharField(max_length=50, blank=True, null=True)      # optionnel

    def __str__(self):
        return f"{self.title} - {self.artist}"

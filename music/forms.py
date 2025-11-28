from django import forms
from .models import Musique

class MusiqueForm(forms.ModelForm):
    class Meta:
        model = Musique
        fields = ['artiste', 'titre', 'duree', 'style']

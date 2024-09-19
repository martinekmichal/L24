from django import forms
from .models import kontakt



class KontaktForm(forms.ModelForm):
    class Meta:
        model = kontakt
        fields = ['meno', 'email', 'cislo']
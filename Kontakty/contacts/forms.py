from django import forms
from .models import kontakt


class KontaktSearchForm(forms.Form):
    Kontakt_name = forms.CharField(label='Kontakt name', max_length=100)



class KontaktForm(forms.ModelForm):
    class Meta:
        model = kontakt
        fields = ['meno', 'email', 'cislo']
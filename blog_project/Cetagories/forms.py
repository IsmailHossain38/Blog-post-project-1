from django import forms
from . models import Cetagories
class Cetagoriesform(forms.ModelForm):
    class Meta:
        model = Cetagories
        fields ="__all__"
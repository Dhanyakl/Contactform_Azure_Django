from django import forms
from .models import Contactmodels

class Contactforms(forms.ModelForm):
    class Meta:
        model= Contactmodels
        fields=('name','email','message')
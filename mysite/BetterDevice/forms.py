from .models import Laptop
from django import forms

class LaptopRegistration(forms.ModelForm):
    class Meta:
        model=Laptop
        fields=['manufacture','name','ram','gpu','cpu','price']
from .models import Laptop
from django import forms

class LaptopRegistration(forms.ModelForm):
    class Meta:
        model=Laptop
        field=['manufacture','name','ram','gpu','cpu','price']
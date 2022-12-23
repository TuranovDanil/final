from django import forms
from .models import *


class CreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

from dataclasses import fields
from importlib.metadata import files
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['code','name','description']

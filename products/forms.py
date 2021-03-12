from django import forms 
from .models import *
from django.forms import ModelForm
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','image'] 
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter name of model','aria-describedby':"emailHelp"}),'description': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter the description of product','row':'20'}),'image':forms.FileInput(attrs={'class': 'form-control-file'})}
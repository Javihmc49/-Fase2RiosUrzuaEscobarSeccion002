from django import forms
from .models import Contacto

class Peticiones(forms.Form):
    nombre = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
        attrs = {
            'class':'form-control p-4'
        }
    ))
    Direccion = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
        attrs = {
            'class':'form-control p-4'
        }
    ))

    Apellido =forms.CharField(required=True, max_length=100, widget=forms.TextInput(
        attrs = {
            'class':'form-control p-4'
        }
    ))

    fono = forms.IntegerField(required=True, max_length=100, widget=forms.TextInput(
        attrs = {
            'class':'form-control p-4'
        }
    ))
    email = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(
        attrs = {
            'class':'form-control p-4'
        }
    ))
    fecha = forms.DateField(required=True, max_length=100, widget=forms.TextInput(
        attrs = {
            'class':'form-control p-4'
        }
    ))
    
    motivo = forms.CharField(required=True, max_length=100, widget=forms.TextInput(
        attrs = {
            'class':'form-control p-4'
        }
    ))
    
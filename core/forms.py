from django import forms
from django.forms import ModelForm
from .models import Tattoo, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.widgets import Widget
from django.shortcuts import render, redirect, get_object_or_404
   


class RegistroUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta: 
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso. Prueba con otro.")
        return email

class EditarUserForm(UserCreationForm):
    class Meta: 
        model = User 
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class TattooForm(forms.ModelForm):
    class Meta: 
        model = Tattoo
        fields = [ 'codigo', 'titulo', 'tipo', 'categoria', 'precio','imagen']
        labels = {
            'codigo': 'Codigo',
            'titulo' : 'Titulo',
            'tipo' : 'Tipo',
            'categoria' : 'Categoria',
            'precio' : 'Precio',
            'imagen': 'Imagen'
        }
        widgets ={
            'codigo': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese codigo..',
                    'id': 'codigo',
                    'class': 'form-control'
                }
            ),
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese titulo..',
                    'id': 'titulo',
                    'class': 'form-control'
                }
            ),
            'tipo': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese tipo..',
                    'id': 'tipo',
                    'class': 'form-control'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'id': 'categoria',
                    'class': 'form-control'
                }
            ), 
            'precio': forms.NumberInput(
                attrs={
                    'placeholder': 'Ingrese precio',
                    'id': 'precio',
                    'class': 'form-control'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen',
                }
            )
            
        }

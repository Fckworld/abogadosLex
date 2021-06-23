from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


#Yo creo el formulario con los campos que quiera que
#obviamente tienen que pertenecer a User
class UserCreationFormPersonalizado(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2'] 
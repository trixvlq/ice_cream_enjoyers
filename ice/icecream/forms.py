from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput
from .models import *


class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['title','description','image','price','category']

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
# from django.contrib.auth.models import
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class StudentenDaten(ModelForm):
    class Meta:
        model = Student
        fields = ['matrikelnummer', 'studiengang']


class PruefungCheckin(ModelForm):
    class Meta:
        model = Pruefung
        fields = ['student']


class PruefungForm(ModelForm):
    class Meta:
        model = Pruefung
        fields = '__all__'
        exclude = ['student']
        widgets = {'professor': forms.HiddenInput()}

from django.forms import ModelForm
from django import forms
from .models import *


class Pruefung (ModelForm):

    class Meta:

        model = Pruefung
        fields = '__all__'
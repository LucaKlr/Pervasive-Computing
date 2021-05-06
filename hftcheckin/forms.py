from django.forms import ModelForm
from django import forms
from .models import *


class Pruefung (ModelForm):

    class Meta:

        model = Pruefung
        fields = '__all__'
        labels = {
            'pid': 'Prüfungs ID',
            'passwort': 'Passwort',
            'modul': 'Modul',
            'semester': 'Semester',
            'pruefer': 'Prüfer',
            'raumnummer': 'Raumnummer',
            'dauer': 'Dauer in Minuten'

        }
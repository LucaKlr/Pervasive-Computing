import django_filters
from hftcheckin.models import *


class StudentenFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['vorname', 'nachname', 'studiengang', 'matrikelnummer']


class PruefungenFilter(django_filters.FilterSet):
    class Meta:
        model = Pruefung
        fields = ['modul', 'semester', 'datum']
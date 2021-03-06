from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Einzelne Zeile auskommentieren

'''
    Ganzen Block auskommentieren
'''


class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    vorname = models.CharField(max_length=45, null=True)
    nachname = models.CharField(max_length=45, null=True)
    matrikelnummer = models.CharField(max_length=45, null=True)
    studiengang = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=45, null=True)

    def __str__(self):
        return f'{self.vorname} {self.nachname}'


class Professor(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    titel = models.CharField(max_length=45, null=True)
    vorname = models.CharField(max_length=45, null=True)
    nachname = models.CharField(max_length=45, null=True)
    mitarbeiternummer = models.CharField(max_length=45, null=True)
    email = models.CharField(max_length=45, null=True)

    def __str__(self):
        return f'{self.titel} {self.vorname} {self.nachname}'


class Pruefung(models.Model):
    student = models.ManyToManyField(Student)
    professor = models.ForeignKey(Professor, null=True, on_delete=models.SET_NULL)
    pid = models.CharField(max_length=45, null=False)
    passwort = models.CharField(max_length=45, null=True)
    modul = models.CharField(max_length=45, null=True)
    semester = models.CharField(max_length=45, null=True)
    pruefer = models.CharField(max_length=45, null=True)
    raumnummer = models.CharField(max_length=45, null=True)
    dauer = models.FloatField(max_length=45, null=True)
    datum = models.CharField(max_length=45, null=True)

    def __str__(self):
        return f'{self.modul} {self.semester} {self.pruefer}'

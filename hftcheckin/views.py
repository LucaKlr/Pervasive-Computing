from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from hftcheckin.models import *
from hftcheckin.forms import *
from .forms import CreateUserForm
from .forms import Pruefung
from .models import Pruefung as Pruefungen
from .decorators import allowed_users


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('checkin')
        else:
            messages.info(request, 'Falscher Benutzername oder falsches Passwort.')
    context = {}
    return render(request, 'hftchekin/login.html', context)


def logoutPage(request):
    logout(request)
    messages.info(request, 'Sie haben sich erfolgreich ausgeloggt.')
    return redirect('login')


def registrierung(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            emails = ('@hft-stuttgart.de')
            if email.endswith(emails):
                user = form.save()
                group = Group.objects.get(name='Studenten')
                user.groups.add(group)
                Student.objects.create(
                    user=user,
                    vorname=user.first_name,
                    nachname=user.last_name,
                    email=user.email
                )
                login(request, user)
                messages.success(request, 'Sie haben sich erfolgreich registriert')
                return redirect('registrierung2')
            else:
                messages.info(request, 'Unzulässige E-Mail Adresse')

    context = {'form': form}
    return render(request, 'hftchekin/registrierung.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Studenten'])
def registrierung2(request):
    student = Student.objects.get(user=request.user)
    form = StudentenDaten(instance=student)
    if request.method == 'POST':
        form = StudentenDaten(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'hftchekin/registrierung2.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Studenten'])
def checkin(request):
    return render(request, 'hftchekin/checkin.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Studenten'])
def formular(request):
    return render(request, 'hftchekin/formular.html')


def timer(request):
    return render(request, 'hftchekin/timer.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Studenten'])
def studentkonto(request):
    student = Student.objects.get(user=request.user)
    context = {'student': student}

    return render(request, 'hftchekin/studentkonto.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def professorkonto(request):
    professor = Professor.objects.get(user=request.user)
    context = {'professor': professor}

    return render(request, 'hftchekin/professorkonto.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def pruefungsregistrierung(request):
    form = Pruefung()
    if request.method == 'POST':
        form = Pruefung(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pruefungstabelle')
    context = {'form': form}
    return render(request, 'hftchekin/pruefungsregistrierung.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def professorhome(request):
    return render(request, 'hftchekin/professorhome.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def pruefungstabelle(request):
    pruefungen = Pruefungen.objects.all()
    return render(request, 'hftchekin/pruefungstabelle.html', {'pruefungen': pruefungen})


@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def studententabelle(request):
    return render(request, 'hftchekin/studententabelle.html')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def geschriebenuebersicht(request):
    return render(request, 'hftchekin/geschriebenuebersicht.html')

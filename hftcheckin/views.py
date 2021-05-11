from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from hftcheckin.models import *
from .forms import CreateUserForm
from .decorators import allowed_users

from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('checkin')
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
                form.save()
                return redirect('login')
        context = {'form': form}
        return render(request, 'hftchekin/registrierung.html', context)

# def registrierung2(request):
   # return redirect('login')
   # return render(request, 'hftchekin/registrierung2.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Studenten'])
def checkin(request):
    return render(request, 'hftchekin/checkin.html')


def formular(request):
    return render(request, 'hftchekin/formular.html')

@login_required(login_url='login')
def timer(request):
    return render(request, 'hftchekin/timer.html')

@login_required(login_url='login')
def studentkonto(request):
    return render(request, 'hftchekin/studentkonto.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def professorkonto(request):
    return render(request, 'hftchekin/professorkonto.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def pruefungsregistrierung(request):
    return render(request, 'hftchekin/pruefungsregistrierung.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def professorhome(request):
    return render(request, 'hftchekin/professorhome.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def pruefungstabelle(request):
    return render(request, 'hftchekin/pruefungstabelle.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def studententabelle(request):
    return render(request, 'hftchekin/studententabelle.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def geschriebenuebersicht(request):
    return render(request, 'hftchekin/geschriebenuebersicht.html')





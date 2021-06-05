from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from hftcheckin.forms import *
from .filter import StudentenFilter, PruefungenFilter
from .forms import CreateUserForm
from .forms import PruefungForm
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

    # Daten nach dem POST Request abfangen
    student = Student.objects.get(user=request.user)
    pid = request.POST.get('pid')
    password = request.POST.get('password')

    # Hole die Prüfung und füge den eingeloggten Studenten zur Prüfung hinzu
    # pruefung = Pruefung.objects.get(pid__exact=pid, passwort__exact=password)
    pruefung = get_object_or_404(Pruefung, pid__exact=pid, passwort__exact=password)
    pruefung.student.add(student)

    # Ausgabe der Prüfungs- und Studentendaten
    pruefungsdaten = student.pruefung_set.get(pid__exact=pid, passwort__exact=password)

    context = {
        'student': student,
        'pruefungsdaten': pruefungsdaten,
    }
    return render(request, 'hftchekin/formular.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Studenten'])
def timer(request):
    student = Student.objects.get(user=request.user)
    if request.method == 'POST':
        return redirect('timer')
    return render(request, 'hftchekin/timer.html', {'student': student})


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
    professor = Professor.objects.get(user=request.user)
    form = PruefungForm(initial={'professor': professor})
    if request.method == 'POST':
        form = PruefungForm(request.POST)
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
    professor = Professor.objects.get(user=request.user)
    pruefungen = professor.pruefung_set.all()

    pruefungen_filter = PruefungenFilter(request.GET, queryset=pruefungen)
    pruefung = pruefungen_filter.qs

    context = {'pruefungen': pruefung, 'pruefungen_filter': pruefungen_filter}
    return render(request, 'hftchekin/pruefungstabelle.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Profs'])
def studententabelle(request):
    professor = Professor.objects.get(user=request.user)
    studenten = Student.objects.filter(pruefung__professor=professor)

    studenten_filter = StudentenFilter(request.GET, queryset=studenten)
    student = studenten_filter.qs

    context = {'studenten': student, 'studenten_filter': studenten_filter}
    return render(request, 'hftchekin/studententabelle.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Studenten'])
def geschriebenuebersicht(request):
    student = Student.objects.get(user=request.user)
    if request.method == 'POST':
        return redirect('geschriebenuebersicht')
    return render(request, 'hftchekin/geschriebenuebersicht.html')

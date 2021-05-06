from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
from hftcheckin.models import *
from hftcheckin.forms import *
from django.contrib import messages
from .models import *
from .forms import *

def pruefungsregistrierung(request):
    form = Pruefung()
    if request.method == 'POST':
        form = Pruefung(request.POST)
        if form.is_valid():
            form.save()
        return redirect('pruefungsuebersicht')
        context = {'form': form}
        return render(request, "hftcheckin\pruefungsregistrierung.html", context)


def login(request):
    student = Student.objects.all()

    context = {'student': student}
    return render(request, 'hftchekin/login.html', context)


def registrierung(request):
    return render(request, 'hftchekin/registrierung.html')


def checkin(request):
    return render(request, 'hftchekin/checkin.html')


def formular(request):
    return render(request, 'hftchekin/formular.html')


def timer(request):
    return render(request, 'hftchekin/timer.html')


def studentkonto(request):
    return render(request, 'hftchekin/studentkonto.html')


def professorkonto(request):
    return render(request, 'hftchekin/professorkonto.html')


#def pruefungsregistrierung(request):
 #   return render(request, 'hftchekin/pruefungsregistrierung.html')


def professorhome(request):
    return render(request, 'hftchekin/professorhome.html')


def pruefungstabelle(request):
    return render(request, 'hftchekin/pruefungstabelle.html')


def studententabelle(request):
    return render(request, 'hftchekin/studententabelle.html')


def geschriebenuebersicht(request):
    return render(request, 'hftchekin/geschriebenuebersicht.html')

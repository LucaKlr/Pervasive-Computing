from django.urls import path

from hftcheckin import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('registrierung/', views.registrierung, name='registrierung'),
    path('checkin/', views.checkin, name='checkin'),
    path('formular/', views.formular, name='formular'),
    path('timer/', views.timer, name='timer'),
    path('studentkonto/', views.studentkonto, name='studentkonto'),
    path('professorkonto/', views.professorkonto, name='professorkonto'),
    path('pruefungsregistrierung/', views.pruefungsregistrierung, name='pruefungsregistrierung'),
    path('professorhome/', views.professorhome, name='professorhome'),
    path('pruefungstabelle/', views.pruefungstabelle, name='pruefungstabelle'),
    path('studententabelle/', views.studententabelle, name='studententabelle'),
    path('geschriebenuebersicht/', views.geschriebenuebersicht, name='geschriebenuebersicht'),
    path('registrierung2/', views.registrierung2, name='registrierung2'),
]

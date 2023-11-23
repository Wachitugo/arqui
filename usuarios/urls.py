from django.db import models
from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns= [
    path('eliminaruser/', views.eliminaruser, name='eliminaruser'),
    path('veruser/', views.veruser, name='veruser'),
    path('modificaruser/', views.modificaruser, name='modificaruser'),
    path('agregaruser/', views.agregaruser, name='agregaruser'),
    
]
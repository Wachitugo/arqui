from django.db import models
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'Casino'
urlpatterns= [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("productos/", views.menu, name='menu'),
    path('servicios/', views.mi_perfil, name='mi_perfil'),
    path("registro/", views.registro, name='registro'),
    path('producto/<str:id_producto>/', views.somos, name='producto'),
    path("agendar_servicios/<str:id_servicio>/", views.soporte, name='agendar_servicios'),


    
]
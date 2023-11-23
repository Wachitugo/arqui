from django.urls import path
from . import views

app_name = 'mecanico'

urlpatterns = [
    path('mecanico_agregar/', views.mecanico_agregar, name='mecanico_agregar'),
    path('mecanico_eliminar/', views.mecanico_eliminar, name='mecanico_eliminar'),
    path('mecanico_modificar/', views.mecanico_modificar, name='mecanico_modificar'),
    path('mecanico_ver/', views.mecanico_ver, name='mecanico_ver'),
]
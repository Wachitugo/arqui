from django.shortcuts import render, redirect
from usuarios.models import USUARIO
from mecanico.models import Producto
from mecanico.models import Servicio
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
def index(request):
    return render(request, 'index.html')

def menu(request):
    productos = Producto.objects.all()
    return render(request, 'menu.html', {'productos': productos})


def mi_perfil(request):
    servicios = Servicio.objects.all()
    return render(request, 'mi_perfil.html', {'servicios': servicios})


def soporte(request, id_servicio):
    return render(request, 'soporte.html', {'id_servicio': id_servicio})
    

def somos(request, id_producto):
    producto = get_object_or_404(Producto, ID_PRODUCTO=id_producto)
    todos_productos = Producto.objects.all()[:9]  # Obtén 9 productos
    productos_grupos = zip(*[iter(todos_productos)]*3)
    return render(request, 'somos.html', {'producto': producto, 'productos_grupos': productos_grupos})


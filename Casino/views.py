from django.shortcuts import render, redirect
from mecanico.models import Usuario
from mecanico.models import Producto
from mecanico.models import Servicio
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import UsuarioForm  



def index(request):
    return render(request, 'index.html')

from django.shortcuts import render

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:  # Comprueba si el nombre de usuario o la contraseña están vacíos
            return JsonResponse({'success': False, 'error': 'Falta nombre de usuario o contraseña'})

        try:
            usuario = Usuario.objects.get(NOM_USUARIO=username)
            if password == usuario.CONTRASENA:  
                user, created = User.objects.get_or_create(username=username)
                if created:
                    user.set_unusable_password()  
                    if username == 'admin':  
                        user.is_superuser = True  
                    user.save()
                auth_login(request, user)
                return JsonResponse({'success': True, 'isAdmin': user.is_superuser})  
            return JsonResponse({'success': False, 'error': 'Nombre de usuario o contraseña incorrectos'})
        except Usuario.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Nombre de usuario o contraseña incorrectos'})
    elif request.method == 'GET':
        return render(request, 'login.html')  
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido'})
    
def logout_view(request):
    logout(request)
    return redirect('/')

def menu(request):
    productos = Producto.objects.all()
    return render(request, 'menu.html', {'productos': productos})


def mi_perfil(request):
    servicios = Servicio.objects.all()
    return render(request, 'mi_perfil.html', {'servicios': servicios})



def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UsuarioForm()    
    return render(request, 'registro.html', {'form': form})


def soporte(request, id_servicio):
    servicio = get_object_or_404(Servicio, ID_SERVICIO=id_servicio)
    todos_productos = Producto.objects.all()[:9]  # Obtén 9 productos
    productos_grupos = zip(*[iter(todos_productos)]*3)
    return render(request, 'soporte.html', {'servicio': servicio,'productos_grupos': productos_grupos})
    

def somos(request, id_producto):
    producto = get_object_or_404(Producto, ID_PRODUCTO=id_producto)
    todos_productos = Producto.objects.all()[:9]  # Obtén 9 productos
    productos_grupos = zip(*[iter(todos_productos)]*3)
    return render(request, 'somos.html', {'producto': producto, 'productos_grupos': productos_grupos})




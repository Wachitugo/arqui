from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.


def index(request):
    usuarios = Usuario.objects.all()
    print(usuarios)
    return render(request, 'casino/index.html', {'usuarios': Usuario})






def mecanico_ver(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        usuarios = Usuario.objects.filter(PNOMBRE__icontains=nombre)
    else:
        usuarios = Usuario.objects.all()
    return render(request, 'mecanico_ver.html', {'usuarios': usuarios})

def mecanico_agregar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mecanico/mecanico_ver')
    else:
        form = UsuarioForm()
    return render(request, 'mecanico_agregar.html', {'form': form})

def mecanico_eliminar(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('nombre')
        Usuario.objects.get(pk=usuario_id).delete()
        return redirect('/mecanico/mecanico_ver')
    else:
        usuarios = Usuario.objects.all()
        return render(request, 'mecanico_eliminar.html', {'usuarios': usuarios})

def mecanico_modificar(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('nombre')
        usuario = Usuario.objects.get(pk=usuario_id)
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('/mecanico/mecanico_ver')
    else:
        usuarios = Usuario.objects.all()
        form = UsuarioForm()
        return render(request, 'mecanico_modificar.html', {'usuarios': usuarios, 'form': form})
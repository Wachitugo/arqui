from django.shortcuts import render, redirect, HttpResponse
from .models import USUARIO,CIUDAD
from django.core.exceptions import ObjectDoesNotExist

def eliminaruser(request):
    if request.method == "GET":
        usuarios = USUARIO.objects.all()
        context = {'usuarios': usuarios}
        return render(request, 'eliminaruser.html', context)
    elif request.method == "POST":
        nombre = request.POST["nombre"]
        nom_elegido=USUARIO.objects.get(nombre=nombre)
        nom_elegido.delete()
        usuarios = USUARIO.objects.all()
        context = {'usuarios': usuarios}
        return render(request,'eliminaruser.html',context)

def modificaruser(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        usuario = USUARIO.objects.get(rut=rut)
        ciudades = CIUDAD.objects.all()
        nombre = request.POST["nombre"]
        if USUARIO.objects.filter(nombre=nombre).exclude(rut=rut).exists():
            context = {
                'usuarios': USUARIO.objects.all(),
                'nombre_ciudad': ciudades,
                'usuario': usuario,
                'error_message': 'El nombre ya existe en la base de datos.'
            }
            return render(request, 'modificaruser.html', context)

        usuario.nombre = nombre
        usuario.contra = request.POST["contra"]
        nombre_ciudad = request.POST.get("nombre_ciudad")
        usuario.saldo = request.POST["saldo"]
        usuario.correo = request.POST["correo"]
        objciudad = CIUDAD.objects.get(nombre_ciudad=nombre_ciudad)
        usuario.id_ciudad = objciudad
        usuario.save()
        usuario = USUARIO.objects.get(rut=rut)

        context = {
            'usuarios': USUARIO.objects.all(),
            'nombre_ciudad': ciudades,
            'usuario': usuario
        }

        return render(request, 'modificaruser.html', context)
    else:
        usuarios = USUARIO.objects.all()
        ciudades = CIUDAD.objects.all()
        context = {
            'usuarios': usuarios,
            'nombre_ciudad': ciudades
        }
        return render(request, 'modificaruser.html', context)






def veruser(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        usuarios = USUARIO.objects.filter(nombre=nombre)
        if usuarios.exists():
            context = {'usuario': usuarios}
            return render(request, 'veruser.html', context)
        elif nombre=='':
            usuarios = USUARIO.objects.all()
            context = {'usuario': usuarios}
            return render(request, 'veruser.html', context)
        else:
            context = {'mensaje': 'OK, datos guardados con éxito'}
            return render(request, 'veruser.html', context)
    else:
        usuarios = USUARIO.objects.all()
        context = {'usuario': usuarios}
        return render(request, 'veruser.html', context)


def agregaruser(request):
    if request.method == "GET":
        ciudades = CIUDAD.objects.all()
        context = {'nombre_ciudad': ciudades}
        return render(request, 'agregaruser.html', context)
    elif request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]

        contra = request.POST["contra"]
        id_ciudad = request.POST["nombre_ciudad"]
        saldo = request.POST["saldo"]
        correo = request.POST["correo"]
        if USUARIO.objects.filter(nombre=nombre).exists():
            ciudades = CIUDAD.objects.all()
            context = {'nombre_ciudad': ciudades, 'error_message': 'El nombre ya existe en la base de datos.'}
            return render(request, 'agregaruser.html', context)

        objCiudad = CIUDAD.objects.get(id_ciudad=id_ciudad)
        obj = USUARIO.objects.create(rut=rut,
                                     nombre=nombre,
                                     contra=contra,
                                     id_ciudad=objCiudad,
                                     saldo=saldo,
                                     correo=correo,
                                     )
        obj.save()
        
        ciudades = CIUDAD.objects.all()
        context = {'nombre_ciudad': ciudades, 'mensaje': 'OK, datos guardados con éxito'}
        return render(request, 'agregaruser.html', context)
    
    

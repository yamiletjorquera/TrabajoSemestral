from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    context = {}
    return render(request, 'pages/index.html', context)

def mostnew(request):
    context = {}
    return render(request, 'pages/Mostnew.html', context)

def writers(request):
    context = {}
    return render(request, 'pages/Writers.html', context)

def generos(request):
    context = {}
    return render(request, 'pages/Generos.html', context)

def escritor(request):
    context = {}
    return render(request, 'pages/Escritor.html', context)

def formulario(request):
    rut = request.POST["txtRut"]
    nombre = request.POST["txtNombre"]
    apPaterno = request.POST["txtAppaterno"]
    apMaterno = request.POST["txtApmaterno"]
    fecNac = request.POST["txtFecha"]
    genero = request.POST["optGenero"]
    correo = request.POST["txtMail"]    
    contraseña = request.POST["txtPassword"]
    activo = True

    obj = User.objects.create(
        rut=rut,
        nombre=nombre,
        apellido_paterno=apPaterno,
        apellido_materno=apMaterno,
        fecha_nacimiento=fecNac,
        genero=genero,
        correo=correo,
        contraseña=contraseña,
        activo=activo,
    )
    obj.save()
    context = {}
    return render(request, 'pages/Formulario.html', context)

def crud(request):
    usuarios = User.objects.all()
    context = {
        "usuarios": usuarios,
    }

    return render(request, 'pages/Crud.html', context)
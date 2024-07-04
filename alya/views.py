from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('index')


def index(request):
    if request.method != "POST":
        context = {

        }
        return render(request,"pages/index.html",context)
    else:
        username = request.POST["txtUser"]
        password = request.POST["txtPass"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            usuarios = User.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/index.html",context)
        else:
            context = {
                "mensaje":"Correo o contraseña incorrecta",
                "design":"alert alert-danger w-20 mx-3 text-center",
            }
            return render(request,"pages/index.html",context)

def mostnew(request):
    if request.method != "POST":
        context = {

        }
        return render(request,"pages/Mostnew.html",context)
    else:
        username = request.POST["txtUser"]
        password = request.POST["txtPass"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            usuarios = User.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/Mostnew.html",context)
        else:
            context = {
                "mensaje":"Correo o contraseña incorrecta",
                "design":"alert alert-danger w-20 mx-3 text-center",
            }
            return render(request,"pages/Mostnew.html",context)

def writers(request):
    if request.method != "POST":
        context = {

        }
        return render(request,"pages/Writers.html",context)
    else:
        username = request.POST["txtUser"]
        password = request.POST["txtPass"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            usuarios = User.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/Writers.html",context)
        else:
            context = {
                "mensaje":"Correo o contraseña incorrecta",
                "design":"alert alert-danger w-20 mx-3 text-center",
            }
            return render(request,"pages/Writers.html",context)

def generos(request):
    if request.method != "POST":
        context = {

        }
        return render(request,"pages/Generos.html",context)
    else:
        username = request.POST["txtUser"]
        password = request.POST["txtPass"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            usuarios = User.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/Generos.html",context)
        else:
            context = {
                "mensaje":"Correo o contraseña incorrecta",
                "design":"alert alert-danger w-20 mx-3 text-center",
            }
            return render(request,"pages/Generos.html",context)

def escritor(request):
    if request.method != "POST":
        context = {

        }
        return render(request,"pages/Escritor.html",context)
    else:
        username = request.POST["txtUser"]
        password = request.POST["txtPass"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            usuarios = User.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/Escritor.html",context)
        else:
            context = {
                "mensaje":"Correo o contraseña incorrecta",
                "design":"alert alert-danger w-20 mx-3 text-center",
            }
            return render(request,"pages/Escritor.html",context)

def crud(request):
    usuarios = User.objects.all()
    context = {
        "usuarios": usuarios,
    }

    return render(request, 'pages/Crud.html', context)

def formulario(request):
    if request.method != "POST":
        context = {}
        return render(request, 'pages/Formulario.html', context)
    else:
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


def usuario_editar(request,pk):
    if pk!="":
        usuario = User.objects.get(rut=pk)

        context={
            "usuario":usuario,
        }
        return render(request,"pages/Formulario_editar.html",context)
    else:
        usuarios = User.objects.all()
        context={
            "mensaje": "Error, Rut no encontrado",
            "usuarios":usuarios,
        }
        return render(request,"pages/Crud.html",context)


def formulario_editar(request):
    if request.method=="POST":
        rut = request.POST["txtRut"]
        nombre = request.POST["txtNombre"]
        apPaterno = request.POST["txtAppaterno"]
        apMaterno = request.POST["txtApmaterno"]
        fecNac = request.POST["txtFecha"]
        genero = request.POST["optGenero"]
        correo = request.POST["txtMail"]    
        contraseña = request.POST["txtPassword"]
        activo = True


        obj = User(
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
        context = {
            "usuario":obj,
        }
        return render(request, 'pages/Formulario_editar.html', context)


def deletear_usuario(request, pk):
    try:
        usuario = User.objects.get(rut=pk)
        usuario.delete()

        usuarios = User.objects.all()
        context = {
            "mensaje": "Registro eliminado",
            "usuarios": usuarios,
        }
        return render(request, "pages/Crud.html", context)
    except:
        usuarios = User.objects.all()
        context = {
            "mensaje": "Error, Rut no encontrado",
            "usuarios": usuarios,
        }
        return render(request, "pages/Crud.html", context)
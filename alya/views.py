from django.shortcuts import render,redirect
from .models import Usuario
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

            usuarios = Usuario.objects.all()
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

def carrito(request):
    if request.method != "POST":
        context = {

        }
        return render(request,"pages/Carrito.html",context)
    else:
        username = request.POST["txtUser"]
        password = request.POST["txtPass"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)

            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/Carrito.html",context)
        else:
            context = {
                "mensaje":"Correo o contraseña incorrecta",
                "design":"alert alert-danger w-20 mx-3 text-center",
            }
            return render(request,"pages/Carrito.html",context)

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

            usuarios = Usuario.objects.all()
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

            usuarios = Usuario.objects.all()
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

            usuarios = Usuario.objects.all()
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

            usuarios = Usuario.objects.all()
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

@login_required
def crud(request):
    usuarios = Usuario.objects.all()
    context = {
        "usuarios": usuarios,
    }

    return render(request, 'pages/Crud.html', context)

@login_required
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

        user = User.objects.create_user(
            username=correo,
            password=contraseña,
            first_name=nombre,
            last_name=apPaterno 
        )

        obj = Usuario.objects.create(
            user=user,
            rut=rut,
            apellido_materno=apMaterno,
            fecha_nacimiento=fecNac,
            genero=genero,
            activo=activo,
        )
        obj.save()
        context = {}
        return render(request, 'pages/Formulario.html', context)

@login_required
def usuario_editar(request,pk):
    if pk!="":
        usuario = Usuario.objects.get(rut=pk)

        context={
            "usuario":usuario,
        }
        return render(request,"pages/Formulario_editar.html",context)
    else:
        usuarios = Usuario.objects.all()
        context={
            "mensaje": "Error, Rut no encontrado",
            "usuarios":usuarios,
        }
        return render(request,"pages/Crud.html",context)

@login_required
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

        user = User(
            username=correo,
            password=contraseña,
            first_name=nombre,
            last_name=apPaterno 
        )

        obj = Usuario(
            user=user,
            rut=rut,
            apellido_materno=apMaterno,
            fecha_nacimiento=fecNac,
            genero=genero,
            activo=activo,
        )
        user.save()
        obj.save()
        context = {
            "usuario":obj,
        }
        return render(request, 'pages/Formulario_editar.html', context)

@login_required
def deletear_usuario(request, pk):
    try:
        usuario = Usuario.objects.get(rut=pk)

        user = usuario.user

        usuario.delete()

        user.delete()

        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Registro eliminado",
            "usuarios": usuarios,
        }
        return render(request, "pages/Crud.html", context)
    except:
        usuarios = Usuario.objects.all()
        context = {
            "mensaje": "Error, Rut no encontrado",
            "usuarios": usuarios,
        }
        return render(request, "pages/Crud.html", context)
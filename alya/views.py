from django.shortcuts import render

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
    context = {}
    return render(request, 'pages/Formulario.html', context)

def crud(request):
    context = {}
    return render(request, 'pages/Crud.html', context)
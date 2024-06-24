from django.shortcuts import render

# Create your views here.

def PaginaInicial(request):
    context = {
        "user": "",
    }
    return render(request, "PaginaInicial.html", context)
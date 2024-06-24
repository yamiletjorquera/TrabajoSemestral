from django.urls import path
from GameStore import views

urlpatterns = [
    path("",views.PaginaInicial, name="PaginaInicial"),
]
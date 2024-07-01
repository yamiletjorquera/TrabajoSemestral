from django.urls import path
from . import views


urlpatterns = [
    path('inicio', views.index, name='index'),
    path('nuevo', views.mostnew, name='nuevo'),
    path('escritores', views.writers, name='escritores'),
    path('generos', views.generos, name='generos'),
    path('escritor', views.escritor, name='escritor'),
    path('formulario', views.formulario, name='formulario'),
    path('crud', views.crud, name='crud')
]

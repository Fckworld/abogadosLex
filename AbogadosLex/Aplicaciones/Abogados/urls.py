#Esta la cree yo!
from django.contrib import admin
from django.urls import path
from Aplicaciones.Abogados.views import *

urlpatterns = [
    path('',index, name = 'LogInPage'),
    path('listaContrato/',gestionContrato),
    path('crearusuario/',crearUsuario),
    path('registro/',paginaRegistro, name = 'RegisterPage'),
    path('miinicio/',paginaLogeo),

]
from django.shortcuts import render
from .models import Contrato
from django.contrib.auth.forms import UserCreationForm #Formulario Django
from django.contrib.auth.models import User
from django.db import *
from .forms import UserCreationFormPersonalizado #Importa formulario Avanzado
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def gestionContrato(request):
    contratosListados = Contrato.objects.all()
    return render(request,'gestionContratos.html',{'contratos':contratosListados})

def crearUsuario(request): #Formulario Basico Django

    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                crearUsuario = User.objects.create_user(request.POST.get('username'),password=request.POST.get('password1'))
                crearUsuario.save()
                return render(request,'crearCuenta.html',{'formulario':UserCreationForm(),'info':'El usuario'+request.POST.get('username')+'fue creado exitosamente.'})
            except IntegrityError:
                return render(request,'crearCuenta.html',{'formulario':UserCreationForm(),'info':'El usuario'+request.POST.get('username')+'ya se está registrado.'})
        else:
            return render(request,'crearCuenta.html',{'formulario':UserCreationForm(),'error':'Las contraseñas no coinciden.'})
    else:
        return render(request,'crearCuenta.html',{'formulario':UserCreationForm})

def paginaRegistro(request):
    #formularioBasico = UserCreationForm()
    formularioAvanzado = UserCreationFormPersonalizado()
    if request.method=='POST':
        #formularioBasico = UserCreationForm(request.POST)
        formularioAvanzado = UserCreationFormPersonalizado(request.POST)
        if formularioAvanzado.is_valid():
            formularioAvanzado.save()
            nombre = formularioAvanzado.cleaned_data.get('first_name')
            messages.success(request,'Cuenta creada por '+nombre)
    data = {
        'formulario': formularioAvanzado
    }
    return render(request,'registro.html',data)

def index(request):
    return render(request,'index.html')

def paginaLogeo(request):
    data = {}
    return render(request,'inicio.html')
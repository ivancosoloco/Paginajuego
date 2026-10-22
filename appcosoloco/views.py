from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, 'appcosoloco/inicio.html')

def historia(request):
    return render(request, 'appcosoloco/historia.html')

def desarrollo(request):
    return render(request, 'appcosoloco/desarrollo.html')

def contacto(request):
    return render(request, 'appcosoloco/contacto.html')

def descargar(request):
    return render(request, 'appcosoloco/descargar.html')
from django.shortcuts import render
from .models import Dojo, Evento  # Supondo que você criou um modelo para Eventos

def home(request):
    dojo = Dojo.objects.first()  # Pega o primeiro dojo cadastrado
    return render(request, 'dojo/home.html', {'dojo': dojo})

def sobre(request):
    dojo = Dojo.objects.first()
    return render(request, 'dojo/sobre.html', {'dojo': dojo})

def eventos(request):
    eventos = Evento.objects.all()  # Lista todos os eventos
    return render(request, 'dojo/eventos.html', {'eventos': eventos})

def contato(request):
    dojo = Dojo.objects.first()
    return render(request, 'dojo/contato.html', {'dojo': dojo})
from django.shortcuts import render
from .models import Dojo

def dojo_info(request):
    dojo = Dojo.objects.first()  # Pega o primeiro dojo cadastrado
    return render(request, 'dojo/dojo_info.html', {'dojo': dojo})
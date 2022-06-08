from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def graficas(request):
    return render(request, 'graficas.html')

def procesadores(request):
    return render(request, 'procesadores.html')
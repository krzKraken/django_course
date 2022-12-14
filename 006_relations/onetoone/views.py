from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def create(request):
    # Creacion de elementos
    return HttpResponse("Datos creados")

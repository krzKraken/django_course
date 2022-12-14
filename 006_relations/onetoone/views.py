from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.
def create(request):
    # Creacion de elementos con relacion 1 a 1
    place = Place(name="lugar 1", address="calle demo")
    place.save()

    restaurant = Restaurant(place=place, number_off_employees=8)
    restaurant.save()

    return HttpResponse(restaurant.place.name)

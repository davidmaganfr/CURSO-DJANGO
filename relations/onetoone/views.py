from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

def create(request):
    place = Place(name='lugar 1', address='calle demo') #Creacion del objeto
    place.save() #Guardado del objeto

    restaurant = Restaurant(place=place, number_of_employees=8) #creacion del objeto
    restaurant.save() #guardado del objeto

    return HttpResponse(restaurant.place.name)

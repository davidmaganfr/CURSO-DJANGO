from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

def test(request):
    return HttpResponse('Funciona correctamente')

def create(request):
    # comment = Comment(name='Juanjo', score=5, comment='Este es un comentario')
    # comment.save() 
    comment = Comment.objects.create(name='Alex') #Crear y guardar objeto sin necesiddad de otro comando
    return HttpResponse('Ruta para probar la creacion de modelos')

def delete(request): # BORRAR objetos de comentario
    comment = Comment.objects.get(id=1) # PRIMERA FORMA DE BORRAR EL OBJETO
    comment.delete() # PRIMERA FORMA DE BORRAR EL OBJETO
    Comment.objects.filter(id=2).delete() # SEGUNDA FORMA DE BORRAR EL OBJETO

    return HttpResponse('Ruta para probar los borrados')
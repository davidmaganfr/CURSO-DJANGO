from django.shortcuts import render
from .models import Autor, Entry
from django.http import HttpResponse

def update(request):
    autor1 = Autor.objects.get(id=1)
    autor1.name = 'Juanjo' # modifico el nombre del id=1
    autor1.email = 'juanjo@demo.com' # modifico su email id=1
    autor1.save()
    return HttpResponse('Nombre modificado')

def queries(request):
    # obtener todos los elementos de un objeto
    autores = Autor.objects.all()
    # Aplicar un filtro para obtener datos concretos
    autores_filtrados = Autor.objects.filter(email='anne74@example.org')
    # Obtener UN UNICO DATO FILTRADO
    autor = Autor.objects.get(id=1)
    # Obtener datos CON UNA LIMITACION de elementos (10 en este caso)
    limit = Autor.objects.all()[:10]
    # Obtener datos indexando a partir del 5 elemento
    offsets = Autor.objects.all()[5:15]
    # Ordena en orden alfabetico los emails
    orden = Autor.objects.all().order_by('email')
    # Obtener todos los elementos que su ID sea <=15
    filtrados = Autor.objects.filter(id__lte=15)
    # Obtener todos los autores que contienen la palabra yes en su nombre
    palabra_clave = Autor.objects.filter(name__contains='yes')

    return render(request, 'post/queries.html', {'autores': autores, 'autores_filtrados': autores_filtrados, 'autor': autor, 'limit': limit, 'offsets': offsets, 'orden': orden, 'filtrados': filtrados, 'palabra_clave': palabra_clave })

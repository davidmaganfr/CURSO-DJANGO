from django.shortcuts import render
from .models import Autor, Entry

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

    return render(request, 'post/queries.html', {'autores': autores, 'autores_filtrados': autores_filtrados, 'autor': autor, 'limit': limit, 'offsets': offsets })



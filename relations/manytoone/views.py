from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Articles
from datetime import date

def create(request):
    rep = Reporter(first_name='David', last_name='Magan', email='david@demo.com')
    rep.save()

    art = Articles(headline='lorem ipsum dolot', pub_date= date(2022,5,5), reporter=rep)
    art.save()
    art2 = Articles(headline='deportes', pub_date=date(2022,4,4), reporter=rep)
    art2.save()
    art3 = Articles(headline='investigacion', pub_date=date(2022,3,3), reporter=rep)
    art3.save()
    
    # Accedemos a todos los articulos que ha hecho el resportero
    result2 = rep.articles_set.all()
    # Accedemos al nombre del reportero que crea el articulo
    result = art.reporter.first_name
    # Filtramos para obtener un unico articulo
    result3 = rep.articles_set.filter(headline='deportes')
    # Comando para obtener el numero de articulos escritos
    result4 = rep.articles_set.count()

    return HttpResponse(result4)


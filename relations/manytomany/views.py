from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Publication

def create(request):
    #OBLIGATORIO GUARDAR LOS OBJETOS DE QUEDEBEMOS RELACIONAR
    article1= Article(headline='Articulo Nº1')
    article1.save()
    article2= Article(headline='Articulo Nº2')
    article2.save()
    article3= Article(headline='Articulo Nº3')
    article3.save()

    pub1= Publication(title='Publicacion primera')
    pub1.save()
    pub2= Publication(title='Publicacion segunda')
    pub2.save()
    pub3= Publication(title='Publicacion tercera')
    pub3.save()
    pub4= Publication(title='Publicacion cuarta')
    pub4.save()
    pub5= Publication(title='Publicacion quinta')
    pub5.save()
    pub6= Publication(title='Publicacion sexta')
    pub6.save()
    pub7= Publication(title='Publicacion septima')
    pub7.save()

    #RELACIONA ARTICULOS CON PUBLICACIONES
    article1.publications.add(pub1)
    article1.publications.add(pub2)
    article1.publications.add(pub3)
    article2.publications.add(pub4)
    article2.publications.add(pub5)
    article3.publications.add(pub6)
    article3.publications.add(pub7)

    #FORMA DE ACCEDER A TODAS LAS PUBLICACIONES DEL ARTICULO 1
    result = article1.publications.all()

    # Creacion del objeto para Acceder a los articulos de una publicacion especifica
    pub1 = Publication.objects.get(id=1)
    # FORMA DE ACCEDER A LOS ARTICULOS DESDE LA PUBLICACION
    result2 = pub1.article_set.all()

    #ELIMINAR RELACION DE UN ARTICULO CON UNA PUBLICACION
    #article1.publications.remove(pub1)


    return HttpResponse(result2)

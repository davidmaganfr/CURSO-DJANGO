from django.shortcuts import render, HttpResponse

def saludo(request):
    return HttpResponse('hola')

def adulto(request, edad):
    if edad > 18:
        return HttpResponse('eres mayor de edad')
    else:
        return HttpResponse('no puedes acceder, eres menor de edad')

def simple(request):
    return render(request, 'simple.html', {})

def dinamico(request, name):
    categories = ['code', 'design', 'marketing']
    context = {'name' : name, 'categories' : categories}
    return render(request, 'dinamico.html', context)

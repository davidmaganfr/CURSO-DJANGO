from django.shortcuts import render

def presentacion(request):
    return render(request, 'presentacion.html', {})

def formacion(request):
    return render(request, 'formacion.html', {})

def experiencia(request):
    return render(request, 'experiencia.html', {})
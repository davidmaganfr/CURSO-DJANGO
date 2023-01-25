
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo, name='saludo'),
    path('adulto/<int:edad>/', views.adulto, name='adulto'),
    path('simple/', views.simple, name='simple'),
    path('dinamico/<str:name>/', views.dinamico, name='dinamico')
]

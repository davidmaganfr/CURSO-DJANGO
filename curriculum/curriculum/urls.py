from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.presentacion, name='presentacion'),
    path('formacion/', views.formacion, name='formacion'),
    path('experiencia/', views.experiencia, name='experiencia')
]

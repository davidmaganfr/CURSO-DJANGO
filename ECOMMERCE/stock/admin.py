from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','short_description', 'stock')#Nos muestra todos los valores en una tabla
    search_fields = ('name', 'short_description') #Incluye una barra de busqueda
    list_filter = ('stock', 'discount_until', 'name')#filtar por stock, fecha o nombre
    date_hierarchy = 'discount_until' #filtra por fechas encima del panel


admin.site.register(Product, ProductAdmin)
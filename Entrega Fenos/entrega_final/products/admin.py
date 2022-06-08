from django.contrib import admin

from products.models import Products, Graficas, Procesadores

# Register your models here.

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'SKU', 'is_active']
    

@admin.register(Graficas)
class GraficasAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'memory' ,'SKU', 'is_active']

@admin.register(Procesadores)
class ProcesadoresAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'cache', 'cores', 'SKU', 'is_active']
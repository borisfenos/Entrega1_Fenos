from django.contrib import admin
from django.urls import path, include

from entrega_final.views import index, contact, graficas, procesadores
from products.views import Create_grafica, Create_procesador




urlpatterns = [
    path('', index, name = 'index'),
    
    path('admin/', admin.site.urls),

    path('contact/', contact, name = 'contacto'),

    path('products/', include('products.urls')),

    path('graficas/', graficas, name='graficas'),
    
    path('procesadores/', procesadores, name='procesadores'),

    path('products/create-grafica/', Create_grafica.as_view(), name='create_grafica'),
    path('products/create-procesador/', Create_procesador.as_view(), name='create_procesador'),
]


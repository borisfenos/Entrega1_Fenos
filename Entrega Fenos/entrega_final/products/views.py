from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from products.models import Procesadores, Products, Graficas
from products.forms import Product_form, Grafica_form, Procesador_form

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class List_products(ListView):
    model = Products
    template_name= 'products.html'
    queryset = Products.objects.filter(is_active = True)

class List_graficas(ListView):
    model = Graficas
    template_name= 'graficas.html'
    queryset = Graficas.objects.filter(is_active = True)

class List_procesadores(ListView):
    model = Procesadores
    template_name= 'procesadores.html'
    queryset = Procesadores.objects.filter(is_active = True)

class Detail_product(DetailView):
    model = Products
    template_name= 'detail_product.html'

class Create_product(CreateView):
    model = Products
    template_name = 'create_products.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_product', kwargs={'pk':self.object.pk})

class Create_grafica(CreateView):
    model = Graficas
    template_name = 'create_grafica.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_grafica', kwargs={'pk':self.object.pk})

class Create_procesador(CreateView):
    model = Procesadores
    template_name = 'create_procesador.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_procesador', kwargs={'pk':self.object.pk})

class Delete_product(DeleteView):
    model = Products
    template_name = 'delete_product.html'

    def get_success_url(self):
        return reverse('list_products')

class Update_product(UpdateView):
    model = Products
    template_name = 'update_product.html'
    fields = '__all__'


    def get_success_url(self):
        return reverse('detail_product', kwargs = {'pk':self.object.pk})

def search_products(request):
    products = Products.objects.filter(name__icontains=request.GET['search'])
    if products.exists():
        context = {'products':products}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'search_products.html', context = context)
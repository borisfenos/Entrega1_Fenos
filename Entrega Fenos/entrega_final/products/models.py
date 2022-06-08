from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'


class Graficas(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    memory = models.IntegerField(null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'grafica'
        verbose_name_plural = 'graficas'

class Procesadores(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    cache = models.IntegerField(null=True)
    cores = models.IntegerField(null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'procesador'
        verbose_name_plural = 'procesadores'

from django.db import models
#from locales.models import localDatos

#from multiselectfield import MultiSelectField
# Create your models here.

class Productos(models.Model):
    nombre = models.TextField(max_length=20, null=True, blank=True)
    descripcion = models.TextField(max_length=70, null=True, blank=True)
    precio = models.IntegerField(null=True)
    
#class MyModel(models.Model):

 #   my_field = Multiselectfield(choices=Productos.nombre)

"""
class Productos_Local(models.Model):
    nro_local = models.IntegerField(null=True, blank=True),
    producto = models.TextField(max_length=20, null=True, blank=True)
   """






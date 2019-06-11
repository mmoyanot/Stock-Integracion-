from django.db import models
from empresa.models import empresaDatos
#from locales.models import localDatos

#from multiselectfield import MultiSelectField
# Create your models here.

class Productos(models.Model):
    nombre = models.TextField(max_length=20, null=True, blank=True)
    descripcion = models.TextField(max_length=70, null=True, blank=True)
    precio = models.IntegerField(null=False)
    
#class MyModel(models.Model):

 #   my_field = Multiselectfield(choices=Productos.nombre)


class productosLocal(models.Model):
    nombreProducto = models.CharField(max_length=70)
    cantidad = models.IntegerField(null=False)
    direccion_local = models.CharField(max_length=70)
    rutEmpresa = models.ForeignKey(empresaDatos, on_delete=models.CASCADE, blank=True, null=False)
    def _str_(self):
        return self.nombreProducto






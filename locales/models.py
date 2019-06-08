from django.db import models
from django.contrib.auth.models import AbstractUser
from empresa.models import empresaDatos
# Create your models here.

class localDatos(models.Model):
    direccion_local = models.CharField(max_length=70, null=True, blank=True)
    rutEmpresa = models.ForeignKey( empresaDatos, on_delete=models.CASCADE, blank=True, null=False)
    def _str_(self):
        return self.nombre
   
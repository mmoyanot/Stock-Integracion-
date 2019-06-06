from django.db import models
from django.contrib.auth.models import AbstractUser
from adminEmpresa.models import adminDatos
# Create your models here.

class empresaDatos(models.Model):
    nombreEmpresa = models.CharField(max_length=70, null=True, blank=True)
    rutEmpresa = models.CharField(max_length=12, null=False, blank=True, primary_key=True)
    rutAdmin = models.ForeignKey( adminDatos, on_delete=models.CASCADE, blank=True, null=True)
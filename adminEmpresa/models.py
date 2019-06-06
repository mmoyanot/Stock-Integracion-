from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class tipoUsuario(models.Model):
    descUsuario = models.CharField(max_length=70, null=False, blank=True)
   

class adminDatos(models.Model):
    nomAdmin = models.CharField(max_length=70, null=True, blank=True)
    rutAdmin = models.CharField (max_length=12, primary_key=True)
    emailAdmin = models.CharField(max_length=70, null=True, blank=True)
    passAdmin = models.CharField(max_length=12, null=True, blank=True)
    id_tipoUsuario = models.ForeignKey(tipoUsuario, on_delete=models.CASCADE, blank=True, null=True, default=1)


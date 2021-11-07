from django.db import models

# Create your models here.
class Referencia(models.Model):
    nombre = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    numeros = models.CharField(max_length=30)
    correo = models.EmailField(blank=True, null=True)
    empresa = models.CharField(max_length=100)
    
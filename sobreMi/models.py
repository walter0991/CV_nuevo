from django.db import models

# Create your models here.
class SobreMi(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefonos = models.CharField(max_length=50)
    correo = models.EmailField()
    descripcion = models.CharField(max_length=1000)
    
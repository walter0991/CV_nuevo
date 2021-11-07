from django.db import models

# Create your models here.
class Experiencia(models.Model):
    cargo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    
    
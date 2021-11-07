from django.db import models

# Create your models here.
class Educacion(models.Model):
    unidadEducativa = (models.CharField(max_length=100))
    titulo = (models.CharField(max_length=100))
    fecha = (models.CharField(max_length=100))
    
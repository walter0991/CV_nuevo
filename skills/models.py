from django.db import models

# Create your models here.
class Skill(models.Model):
    nombre = models.CharField(max_length=50)
    
class Desarrollo(models.Model):
    link = models.CharField(max_length=100)
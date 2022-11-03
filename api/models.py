
from django.db import models

class Usuario(models.Model):
    region = models.CharField(max_length=255)
    centroFormacion= models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    cedula = models.PositiveIntegerField()
    telefono = models.PositiveIntegerField()
    email = models.EmailField(max_length=254)
    profesion = models.CharField(max_length=255)
    descripcion = models.TextField()
    años = models.PositiveIntegerField()
    

    def __str__(self) -> str:
        return self.name
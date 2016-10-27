from django.db import models

class Comentario(models.Model):
    """docstring for Comentario"""
    nombre = models.CharField(max_length=128 , )
    email  = models.EmailField(unique = True)
    telefono = models.CharField(max_length=20 ,)
    comentario = models.TextField(default = None)

    def __str__(self):
        return self.nombre




# Create your models here.

from django.db import models

class Categoria (models.Model):
    nombre = models.CharField(
        max_length = 50, 
        unique = True,
        error_messages = {
            'unique': 'Ya existe una categoría con este nombre.'
        }
    )
    descripcion = models.CharField(max_length = 255)
    estado = models.IntegerField(default=1)
    createdAt = models.DateTimeField(auto_now=True)
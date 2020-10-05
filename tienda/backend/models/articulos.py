from django.db import models

class Articulo (models.Model):
    ACTIVO = 1
    INACTIVO = 0
    
    ESTADO = (
        (ACTIVO, 'Articulo disponible'),
        (INACTIVO, 'Articulo no disponible')
    )
    
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(max_length=500, blank=True)
    precio = models.FloatField()
    estado = models.IntegerField(choices=ESTADO, default=ACTIVO)
    existencias = models.IntegerField()
    # descuento = models.FloatField()
    createdAt = models.DateField(auto_now=True)
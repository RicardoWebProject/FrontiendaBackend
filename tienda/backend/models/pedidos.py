from django.db import models

class Pedido (models.Model):
    cantidad = models.IntegerField()
    fecha_hora = models.DateTimeField(auto_now=True)
    articulo = models.ForeignKey('backend.Articulo', on_delete=models.CASCADE)
    cliente = models.ForeignKey('backend.Cliente', on_delete=models.CASCADE)
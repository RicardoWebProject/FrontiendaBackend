from django.db import models

class Cliente (models.Model):
    CLIENTE = 1

    tipo = models.IntegerField(default=CLIENTE)
    nombre = models.CharField(max_length=255)
    saldo = models.FloatField()
    credito_limite = models.FloatField()

class Fabrica (models.Model):
    telefono = models.IntegerField()
    cantidad_proveida = models.IntegerField()
    fabrica_principal = models.BooleanField()
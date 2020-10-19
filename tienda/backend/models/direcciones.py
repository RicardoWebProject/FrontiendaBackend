from django.db import models

class Direcciones (models.Model):
    no_calle = models.IntegerField()
    comuna = models.CharField(max_length = 250)
    ciudad = models.CharField(max_length = 250)
    createdAt = models.DateField(auto_now = True)
    cliente = models.ForeignKey('backend.Cliente', related_name='direcciones', on_delete=models.CASCADE)
from rest_framework import serializers
#Modelo del serializador
from ..models.articulos import Articulo

class ArticuloSerializer (serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['id', 'nombre', 'descripcion', 'precio', 'estado', 'existencias', 'createdAt']
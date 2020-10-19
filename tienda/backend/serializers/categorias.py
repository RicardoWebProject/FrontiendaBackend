from rest_framework import serializers
#Modelo de este serializador
from ..models.categorias import Categoria

class CategoriaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'estado', 'createdAt']
from rest_framework import serializers
#Modelo
from ..models.direcciones import Direcciones

class DireccionesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Direcciones
        fields = ['no_calle', 'comuna', 'ciudad']
        read_only_fields = ['created_at']
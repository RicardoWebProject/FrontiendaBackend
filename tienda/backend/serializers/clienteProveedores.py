from rest_framework import serializers
#Modelos
from ..models.clienteProveedores import Cliente, Fabrica
from ..models.direcciones import Direcciones
#Serializador para direcciones de cliente
from .direcciones import DireccionesSerializer

class ClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'saldo', 'credito_limite', 'no_calle', 'comuna', 'ciudad']
    
    # def create(self, validated_data):
    #     direcciones_data = validated_data.pop('direcciones')
    #     cliente = Cliente.objects.create(**validated_data)
    #     for direccion_data in direccion_data:
    #         Direcciones.objects.create(cliente = cliente, **direccion_data)
    #     return cliente

class FabricaSerializer (serializers.ModelSerializer):
    class Meta:
        model = Fabrica
        fields = '__all__'
from rest_framework import serializers
#Modelo
from ..models.pedidos import Pedido

class PedidosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = []
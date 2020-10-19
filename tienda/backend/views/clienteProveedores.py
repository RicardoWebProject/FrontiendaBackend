from rest_framework import viewsets
#Modelo
from ..models.clienteProveedores import Cliente, Fabrica
#Serializadores
from ..serializers.clienteProveedores import ClienteSerializer, FabricaSerializer

class ClienteViewSet (viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = []

class FabricaViewSet (viewsets.ModelViewSet):
    queryset = Fabrica.objects.all()
    serializer_class = FabricaSerializer
    permission_classes = []
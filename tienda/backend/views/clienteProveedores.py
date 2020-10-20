from rest_framework import viewsets
#Modelo
from ..models.clienteProveedores import Cliente, Fabrica
#Serializadores
from ..serializers.clienteProveedores import ClienteSerializer, FabricaSerializer
#Permisos
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class ClienteViewSet (viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

class FabricaViewSet (viewsets.ModelViewSet):
    queryset = Fabrica.objects.all()
    serializer_class = FabricaSerializer
    permission_classes = [IsAuthenticated]
#Vistas
from rest_framework import viewsets
#Modelo
from ..models.direcciones import Direcciones
#Serializador
from ..serializers.direcciones import DireccionesSerializer

class DireccionesViewSet (viewsets.ModelViewSet):
    queryset = Direcciones.objects.all()
    serializer_class = DireccionesSerializer
    permission_classes = []
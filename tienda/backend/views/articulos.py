#Vistas
from rest_framework import viewsets
#Modelo
from ..models.articulos import Articulo
#Serializador
from ..serializers.articulos import ArticuloSerializer
#Permisos
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class ArticuloViewSet (viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [IsAuthenticated]
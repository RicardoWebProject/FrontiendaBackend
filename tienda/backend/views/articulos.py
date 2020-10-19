#Vistas
from rest_framework import viewsets
#Modelo
from ..models.articulos import Articulo
#Serializador
from ..serializers.articulos import ArticuloSerializer

class ArticuloViewSet (viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = []
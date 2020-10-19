#Vistas
from rest_framework import viewsets
#Modelo
from ..models.categorias import Categoria
#Serializador
from ..serializers.categorias import CategoriaSerializer
#Permisos
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class CategoriasViewSet (viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]
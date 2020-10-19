from django.urls import path, include
#Vistas de Categorías
from .views.categorias import CategoriasViewSet
#Vistas de Usuarios (no clientes)
from .views.usuarios import CrearUsuario, ListarUsuarios, ActualizarUsuario, EliminarUsuario, VerUsuario, LoginView
#Vistas de Articulos
from .views.articulos import ArticuloViewSet
#Vistas de Clientes y Fábricas
from .views.clienteProveedores import ClienteViewSet, FabricaViewSet
#Vistas de Direcciones
from .views.direcciones import DireccionesViewSet
#Router
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('categorias', CategoriasViewSet, basename='categorias')
router.register('articulos', ArticuloViewSet, basename='articulos')
router.register('clientes', ClienteViewSet, basename='clientes')
router.register('fabricas', FabricaViewSet, basename='fabricas')
router.register('direcciones', DireccionesViewSet, basename='direcciones')

urlpatterns = [
    #URLs desde router
    path('', include(router.urls)),
    #URL Login
    path('login/', LoginView.as_view(), name='login'),
    #URL de Usuarios
    path('usuarios/crear/', CrearUsuario.as_view(), name='crearUsuario'),
    path('usuarios/listar/', ListarUsuarios.as_view(), name='listarUsuarios'),
    path('usuarios/actualizar/<pk>', ActualizarUsuario.as_view(), name='actualizarUsuario'),
    path('usuarios/eliminar/<pk>', EliminarUsuario.as_view(), name='eliminarUsuario'),
    path('usuarios/ver/<pk>', VerUsuario.as_view(), name='verUsuario'),
]

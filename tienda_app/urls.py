from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'pedidos', views.PedidoViewSet)
router.register(r'detalles', views.DetallePedidoViewSet)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscar/', views.buscar, name='buscar'),
    path('api/', include(router.urls)),
]
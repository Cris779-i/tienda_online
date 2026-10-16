from django.shortcuts import render
from rest_framework import viewsets

from .models import Categoria, Producto, Cliente, Pedido, DetallePedido
from .serializers import (
    CategoriaSerializer,
    ProductoSerializer,
    ClienteSerializer,
    PedidoSerializer,
    DetallePedidoSerializer,
)

# Simulamos productos, no tenemos base de datos conectada
PRODUCTOS = {
    "notebook": "Notebook",
    "mouse": "Mouse",
    "teclado": "Teclado",
}


def inicio(request):
    return render(request, 'tienda_app/inicio.html')


def buscar(request):
    nombre = request.GET.get('nombre', '').lower().strip()
    producto = PRODUCTOS.get(nombre)

    if producto:
        return render(request, 'tienda_app/resultado.html', {'nombre': nombre, 'producto': producto})

    return render(request, 'tienda_app/no_encontrado.html', {'nombre': nombre}, status=404)


def pagina_no_encontrada(request, exception):
    return render(request, 'tienda_app/no_encontrado.html', {'nombre': request.path}, status=404)


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer
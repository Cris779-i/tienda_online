from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="productos"
    )

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("enviado", "Enviado"),
        ("entregado", "Entregado"),
        ("cancelado", "Cancelado"),
    ]
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="pedidos"
    )
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, related_name="detalles"
    )
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name="detalles"
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

from django.shortcuts import render

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
    else:
        return render(request, 'tienda_app/no_encontrado.html', {'nombre': nombre})
def pagina_no_encontrada(request, exception):
    return render(request, 'tienda_app/no_encontrado.html', {'nombre': request.path}, status=404)
    
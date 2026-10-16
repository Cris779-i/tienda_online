# API de Tienda Online

Proyecto de Backend con Django y Django REST Framework (Evaluación 2).
API REST para gestionar categorías, productos, clientes, pedidos y detalles de pedido.

## Requisitos

- Python 3.14
- MariaDB 10.11 o superior (se usó MariaDB 11.8 en el puerto 3307)

## Instalación

1. Crear y activar el ambiente virtual:

    python -m venv ambiente
    ambiente\Scripts\activate

2. Instalar dependencias:

    pip install -r requirements.txt

3. Crear la base de datos, el usuario y los permisos ejecutando el script:

    scripts_sql/crear_base_datos.sql

4. Revisar el archivo .env en la raíz del proyecto, con estas variables:

    SECRET_KEY=
    DB_NAME=tienda_online_db
    DB_USER=tienda_user
    DB_PASSWORD=
    DB_HOST=localhost
    DB_PORT=3307

5. Aplicar las migraciones:

    python manage.py migrate

6. Iniciar el servidor:

    python manage.py runserver

## Endpoints

Raíz de la API: http://127.0.0.1:8000/api/

- /api/categorias/
- /api/productos/
- /api/clientes/
- /api/pedidos/
- /api/detalles/

Cada endpoint permite GET, POST (en la lista) y GET, PUT, PATCH, DELETE
(en el detalle, por ejemplo /api/categorias/1/).

## Modelo de datos

- Categoria: nombre, descripcion
- Producto: nombre, descripcion, precio, stock, categoria
- Cliente: nombre, email, telefono
- Pedido: cliente, fecha, estado
- DetallePedido: pedido, producto, cantidad, precio_unitario

## Estructura

- core/: configuración del proyecto
- tienda_app/: app con models, serializers, views y urls
- scripts_sql/: scripts SQL de la base de datos
- requirements.txt: dependencias

## Autora

Cristal - Ingeniería en Informática, INACAP Temuco
-- Crear base de datos
CREATE DATABASE IF NOT EXISTS tienda_online_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Crear usuario
CREATE USER IF NOT EXISTS 'tienda_user'@'localhost' IDENTIFIED BY 'Tienda2026!';

-- Asignar permisos
GRANT ALL PRIVILEGES ON tienda_online_db.* TO 'tienda_user'@'localhost';

FLUSH PRIVILEGES;
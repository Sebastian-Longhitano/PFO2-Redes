# Sistema de Gestión de Tareas (API Flask + SQLite)

Este proyecto es un sistema básico de gestión de tareas implementado en Python utilizando Flask como framework de servidor y SQLite como base de datos. 

## 📁 Estructura del proyecto

tareas_api/
│
├── server.py # Servidor principal con Flask
├── bd.py # Módulo de conexión y creación de tablas SQLite
├── auth.py # Módulo de registro e inicio de sesión de usuarios
├── tareas.db # Base de datos SQLite (se crea automáticamente)
└── README.md # Instrucciones del proyecto


## 🚀 Cómo ejecutar el proyecto

1. Clona el repositorio o descargá los archivos.

2. Instalá las dependencias:

pip install flask werkzeug

3. Ejecutá el servidor:

python server.py

4. La API estará disponible en http://localhost:5000


## ¿Por qué hashear contraseñas?

Porque guardar contraseñas en texto plano representa un gran riesgo de seguridad. Si un atacante accede a la base de datos, podría ver todas las contraseñas directamente. Hashear (encriptar de forma unidireccional) las contraseñas permite que incluso si la base es comprometida, no se expongan los datos reales de los usuarios.


## Ventajas de usar SQLite

1. No requiere instalación ni configuración adicional, ideal para proyectos pequeños o individuales.

2. Guarda los datos en un único archivo .db, lo que facilita su portabilidad.

3. Totalmente compatible con Python mediante la librería estándar sqlite3.

4. Rápido y liviano, perfecto para prototipos o pruebas.
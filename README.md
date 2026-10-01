# Base del Sistema de Blog Web (Django)

Este repositorio contiene la estructura y configuración base para un sistema de blog web desarrollado en **Django**. El proyecto marca la transición de la lógica de consola a una arquitectura web escalable.

---

## 🛠️ Estructura del Proyecto

- **Proyecto principal (`blog_project`):** Contiene las configuraciones globales, ruteo de URLs e integración del proyecto.
- **Aplicación principal (`posts`):** Módulo encargado de gestionar las publicaciones, modelos y vistas del blog.
- **Configuración Regional:** Adaptado para español de Argentina (`es-ar`) y zona horaria `America/Argentina/Buenos_Aires`.

```text
.
├── blog_project/          # Configuración del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── posts/                 # App principal del blog
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── .gitignore             # Archivos y carpetas excluidos de Git
├── manage.py              # Script de gestión de Django
├── README.md              # Documentación del proyecto
└── requirements.txt       # Dependencias del proyecto
```


## 🚀 Guía de Instalación y Ejecución
Sigue estos pasos para clonar y ejecutar el proyecto en tu entorno local:

1. Clonar el repositorio
Bash
git clone [https://github.com/MarceloDiaz1375/python_entrega7.git](https://github.com/MarceloDiaz1375/python_entrega7.git)
cd python_entrega5
2. Crear y activar el entorno virtual
En Windows (PowerShell):

**PowerShell**
python -m venv venv
.\venv\Scripts\activate

En Linux / macOS:

**Bash**
python3 -m venv venv
source venv/bin/activate
3. Instalar las dependencias
Con el entorno virtual activo, instala las librerías necesarias mediante el archivo requirements.txt:

**Bash**
pip install -r requirements.txt
4. Levantar el servidor de desarrollo
Ejecuta el servidor local de Django:

**Bash**
python manage.py runserver
Abre tu navegador e ingresa a:
http://127.0.0.1:8000/

`Si ves la pantalla de bienvenida predeterminada de Django, el entorno y la estructura inicial se encuentran correctamente configurados.`

Para detener el servidor, presiona Ctrl + C en la terminal.

## 📋 Requisitos Técnicos
Python: 3.10+

Django: 6.0.1
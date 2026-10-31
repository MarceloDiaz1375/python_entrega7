# Base del Sistema de Blog Web (Django)

Este repositorio contiene un sistema de blog web desarrollado en **Django**, con gestión de publicaciones, formularios de contacto y carga de imágenes.

---

## 🛠️ Estructura del Proyecto

- **Proyecto principal (`blog_project`):** Contiene las configuraciones globales y el ruteo de URLs.
- **Aplicación (`posts`):** Gestiona las publicaciones, sus formularios, vistas y plantillas.
- **Aplicación (`cuentas`):** Gestiona el registro, el perfil de usuario y las funciones de autenticación.
- **Configuración regional:** Español de Argentina (`es-ar`) y zona horaria `America/Argentina/Buenos_Aires`.

```text
.
├── .gitignore
├── manage.py
├── README.md
├── requirements.txt
├── blog_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/
│   ├── avatares/ (avatares cargados; ignorado por Git)
│   └── posts/ (imágenes de publicaciones; ignorado por Git)
├── cuentas/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── templates/
│       ├── cuentas/
│       │   └── registro.html
│       └── registro/
│           ├── editar_perfil.html
│           ├── login.html
│           ├── password_change.html
│           ├── password_change_done.html
│           └── perfil.html
└── posts/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    ├── static/
    │   └── posts/
    │       └── css/
    │           └── estilos.css
    └── templates/
        └── posts/
            ├── acerca.html
            ├── base.html
            ├── contacto.html
            ├── detalle_post.html
            ├── inicio.html
            ├── lista_posts.html
            ├── post_confirm_delete.html
            └── post_form.html
```

Los archivos de medios se almacenan en `media/`: las imágenes de publicaciones en `media/posts/` y los avatares en `media/avatares/`. Estas carpetas contienen archivos subidos por los usuarios y están excluidas del control de versiones; pueden estar vacías al clonar el proyecto. También se omiten del esquema la base de datos local y el entorno virtual.

## 🖼️ Manejo de Imágenes

Cada publicación puede tener una imagen opcional. La implementación funciona así:

1. El modelo `Post` define el campo `imagen` como `ImageField`, opcional mediante `blank=True` y `null=True`. `upload_to='posts/'` guarda los archivos en una subcarpeta `posts/` dentro de `MEDIA_ROOT`.
2. `PostForm` incluye el campo de imagen. La plantilla del formulario usa `enctype="multipart/form-data"` para permitir el envío de archivos en las operaciones de creación y edición.
3. Las vistas de creación y edición inicializan el formulario con `request.POST` y `request.FILES`. Cuando el formulario es válido, `form.save()` persiste el registro y el archivo.
4. En el detalle de la publicación, la plantilla verifica que exista una imagen antes de mostrarla y obtiene su dirección desde `post.imagen.url`.

En `blog_project/settings.py`, `MEDIA_ROOT` apunta a `media/` en la raíz del proyecto y `MEDIA_URL` define la URL `/media/`. `blog_project/urls.py` sirve estos archivos durante el desarrollo solo cuando `DEBUG` está activado. En producción debe configurarse un servidor web o almacenamiento dedicado para los archivos multimedia.

La dependencia `Pillow`, requerida por Django para trabajar con `ImageField`, está incluida en `requirements.txt`.

## 🚀 Guía de Instalación y Ejecución

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. Clonar el repositorio:

```bash
git clone https://github.com/MarceloDiaz1375/python_entrega7.git
```

2. Crear y activar el entorno virtual.

En Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\activate
```

En Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Aplicar las migraciones:

```bash
python manage.py migrate
```

5. Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

Abre http://127.0.0.1:8000/ en el navegador. Desde el sitio puedes consultar publicaciones y acceder a los formularios para crear o editar posts, incluida la carga de imágenes.

Para detener el servidor, presiona `Ctrl + C` en la terminal.

## 📋 Requisitos Técnicos

- Python: 3.12+
- Django: 6.1.1
- Pillow: 13.0.0
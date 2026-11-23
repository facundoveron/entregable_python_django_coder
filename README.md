# Blog Django

Proyecto base de un blog web desarrollado con Django.

## Descripción

Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog.  
Incluye la configuración base del proyecto y una aplicación principal llamada `posts`.

---

## Tecnologías

- **Python 3.9+**
- **Django 4.2.30**
- **Bootstrap 5** (CDN) para el UI
- **SQLite** (base de datos predeterminada)
- **django‑crispy‑forms** (opcional) para estilos de formularios
- **python‑decouple** para la gestión de variables de entorno

## Funcionalidades principales

- Creación, edición y eliminación de posts con soporte de imágenes y resumen.
- Estado del post (borrador, publicado, archivado) y control de visibilidad.
- Sistema de usuarios con registro, login, perfil editable y avatar.
- Vista "Mis posts" para que cada autor administre sus artículos.
- Búsqueda de posts por título, contenido o resumen.
- Slug único automático con sufijo numérico.
- Mensajes de feedback con `django.contrib.messages`.
- Diseño responsivo y moderno usando Bootstrap 5 y CSS personalizado.
- Seguridad: el autor se asigna automáticamente, solo el autor puede editar/eliminar su post.

## Instalación y ejecución

Sigue los pasos a continuación para poner en marcha el proyecto en tu entorno local.

### 1. Clonar el repositorio
```bash
git clone https://github.com/facundoveron/entregable_python_django_coder.git
```

### 2. Entrar a la carpeta del proyecto
```bash
cd entregable_python_django_coder
```

### 3. Crear y activar un entorno virtual
```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
# .\\venv\\Scripts\\activate   # Windows PowerShell
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Configurar variables de entorno
Copia el archivo de ejemplo y adapta la clave secreta y demás valores:
```bash
cp .env.example .env
# Edita .env con tu propia SECRET_KEY (puedes generar una con python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
```

> **Nota:** No subas `db.sqlite3` ni la carpeta `media/`. Cada desarrollador debe crear su propia base de datos y carpeta de medios.

### 6. Ejecutar migraciones (crea la BD y los esquemas)
```bash
python manage.py migrate
```

### 7. (Opcional) Crear un super‑usuario para acceder al admin
```bash
python manage.py createsuperuser
```

### 8. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

Abre tu navegador en <http://127.0.0.1:8000/> y ya podrás usar el blog.

## Autor

**Facundo Verón** – Desarrollador full‑stack Python/Django. 

Puedes contactar a través de GitHub: [facundoveron](https://github.com/facundoveron).

---

### Nota importante sobre datos y media

- El proyecto **no incluye** el archivo `db.sqlite3` ni la carpeta `media/` en el repositorio.
- Para probar el proyecto desde cero, simplemente ejecuta `python manage.py migrate` (creará la base de datos vacía) y, si deseas subir imágenes, crea la carpeta `media/` en la raíz del proyecto (Django la generará automáticamente al subir archivos).
- Usa `python manage.py loaddata <fixture>` si dispones de fixtures de prueba.

## Aplicaciones del proyecto

- **`posts`**: aplicación principal encargada de manejar la lógica y administración de las publicaciones del blog.
- **`accounts`**: gestión de usuarios, registro, login, perfil y cambio de contraseña.

---


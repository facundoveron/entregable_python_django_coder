# Blog Django

Proyecto base de un blog web desarrollado con Django.

## Descripción

Este repositorio contiene la estructura inicial de un proyecto Django para construir un blog.  
Incluye la configuración base del proyecto y una aplicación principal llamada `posts`.

---

## Instalación y Ejecución

Sigue estos pasos para poner en marcha el proyecto en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Entrar a la carpeta del proyecto
```bash
cd entregable_python_django_coder
```

### 3. Crear el entorno virtual
```bash
python -m venv venv
```

### 4. Activar el entorno virtual

- **En Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

- **En Windows (CMD):**
  ```cmd
  .\venv\Scripts\activate.bat
  ```

- **En Linux o macOS:**
  ```bash
  source venv/bin/activate
  ```

### 5. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 6. Ejecutar migraciones (opcional / inicial)
```bash
python manage.py migrate
```

### 7. Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```

### 8. Abrir en el navegador
Ingresa a la siguiente dirección en tu navegador:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Aplicaciones del Proyecto

- **`posts`**: Aplicación principal encargada de manejar la lógica y administración de las publicaciones del blog.

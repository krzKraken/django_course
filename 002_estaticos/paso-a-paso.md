# **Estaticos**

## **1. Crear la carpeta static/ en la raiz del proyecto**

En esta carpeta van a ir todos los archivos estaticos CSS, Javascript e imagenes que ocupa nuestro proyecto

## **2. crear la variable de entorno..**

STATICFILES_DIRS = [
BASE_DIR / "static",
"/var/www/static" # <- Preparado para deploy
]

## **3. las importaciones se realizan de la siguiente manera**

`href="{% static 'style.css' %}"`
se debe considerar que el origen de estos archivos esta definido por la variable de entorno

`STATIC_URL = "static/"` en settings.py

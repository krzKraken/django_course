# CONEXION A BASE DE DATOS

django recomienda utilizar como motor de base de datos a postgreSQL, no significa que no podemos utilizar cualquier otra base de datos pero es la recomendacion del desarrollador.

## Instalacion

1.- Debemos instalar el pgadmin 4 y postgres.app en nuestra mac/pc
2.- Una vez instalado debemos correr el servidor en postgres.app y abrir la base de datos desde pgadmin.
3.- Debemos crear una base de datos por cada proyecto antes de condifugarla en nuestr proyecto
4.- Segumos la documentacion y tenemos que pegar el codigo en el archivo settings.py del proyecto la configuracion

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<NOMBRE_DATABASE>',
        'USER': '<MY_DATABASE_USER>',
        'PASSWORD': '<DB_PASSWORD>',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

### variables de entorno

Para evitar colocar la contrasena podemos utilizar el paquete de python-dotenv que es para guardar variables de entorno .env en nuestro proyecto

#### Instalacion

> pip install python-dotenv

#### .env file

DB_PASSWORD=NUESTRA_CONTRASENA
DB_USER=MY_USER
DB_NAME=MY_DATABASE_NAME

#### Uso de variable de entorno

import os
from dotenv import load_dotenv
load_dotenv()

password=**os.getenv('DB_PASSWORD')**

## Para acabar

Para terminar migramos los modelos o cambios en las bases de datos con

> python3 manage.py migrate

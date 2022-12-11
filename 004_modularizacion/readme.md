# Gestión de Bases de datos

Las bases de datos en django no requieren ser manejo directo con lenguaje de base de datos, basta con crear una clase en los models.py de la siguiente manera

```
# Create your models here.
class comments(models.Model):
    name = models.CharField(max_length=150, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)
    signature = models.CharField(max_length=100, default="hello")

    def __str__(self):
        return self.name

```

De esta forma podemos crear facilmente las tablas y sus columnas de valores definiendolas facilmente.

### 1.- Creamos la base de datos con la clase

### 2.- Debemos tener la aplicacion agregada al proyecto agregandola al array de apliucaciones en setings.py del proyecto

### 3.- Posteriormente podemos hacer un makemigrations para que se reconozcan los cambios que se han realizado

`python manage.py makemigrations`

### 4.- Finalmente podemos ejecutar un migrate para que se actualicen las modificaciones en las bases de datos

`python manage.py migrate`

# Modularización

Podemos crear un proyecto con varias aplicaciones y poder reutilizar las aplicaciones creadas en diferentes proyectos si realizamos las practicas correctas en la creacion y estructuracion de la aplicación.

### 1.- Debemos saber que para poder comunicar una app con un proyecto nos podemos facilmente equivocar y en la urls.py del proyecto agregar las rutas de la aplicacion, que sería una mala práctica.

Lo que se debe hacer es que se debe crear un urls.py en la dirección de la aplicación y se va a manejar como que si fuera la misma aplicación el proyecto.

### 2.- Para agregar la ruta o conexion con nuestro proyecto a las aplicaciones, la manera correcta es la siguiente

- Creamos un archivo urls.py en la app
- Agregamos el path que se va a utilizar en la aplicación

```
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path("test/", views.test, name="test"),
]

```

- En el archivo urls.py del proyecto agregamos la ruta mediante el metodo include que importamos en django.urls -> include

```
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
  path("admin/", admin.site.urls),
  path("comentarios/", include("comentarios.urls")),
]
```

En este caso nuestra aplicacion es comentarios y se incluyen todas las urls que se encuentren en urls.py

** Importante: para acceder a esa ruta, en el navegador debemos incluir en la ruta "comentarios/" previa a la ruta que creamos es decir... **

> HOST_NAME/comentarios/test/

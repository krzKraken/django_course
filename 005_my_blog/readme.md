# SEEDING Y PAQUETES

## Poblado de base de datos para consultas a la base de datos

Para la prueba de modelos y bases de datos no es aconsejable realizar manualmente la creación y eliminación de los datos de las bases de datos, para eso creamos un fadeinFactory que lo que nos permita es introducir datos de prueba en una base de datos para poder crear datos en la base de datos de una forma mas agil.

# Apicación Fade en django -> PAQUETE

El paquete se llama django-seed

- https://pypi.org/project/django-seed/
  en este URL podemos ver la forma de instalarlo

## Instalación

para la instalación lo instalamos en nuestro proyecto desde la linea de comandos con

> pip install django-seed
> pip install psycopg2-binary (Esto es requerido, da error)

en la configuración debemos agragar "django-seed" en la lista de aplicaciones intaladas

```
INSTALLED_APPS = (
...
'django_seed',
)
```

## Utilización

Para utilizar el paquete seed debemos utilizarlo de la siguiente manera.

> python manage.py seed <nombre_app( donde se encuentran los modelos )> --number=<numero_de_elementos>

# CONSULTAS

### Todas las consultas se van a crear en el controlador (views), Ejemplo:

views.py

```
from django.shortcuts import render
from .models import Author, Entry

def queries(request):
    # Obtener todos los elementos (Autores/ entradas/ lo que sea/)
    autores = Author.objects.all()

    return render(request, "post/queries.html", {"authors": autores})

```

El pintado de la pagina -> template/post/queries.html

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Post</title>
</head>
<body>
  <h3> Consulta a todos los autores </h3>
  <ul>
    {% for author in authors %}
   <li>{{author.name}} ( {{author.email}} )</li>
    {% endfor%}
  </ul>
</body>
</html>
```

## Consultas .Todos

```
def queries(request):
    # Obtener todos los elementos
    results = ModelName.objects.all()
_
    return render(request, "<template_path>", {"context_name": results})
```

## Consultas .filter

```
def queries(request):
    # Obtener elementos con filter
    resultsFiltered = ModelName.objects.filter(<id, name, etc> = "<value>")
_
    return render(request, "<template_path>", {"context_name": resultsFiltered})
```

## Consultas .unico Respultado

```
def queries(request):
    # Obtener un unico elemento
    resultsFiltered = ModelName.objects.get(<id, name, etc> = "<value>")
_
    return render(request, "<template_path>", {"context_name": resultsFiltered})
```

## Consultas .limits

```
def queries(request):
    # Obtener los primeros 10 elementos
    resultsFiltered = ModelName.objects.all()[:10]
_
    return render(request, "<template_path>", {"context_name": resultsFiltered})
```

## Consultas .offsets

```
def queries(request):
    # Obtener 5 elementos del 5 al 10 elementos
    resultsFiltered = ModelName.objects.all()[5:10]
_
    return render(request, "<template_path>", {"context_name": resultsFiltered})
```

# Consultas ordenadas

Se pueden realizar consultas mas complejas como que un valor sea mayor o menor, contenga o sea exacto

```
def queries(request):
    # Obtener los elementos que el valor es menor a 15
    # Se agrega al poarametro __lte (lower than equal),__gte (greater than equal), __lt (lower than), __gt (greater than), __contains, __exact
    resultsFiltered = ModelName.objects.filter(<variable__lte> = 15)
_
    return render(request, "<template_path>", {"context_name": resultsFiltered})
```

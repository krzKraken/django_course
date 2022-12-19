# Formularios de clase

https://docs.djangoproject.com/en/4.1/ref/forms/fields/

Para los formularios de clase se debe crear un fichero form.py en el cual vamos a estar definiendo las clases de los elementos que contendra nuestro formulario.

Podemos crear un formulario a travez de los modulos de form de django.

un ejemplo de formulario es:

## Formulario de django - form.py

```
from django import forms

# Se declaran similar a la forma de declarar los modelos
class CommentForm(forms.Form):
    name = forms.CharField(
        label="Escribe tu nombre", max_length=100, help_text="100 caracteres maximo"
    )
    url = forms.URLField(label="tu sitio web", required=False, initial="http://")
    comment = forms.CharField()
```

## Lectura de formulario - GET

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Formularios djando</title>
</head>
<body>
  <h1>Formularios django - Metodo GET</h1>
  <hr>
  <form action="{% url 'getgoal' %}" method="GET">
    {{ comment_form.as_p }}
    <input type="submit" value="Enviar">
  </form>
</body>
</html>
```

## Rutas formulario

```
urlpatterns = [
    path("admin/", admin.site.urls),
    path("getform/", views.getform, name="getform"),
    path("getgoal/", views.getgoal, name="getgoal"),
    path("postform/", views.postform, name="postform"),
    path("postgoal/", views.postgoal, name="postgoal"),
]
```

## Views/controlador

```
from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm


def getform(request):
    # Podemos dar valores iniciales por defecto
    comment_form = CommentForm(
        {
            "name": "ValorPorDefecto",
            "url": "http://urlPorDefecto",
            "comment": "comentarioPordefecto",
        }
    )
    return render(request, "get_form.html", {"comment_form": comment_form})


def getgoal(request):
    if request.method != "GET":
        return HttpResponse("Metodo no permitido")
    return HttpResponse(request.GET["name"])


def postform(request):
    comment_form = CommentForm(
        {
            "name": "ValorPorDefecto",
            "url": "http://urlPorDefecto",
            "comment": "comentarioPordefecto.com",
        }
    )
    return render(request, "post_form.html", {"comment_form": comment_form})


def postgoal(request):
    if request.method != "POST":
        return HttpResponse("Metodo no permitido")
    return HttpResponse(request.POST["name"])

```

## Lectura de formulario - POST

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Formularios djando</title>
</head>
<body>
  <h1>Formularios django - Metodo POST</h1>
  <hr>
  <form action="{% url 'postgoal' %}" method="POST">
    {% csrf_token %}
    {{ comment_form.as_p }}
    <input type="submit" value="Enviar">
  </form>
</body>
</html>
```

# Formularios con estilos

Preparamos el formulario

```
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label=" Nombre", max_length=50)
    email = forms.EmailField(label="Email", max_length=50)
    message = forms.TextInput(label="Mensaje")
```

Para poder colocar una **clase** especifica a un campo podemos agregar el campo widget al forms.XXXX
por ejemplo

```
campo_texto = forms.CharField(
        label="Campo de texto",
        widget=forms.TextInput(
            attrs={"class": "clase_nueva"},
        ),
    )
```

de esta forma en el html podemos importar un estilo CSS o de algun framework de nuestra eleccion

ahora si en nuestro html hacemos una imortacion de algin framework o de algun archivo de estilos podemos asociarlos a esta clase y tendriamos como resultado la personalizacion de nuestro html

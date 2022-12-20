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

# Validaciones

Dos tipos de validaciones...
1.- Validaciones generales: Aquellas explicitadas en el formato del dato que esta llenando el usaurio en el formulario
Ejemplo:
en el formulario se registra un nombre entonces es un charFeld -> que tiene varias condiciones como un maximo de longitud en sus caracteres, que no puede estar vacio ni nulo, etc

#### Validaciones de metodos por defecto

Para los metodos preestablecidos por django cuando se coloca "Max_length = 50" por ejemplo se debe utilizar el metodo **is_valid**, estas validaciones son comunes y se realizan con

```
def widget(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, "widget.html", {"form": form})

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # TODO:todas las acciones que se realiazan cuando sea valido
            return HttpResponse("Valido")
        else:
            # TODO: Todas las acciones que sean necearias cuando no sea valida

            return HttpResponse("No es valido")

```

En este caso, si alguien desde el navegador intenta modificar las restricciones puestas desde las validaciones en el controlador y las envia, al momento de colocar el metodo is valid django hace la valicion desde el servidor usando el metodo is_valid() para verificar que los datos que ingresan por el form sean correctos.

2.- Validaciones personalizadas. Cuando las validaciones no son las que tiene django por defecto.
Para situaciones cuando requerimos hacer validaciones que no estan contempladas en django. Para esto hacemos uso de funcones clean

en este ejemplo dentro de la clase que vamos a realizar la validacion podemos crear un metodo clean\_<nombreValidador> y en ella colocar todas la validaciones extras que se requieren, en este caso vamos a poner como restricción que solo se puede colocar la palabra "palabra" como nombre. caso contraro saltaría un error.

```
class contactForm(form.Form):
    name = forms.CharField(label="whrite your name", max_length=10, help_text="10 caracteres max")

    def clean_name(self):
        # Guardamos en name las validaciones por defecto
        name = self.cleaned_data.get("name")
        if name != "palabra":
            # Error
            raise forms.ValidationError("Solo se permite el valor palabra para este campo")
        else:
            # Exito
            return name
```

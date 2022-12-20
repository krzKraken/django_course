# Model Forms

Se pueden generar formularios en base a los modelos de datos que tengamos, es decir si tenemos creado un modelo de datos empleados, lo mejor para seguir las buenas practicas es no repetir el código o duplicar información. En el siguiente Ejemplo crearemos un modelo de empleados. y crearemos un model form del mismo con el fin de reutilizar la contruccion del modelo para la creacion del formulario.

El formulario tiene como objetivo en general de crear un elemento, modificarlo, eliminarlo... cuando creamos un formulario o un modelo nos damos cuenta que tienen una forma peluliarmente similar, es por ello que se implementa el model form

## Pasos para crear un Model Form con validacion y estilos.

### 1.- Debemos crear el form.py en nuestra aplicacion

Para este ejemplo vamos a crear un formulario al modelo Employee que tiene como campos [name, last_name, email]

**form.py**

```
# Importamos la clase de model form
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee
from django import forms

# Con esto django ya sabe que vamos a introducir datos para un modelo de datos
# !El model form tiene que tener el nombre del modelo+Form <EmployeeFoor>
class EmployeeForm(ModelForm):
    # Indicamos que este formulario tenga los datos del modelo
    class Meta:
        model = Employee
        fields = ["name", "last_name", "email"]
        # podemos decirle rapidamente que queremos todos los campos haciendo uso del "__all__"
        # fields = '__all__'
        # Podemos realizar la exclusion

        exclude = ("email",)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name != "kraken":
            raise forms.ValidationError("Solo se permite el nombre kraken")
        else:
            return name

    # Creamos los wodgets con las clases que vamos a utilizar, ya sean de algun framework o una clase personalizada
    name = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
```

En el archivo form.py vamos a crear el ModelForm que no es mas que un modelo de datos que le dice a django que vamos a crear un formulario de tipo del modelo de datos.

### 2.- El Controlador (views.py)

**views.py**

En el views.py creamos el controlador que va a tener como contexto al ModelForm que creamos (EmployeeForm) y nos va a dirigir al .html que se va a renderizar con el formulario.
Aqui tambien agregamos la validacion del servidor o si necesitamos una validacion personalizada

```
from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm

# Create your views here.
def index(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request, "index.html", {"form": form})
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            return HttpResponse("Valido")
        else:
            return render(request, "index.html", {"form": form})

```

### 3.- El html

En el Html podemos importar algun archivo estatico CSS o podemos de igual manera utilizar un framework de nuestra preferencia

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
  <title>Model Form</title>
</head>
<body>
  <h3>Model Form</h3>
  <hr>
  <form action="{% url 'index' %}" method="POST">
    {% csrf_token %}
    <table>
      {{form.as_table}}
    </table>
    <input type="submit" value="Crear" class="btn btn-success">
  </form>
</body>
</html>
```

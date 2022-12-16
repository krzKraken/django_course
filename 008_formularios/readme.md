# Formularios

Se pueden crear dos tipos de formularios, uno es un **formulario html** y el otro es un **formulario por modelos**, ambos son correctos y ambos se pueden encontrar en producción.
el formulario por modelos de django es mejor utilizarlo porque nos permite mantener un orden mas estricto.

## Componentes de un formulario

> Un formulario consta de un action, que cuando le demos al boton de enviado es el responsable de ejecutar una accion
> Un formulario tendra un vervo que es el metodo con el cual vamos a enviar la peticion
> **GET** -> No enviamos información sensible porque se va a ver en la ruta -> no enviar contraseñas
> **POST** -> Envio de informacion segura, para enviar la informacion codificada o cualquier informacion sensible
> **DELETE** -> Eliminación de datos

### Creacion de una ruta GET

En nuestras rutas del urls.py podemos agregar las duras que tendran el method = 'GET' en el formulario.

```
    path("get/form/", views.getform, name="form"),
    path("get/goal/", views.getgoal, name="goal"),
```

en el formulario que se haya creado debemos colocar los dos componentes requeridos, el action= '<ruta/destino>' y el method = '<metodo>'

```
<form action="{% url 'goal'  %}" method="GET">
  <h3>Formulario de contacto</h3>
  <label> Nombre: </label>
  <input type="text" name="name" placeholder="Escribe tu nombre...">
  <label for="">Comentaio</label>
  <input type="text" name="message" placeholder="Escribe tu comentario...">
  <input type="submit" value="Enviar">
</form>
```

Como podemos ver tenemos el action a la ruta enviada **"{% url 'goal %}"**
y tenemos el **method='GET'**

al realizar una peticion GET tenemos que tener en cuenta que los valores enviados van a ser leidos en la url, por eso no podemos utilizarlos para enviar valores que sean sensibles

Para leer o utilizar los valores enviados podemos realizar la condicion y lectura de la siguiente manera:

```
def getgoal(request):
    # En el Methodo GET
    if request.method != "GET":
        return HttpResponse("El Método POST no esta soportado en esta ruta")

    name = request.GET["name"]
    message = request.GET["message"]

    return render(request, "success.html", {"name": name, "message": message})
```

### Creaciond de una ruta POST

Creamos las rutas del metodo post

```
    path("post/form/", views.postform, name="postform"),
    path("post/goal/", views.postgoal, name="postgoal"),
```

en el formulario especificamos que recibiremos un method = 'POST' y de igual manera el actions que nos va a redirigir al siguiente URL

```
<h1>Formulario post</h1>
<form action="{% url 'postgoal'  %}" method="POST">
  {% csrf_token %}
  <input type="text" name="info" placeholder="Escriba algo...">
  <input type="submit" value="Enviar">

</form>

```

Para leer los valores del metodo post o de la peticion POST podemos utiliazr lo siguiente

```
def postgoal(request):
    if request.method != "POST":
        return HttpResponse("El metodo GET no esta soportado para esta ruta")
    info = request.POST["info"]

    return render(request, "postsuccess.html", {"info": info})

```

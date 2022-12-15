# Relaciones entre tablas

url: https://docs.djangoproject.com/en/4.1/topics/db/examples/

La relación entre tablas puede ser uno a uno, uno a varios o varios a varios.

## Relaciones 1 a 1

para una relacion 1 a 1 tenemos que crear un modelo que tenga como clave una relacio 1 a 1

### modelo 1 a 1

```
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    number_off_employees = models.IntegerField(default=1)

    def __str__(self):
        return self.place.name

```

aqui podemos ver como se relaciona un restaurant a una direccion unica, mediante el models.OneField()

### vista/controlador -> Crear el objeto

Para crear el objeto podemos en nuestro controlador (views.py) crear el metodo..

```
def create(request):
  place = Place(name = "<valor>", address = "<valor>")
  place.save()

  restaurant = Restaurant(place = place,number_off_employees = <valor> )
  restaurant.save()

  return HttpResponse(restaurant.place.name) # Podemos acceder a la relacion directamente a travez del objeto restaurant
```

## Relacion 1 a muchos o muchos a 1

Las relaciones muchos a uno o uno a muchos se realizan mediante el foreignkey, se debe **considerar que el foreignkey debe estar en el modelo que se pueda relacionar con un solo elemento** es decir, si un reportero puede tener varios articulos, y los articulos solo pueden tener un unico Reportero entonces el foreignKey debe colocarse en el Articulo.

### modelo 1 a muchos o muchos a 1

```
from django.db import models

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.email


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

```

### Vista/controlador -> Crear objetos y lectura de articulo1 a reportero

Lectura muchos a 1

```
from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.
def manytoone(request):
   # Como el Articulo es quien contiene un solo reportero, se empieza creandolo primero al reportero
   rep = Reporter(
       first_name="kraken", last_name="Insane", email="krakeninsane@demo.com"
   )
   rep.save()

   art1 = Article(
       headline="loream ipsum dotot", pub_date=date(2022, 5, 5), reporter=rep
   )
   art1.save()
   art2 = Article(
       headline="Lortas manus dotert", pub_date=date(2020, 1, 6), reporter=rep
   )
   art2.save()
   art3 = Article(
       headline="Cricox portus mancus", pub_date=date(2012, 6, 7), reporter=rep
   )
   art3.save()
   result = art1.reporter.first_name

   return HttpResponse(result)

```

Lectura 1 a muchos

```
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date

# Create your views here.
def manytoone(request):
    # Como el Articulo es quien contiene un solo reportero, se empieza creandolo primero al reportero
    rep = Reporter(
        first_name="kraken", last_name="Insane", email="krakeninsane@demo.com"
    )
    rep.save()

    art1 = Article(
        headline="1loream ipsum dotot", pub_date=date(2022, 5, 5), reporter=rep
    )
    art1.save()
    art2 = Article(
        headline="2Lortas manus dotert", pub_date=date(2020, 1, 6), reporter=rep
    )
    art2.save()
    art3 = Article(
        headline="3Cricox portus mancus", pub_date=date(2012, 6, 7), reporter=rep
    )
    art3.save()

    # lectura 1 a muchos
    # Cuando se va en direccion de 1 a varios, se debe colocar <nombreModelo>_set y de ahi en adelante se convierte en una consulta .all() .filter() etc.
    result = rep.article_set.all()
    return HttpResponse(result)

```

## Relacion Muchos a muchos

Para hacer una relacion de varios a varios o muchos a muchos basta con crear la relacion entre una clase en modelo models.ManyToMany(<clase_a_relacionar>)

```
from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    # para una relacion varios a varios solo se debe realacionar en una de las dos clases
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline
```

No requiere un metodo de borrado porque se crea una tabla independiente donde se genera la relacion entre un tabla y otra

### Manipulacion de muchos a muchos

Para poder realizar la relacion de varios a varios se necesita tenerlos creados por lo que vamos a tener un controlador de creacion de elementos createArticles()

```
from django.http import HttpResponse
from .models import Article, Publication

# Para una relacion muchos a muchos primero se deben crear los elementos antes de hacer la relacion
def createArticles(request):
    art1 = Article(headline="Articulo primero")
    art1.save()
    art2 = Article(headline="Articulo segundo")
    art2.save()
    art3 = Article(headline="Articulo tercero")
    art3.save()

    pub1 = Publication(title="publicacion 1")
    pub1.save()
    pub2 = Publication(title="publicacion 2")
    pub2.save()
    pub3 = Publication(title="publicacion 3")
    pub3.save()
    pub4 = Publication(title="publicacion 4")
    pub4.save()
    pub5 = Publication(title="publicacion 5")
    pub5.save()
    pub6 = Publication(title="publicacion 6")
    pub6.save()
    pub7 = Publication(title="publicacion 7")
    pub7.save()
    pub8 = Publication(title="publicacion 8")
    pub8.save()
    # Cuando en el modelo se tiene la relacion ManyToMany
    # AGREGAR UNA RELACION
    art1.publications.add(pub1)
    art1.publications.add(pub2)
    art1.publications.add(pub3)

    art2.publications.add(pub4)
    art2.publications.add(pub5)
    art2.publications.add(pub6)

    art3.publications.add(pub6)
    art3.publications.add(pub7)
    art3.publications.add(pub8)

    return HttpResponse("Relaciones Creadas")
```

Para leer las relaciones creadas si el elemento tiene en su modelo la relacion ManyToMany podemos llamarle directamente mediante **art1.publications.all().filter().etc**

```

def getArticleRelations(request):
    # En este caso el modelo de Article tiene la relacion ManyToMany llamada publications y podemos llamarla directamente
    art1 = Article.objects.get(id=2)
    result = art1.publications.all()
    return HttpResponse(result)
```

Para poder leer las relaciones desde el modelo que no tiene la relacion ManyToMany debemos realizar la busqueda como que se tratara de una relacion de uno a varios, buscando con el metodo get(id, name, etc) y luego utilizar el <modelNameLowerCase>\_set.all().filter().etc

```
def getPublicationsRelations(request):
    # En el caso de no tener en el modelo la relacion ManyToMany podemos hacer como cuando se trata de una relacion de uno a muchos, utilizando el <nombreDelModeloEnMinuscula>_set.all().filter()
    pub6 = Publication.objects.get(id=6)
    result = pub6.article_set.all()
    return HttpResponse(result)

```

Para eliminar las relaciones, podemos hacerlas de la siguiente manera, identificamos los dos objetos que queremos desvincular y simplemente mediante el metodo remove()

```

def removeRelations(request):
    # Eliminar la relacion de articulo# con publicacion#
    art1 = Article.objects.get(id=1)
    pub2 = Publication.objects.get(id=2)
    art1.publications.remove(pub2)
    return HttpResponse("Eliminado relacion de " + art1.headline + " - " + pub2.title)

```

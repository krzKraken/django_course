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


def getArticleRelations(request):
    # En este caso el modelo de Article tiene la relacion ManyToMany llamada publications y podemos llamarla directamente
    art1 = Article.objects.get(id=2)
    result = art1.publications.all()
    return HttpResponse(result)


def getPublicationsRelations(request):
    # En el caso de no tener en el modelo la relacion ManyToMany podemos hacer como cuando se trata de una relacion de uno a muchos, utilizando el <nombreDelModeloEnMinuscula>_set.all().filter()
    pub6 = Publication.objects.get(id=6)
    result = pub6.article_set.all()
    return HttpResponse(result)


def removeRelations(request):
    # Eliminar la relacion de articulo# con publicacion#
    art1 = Article.objects.get(id=1)
    pub2 = Publication.objects.get(id=2)
    art1.publications.remove(pub2)
    return HttpResponse("Eliminado relacion de %s - %s " % art1.headline % pub2.title)

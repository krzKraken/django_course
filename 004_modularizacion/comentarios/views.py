from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment

# Create your views here.
def test(request):
    return HttpResponse("<h1>hola mundo</h1>")


def create(request):
    # De esta forma podemos crear un objeto que se guarda con el metodo save
    # comment = Comment(name="Kraken", score=5, comment="Este es un comentario")
    # comment.save()
    # Otra forma de crear y guardar es mediante la siguiente linea de codigo, aqui simplemente con .objects.create(parametros) guarda automaticamente
    comment = Comment.objects.create(name="Juajua")
    return HttpResponse("Ruta para probar la creacion de models")


def delete(request):
    # Primera forma de eliminar por id
    # comment = Comment.objects.get(id=1)
    # comment.delete()

    # Segunda forma de eliminar con filter
    Comment.objects.filter(id=2).delete()
    return HttpResponse("Ruta poara probar los borrados")

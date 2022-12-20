from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm, ContactForm


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


def widget(request):
    if request.method == "GET":
        form = ContactForm()
        return render(request, "widget.html", {"form": form})

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # TODO:todas las acciones que se realiazan cuando sea valido, crear valor en base de datos, actualizar datos, etc
            return HttpResponse("Valido")
        else:
            # TODO: Todas las acciones que sean necesarias en caso de no ser validos los valores, en este caso se muetran los errores en los formularios
            return render(request, "widget.html", {"form": form})

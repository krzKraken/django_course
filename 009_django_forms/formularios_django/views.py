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
    form = ContactForm()
    return render(request, "widget.html", {"form": form})

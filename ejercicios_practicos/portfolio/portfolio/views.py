from django.shortcuts import render


def inicio(request):
    return render(request, "inicio.html", {})


def portfolio(request):
    return render(request, "portfolio.html", {})


def home(request):
    return render(request, "home.html", {})

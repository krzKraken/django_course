from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola mundo")


def despedida(request):
    return HttpResponse("Hasta luedo")


# Parametro en URL
def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Mayor de edad")
    else:
        return HttpResponse("Menor de edad")

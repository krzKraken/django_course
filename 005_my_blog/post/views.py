from django.shortcuts import render
from .models import Author, Entry

# Create your views here.
def queries(request):
    # Obtener todos los elementos (Autores/ entradas/ lo que sea/)
    autores = Author.objects.all()

    # Obtener datos filtrados por condicion
    filteded = Author.objects.filter(email="frobertson@example.org")

    # Obtener un unico resultado (unico objeto)
    author = Author.objects.get(id=3)

    # Obtencion de los 10 primeros elementos con limits
    limits = Author.objects.all()[:10]

    # Obtener 10 elementos saltando los 5 primeros
    offsets = Author.objects.all()[5:10]

    # Ordenamiento de consulta por email
    orders = Author.objects.all().order_by("email")

    # Obtener elementos filtradas por condicion

    filteredConditions = Author.objects.filter(id__lte=15)
    return render(
        request,
        "post/queries.html",
        {
            "authors": autores,
            "filtered": filteded,
            "author": author,
            "limits": limits,
            "offsets": offsets,
            "orders": orders,
        },
    )

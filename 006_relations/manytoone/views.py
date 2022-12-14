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
    # Articulo a reportero
    # result = art1.reporter.first_name
    # Reportero a articulo
    # Cuando se va en direccion de 1 a varios, se debe colocar <nombreModelo>_set y de ahi en adelante se convierte en una consulta .all() .filter() etc.
    result = rep.article_set.all()
    # result = rep.article_set.count()
    return HttpResponse(result)

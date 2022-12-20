from django.shortcuts import render
from django.http import HttpResponse
from .forms import EmployeeForm

# Create your views here.
def index(request):
    if request.method == "GET":
        form = EmployeeForm()
        return render(request, "index.html", {"form": form})
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            return HttpResponse("Valido")
        else:
            return render(request, "index.html", {"form": form})

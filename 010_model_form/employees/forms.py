# Importamos la clase de model form
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee
from django import forms

# Con esto django ya sabe que vamos a introducir datos para un modelo de datos
# !El model form tiene que tener el nombre del modelo+Form <EmployeeFoor>
class EmployeeForm(ModelForm):
    # Indicamos que este formulario tenga los datos del modelo
    class Meta:
        model = Employee
        fields = ["name", "last_name", "email"]
        # podemos decirle rapidamente que queremos todos los campos haciendo uso del "__all__"
        # fields = '__all__'
        # Podemos realizar la exclusion

        exclude = ("email",)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name != "kraken":
            raise forms.ValidationError("Solo se permite el nombre kraken")
        else:
            return name

    # Creamos los wodgets con las clases que vamos a utilizar, ya sean de algun framework o una clase personalizada
    name = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

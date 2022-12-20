# Importamos la clase de model form
from django.forms import ModelForm
from .models import Employee

# Con esto django ya sabe que vamos a introducir datos para un modelo de datos
# !El model form tiene que tener el nombre del modelo+Form <EmployeeFoor>
class EmployeeForm(ModelForm):
    # Indicamos que este formulario tenga los datos del modelo
    class Meta:
        model = Employee
        fields = ["name", "last_name", "email"]

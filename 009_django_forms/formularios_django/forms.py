from django import forms

# Se declaran similar a la forma de declarar los modelos\
# Formulario normal con html
class CommentForm(forms.Form):
    name = forms.CharField(
        label="Escribe tu nombre", max_length=100, help_text="100 caracteres maximo"
    )
    url = forms.URLField(label="tu sitio web", required=False, initial="http://")
    comment = forms.CharField()


# Formulario con modelos de django
class ContactForm(forms.Form):
    name = forms.CharField(
        label=" Nombre",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            },  # <-- clase "Form-control" (del framework botstrap)
        ),
    )
    email = forms.EmailField(
        label="Email",
        max_length=50,
        widget=forms.EmailInput(
            attrs={"class": "form-control"},
        ),
    )
    message = (
        forms.CharField(
            label="Mensaje",
            widget=forms.Textarea(
                attrs={"class": "form-control"},
            ),
        ),
    )
    campo_texto = forms.CharField(
        label="Campo de texto",
        widget=forms.TextInput(
            attrs={
                "class": "clase_nueva"
            },  # <-- Clase "clase_nueva" es una clase personalizada
        ),
    )

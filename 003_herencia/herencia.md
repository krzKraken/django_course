# Herencia

### Se puede reutilizar el código mediante la creacion de una plantilla o un template base donde se pueda modificar parte del contenido sin alterar el resto del template

### 1. Se crea un template base de donde heredará o extenderá las otras paginas

### 2. En cada seccion o bloque donde se desea incluir el contenido diferente se debe colocar

```
{% block nombreBloque %}
  (Esto queda vacio en el template base)
{% endblock %}

```

### 3. En el archivo o template que va a heredar debemos especificar que extiende del template base

```
{# especifica de quiene extiende #}
{% extends './ubicacion/templateBase.html' %}

{# En el bloque llamado <blockName1> #}
{% block <blockName> %} <valor que queremos colocar> {% endblock %}

{# Los bloques pueden tomar valores o quedar vacios #}

{% block <blockName2> %}

{%endblock%}
```

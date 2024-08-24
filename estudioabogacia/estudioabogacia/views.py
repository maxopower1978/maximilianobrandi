from django.http import HttpResponse
from django.template import Template, Context


def saludo(request):

    return HttpResponse("Hola Django - Coder")


def segunda_vista(request):

    return HttpResponse("<h1>Segunda vista</h1>")


def nombre(request, nombre: str, apellido: str, edad: int):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    edad = edad
    return HttpResponse(f"{apellido}, {nombre} tienes {edad} años")


def probando_template(request):
    mi_html = open("./templates/estudioabogacia/template1.html", encoding="utf-8")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)


def tirar_dados(request):
    from random import randint

    resultado = randint(1, 6)
    if resultado == 6:
        return HttpResponse(f"<h1>{resultado} Ganaste! 😎</h1>")
    else:
        return HttpResponse(f"<h1>{resultado} perdiste 😥 vuelve a tirar</h1>")


def fecha_hoy(request):
    from datetime import datetime

    fecha_hoy = datetime.now()
    fecha_formateada = fecha_hoy.strftime("%d/%m/%Y %H:%M:%S.%f")
    return HttpResponse(f"<h1>La fecha y hora actual es {fecha_formateada}</h1>")

# from django.http import HttpResponse
# from django.template import Template, Context es remmplazado por la línea que sigue
from django.shortcuts import render


# def saludo(request):

#     return HttpResponse("Hola Django - Coder")


# def segunda_vista(request):

#     return HttpResponse("<h1>Segunda vista</h1>")


# def nombre(request, nombre: str, apellido: str, edad: int):
#     nombre = nombre.capitalize()
#     apellido = apellido.capitalize()
#     edad = edad
#     return HttpResponse(f"{apellido}, {nombre} tienes {edad} años")

# def tirar_dados(request):
#     from random import randint

#     resultado = randint(1, 6)
#     if resultado == 6:
#         return HttpResponse(f"<h1>{resultado} Ganaste! 😎</h1>")
#     else:
#         return HttpResponse(f"<h1>{resultado} perdiste 😥 vuelve a tirar</h1>")


# def fecha_hoy(request):
#     from datetime import datetime

#     fecha_hoy = datetime.now()
#     fecha_formateada = fecha_hoy.strftime("%d/%m/%Y %H:%M:%S.%f")
#     return HttpResponse(f"<h1>La fecha y hora actual es {fecha_formateada}</h1>")


def probando_template(request):
    from datetime import datetime

    nombre = "Louis"
    apellido = "Van Beethoven"
    fecha_hoy = datetime.now().strftime("%d/%m/%Y a las %H:%M:%S hs.")
    personas = ["Nicolas", "Maxi", "Danitza"]
    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "fecha_hora": fecha_hoy,
        "personas": personas,
    }
    return render(request, "template1.html", context=datos)

    # mi_html = open("./templates/estudioabogacia/template1.html", encoding="utf-8")
    # mi_template = Template(mi_html.read())
    # mi_html.close() se reemplaza al importar render
    # mi_contexto = Context(datos)
    # mi_documento = mi_template.render(mi_contexto)
    # return HttpResponse(mi_documento)


def probando_template2(request):
    tus_notas = [1, 2, 3, 7, 9, 3]
    notas = {"notas": tus_notas}
    return render(request, "template2.html", context=notas)

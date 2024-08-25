from django.shortcuts import render
from .models import Pais, Cliente


def pais_list(request):
    paises = Pais.objects.all()
    contexto = {"paises": paises}
    return render(request, "clientes/pais_list.html", contexto)


def cliente_list(request):
    clientes = Cliente.objects.all()
    contexto = {"clientes": clientes}
    return render(request, "clientes/cliente_list.html", contexto)

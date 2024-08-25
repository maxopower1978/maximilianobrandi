from django.shortcuts import render
from .models import CategoriaProducto


def index(request):
    return render(request, "productos/index.html")


def producto_list(request):
    productos = CategoriaProducto.objects.all()
    contexto = {"productos": productos}
    return render(request, "productos/producto_list.html", contexto)

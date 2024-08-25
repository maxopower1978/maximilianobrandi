from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path("", views.index, name="index"),
    path("producto/list", views.producto_list, name="producto_list"),
]

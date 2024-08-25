from django.db import models


class CategoriaProducto(models.Model):
    producto = models.CharField(max_length=50, unique=True)
    categoria = models.TextField(max_length=50)

    def __str__(self):
        return f"{self.producto}, es de la categoría {self.categoria}"

    class Meta:
        verbose_name = "Categoria de producto"
        verbose_name_plural = "Categorias de productos"

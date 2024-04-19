from django.db import models

    
# la finalidad de esta tabla es crear una tarjeta de promocion de numero de rifas, tantas como sequieran.
class ValoresPorCantidad(models.Model):
    cantidad = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)

    def __str__(self):
        return self.cantidad

class Rifa(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=500)


class ImagenesRifa(models.Model):
    imagen = models.ImageField(upload_to='static/img/imgPrincipal')

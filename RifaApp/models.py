from django.db import models

# campos dinamicos de la pagina
class Rifa(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=500)
    rango_numeros = models.IntegerField(default=100)
    valor_por_numero = models.CharField(max_length=20)

class logo(models.Model):
    imagen= models.ImageField(upload_to='static/img')

# se guardan las imagenes a mostrar en la pagina 
class Imagen(models.Model):
    imagen = models.ImageField(upload_to='static/img/imagenes')

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'


# la finalidad de esta tabla es crear una tarjeta de promocion de numero de rifas, tantas como sequieran.
class ValoresPorCantidad(models.Model):
    cantidad = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)

    def __str__(self):
        return self.cantidad

class SorteoAnterior(models.Model):
    numero_ganador = models.IntegerField()
    fecha_sorteo = models.DateField(auto_now_add=True)

    def __str__(self):
       return f"Sorteo anterior: {self.numero_ganador} ({self.fecha_sorteo})"
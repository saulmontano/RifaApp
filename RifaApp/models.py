from django.db import models


# la finalidad de esta tabla es cargar una imgen principal para la rifa, con su titulo y la descripcion de la rifa.
class MultimediaPrincipal(models.Model):
    titulo = models.CharField(max_length=100)
    imagen_principal = models.ImageField(upload_to='static/img/multimedia_principal/')
    descripcion = models.TextField()

# la finalidad de esta tabla es cargar las demas imagenes y videos relacionados en la rifa.
class MultimediaSecundaria(models.Model):
    archivo = models.FileField(upload_to='static/img/multimedia_secundaria/')
    # Puedes agregar más campos según tus necesidades

    
# la finalidad de esta tabla es crear una tarjeta de promocion de numero de rifas, tantas como sequieran.
class ValoresPorCantidad(models.Model):
    cantidad = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)

    def __str__(self):
        return self.cantidad

from django.contrib import admin
from .models import *
# Register your models here.
# se suben las tablas a mostrar en el administrador de Django
admin.site.register(ValoresPorCantidad)
admin.site.register(Rifa)
admin.site.register(Imagen)

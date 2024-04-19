from django.shortcuts import render
from django.http import HttpResponse

from .models import *# se importan todos los modelos

def pagina_principal(request):
    # Se guardan los valores del modelo ValoresPorCantidad en la variable "valores"
    valores = ValoresPorCantidad.objects.all()
    
    # Obtener los valores de los campos, con first se optiene el primer dato de la tabla-modelo
    primera_rifa = Rifa.objects.first()
    # validacion de que no este vacia, si lo esta enviar nulo
    titulo = primera_rifa.titulo if primera_rifa else None
    # validacion de que no este vacia, si lo esta enviar nulo
    descripcion = primera_rifa.descripcion if primera_rifa else None

    # Obtener la primera imagen de la rifa
    primera_imagen = ImagenesRifa.objects.first()
    # Obtener la URL de la imagen desde el modelo 
    imagen_url = primera_imagen.imagen.url if primera_imagen else None

    context ={
        'valores': valores,
        'titulo':titulo, 
        'descripcion': descripcion, 
        'imagen_url': imagen_url,
        
    }

    return render(request, 'pagina_principal.html', context)
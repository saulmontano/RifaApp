from django.shortcuts import render
from django.http import HttpResponse

from .models import *# se importan todos los modelos


def pagina_principal(request):
    # Obtener los valores de los campos, con first se optiene el primer dato de la tabla-modelo
    primera_rifa = Rifa.objects.first()
    # validacion de que no este vacia, si lo esta enviar nulo
    titulo = primera_rifa.titulo if primera_rifa else None
    # validacion de que no este vacia, si lo esta enviar nulo
    descripcion = primera_rifa.descripcion if primera_rifa else None
    # numero ganador de sorteo anterior 
    sorteo_anterior = SorteoAnterior.objects.last()
    # Obtener todas las imágenes
    imagenes = Imagen.objects.all()
    # Separar la primera imagen para mostrarla como imagen principal
    imagen_principal = imagenes.first()
    imagen_principal_url = imagen_principal.imagen.url if imagen_principal else None
    # Resto de las imágenes para el scroll
    imagenes_scroll = imagenes[1:]


    # Se guardan los valores del modelo ValoresPorCantidad en la variable "valores"
    valores = ValoresPorCantidad.objects.all()


    # Recuperar la rifa más reciente
    rifa = Rifa.objects.order_by('-id').first()
    # Verificar si se recuperó alguna instancia de Rifa
    if rifa:
        valor_por_numero = rifa.valor_por_numero
    else:
        # Si no hay ninguna instancia de Rifa, asignar un valor predeterminado
        valor_por_numero = 0.00  # Puedes ajustar este valor 
        
        
        
    context ={
        'valores': valores,
        'titulo':titulo, 
        'descripcion': descripcion, 
        'imagen_principal_url': imagen_principal_url,
        'imagenes_scroll': imagenes_scroll,
        'valor_por_numero': valor_por_numero,
        'sorteo_anterior' : sorteo_anterior,
    }

    return render(request, 'pagina_principal.html', context)

def carrito(request):
     
    primera_rifa = Rifa.objects.first()
    # validacion de que no este vacia, si lo esta enviar nulo
    titulo = primera_rifa.titulo if primera_rifa else None
    # validacion de que no este vacia, si lo esta enviar nulo
    descripcion = primera_rifa.descripcion if primera_rifa else None
    # numero ganador de sorteo anterior 
    sorteo_anterior = SorteoAnterior.objects.last()
    # Obtener todas las imágenes
    imagenes = Imagen.objects.all()
    # Separar la primera imagen para mostrarla como imagen principal
    imagen_principal = imagenes.first()
    imagen_principal_url = imagen_principal.imagen.url if imagen_principal else None
    # Resto de las imágenes para el scroll
    imagenes_scroll = imagenes[1:]


    # Se guardan los valores del modelo ValoresPorCantidad en la variable "valores"
    valores = ValoresPorCantidad.objects.all()


    # Recuperar la rifa más reciente
    rifa = Rifa.objects.order_by('-id').first()
    # Verificar si se recuperó alguna instancia de Rifa
    if rifa:
        valor_por_numero = rifa.valor_por_numero
    else:
        # Si no hay ninguna instancia de Rifa, asignar un valor predeterminado
        valor_por_numero = 0.00  # Puedes ajustar este valor 
        
        
        
    context ={
        'valores': valores,
        'titulo':titulo, 
        'descripcion': descripcion, 
        'imagen_principal_url': imagen_principal_url,
        'imagenes_scroll': imagenes_scroll,
        'valor_por_numero': valor_por_numero,
        'sorteo_anterior' : sorteo_anterior,
    }

    return render(request, 'carrito.html', context)
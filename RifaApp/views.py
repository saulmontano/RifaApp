from django.shortcuts import render
from django.http import HttpResponse

from .models import *# se importan todos los modelos

def pagina_principal(request):

    # Se guardan los valores del modelo ValoresPorCantidad en la variable "valores" y se envias a pagina_principal.html
    valores = ValoresPorCantidad.objects.all()

    return render(request, 'pagina_principal.html', {'valores': valores})

def vista_multimedia(request):

    # Se guardan los valores del modelo MultimediaPrincipal en la variable "multimedia_principal" y se envias a pagina_principal.html
    multimedia_principal = MultimediaPrincipal.objects.all()
    multimedia_secundaria = MultimediaSecundaria.objects.all()

    # Se iterando sobre los objetos MultimediaSecundaria y separando aquellos que son videos MP4 de los que son imágenes.
    multimedia_secundaria_con_video = []
    multimedia_secundaria_con_imagen = []

    for item in multimedia_secundaria:
        if item.archivo.name.lower().endswith('.mp4'):
            multimedia_secundaria_con_video.append(item)
        else:
            multimedia_secundaria_con_imagen.append(item)
    return render(request, 'plantilla.html', {'multimedia_principal': multimedia_principal, 'multimedia_secundaria_con_video': multimedia_secundaria_con_video, 'multimedia_secundaria_con_imagen': multimedia_secundaria_con_imagen})
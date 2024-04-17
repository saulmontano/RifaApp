from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    # recive una solicitud y retorna una respuesta con el archivo base.html
    return render(request,'base.html') 


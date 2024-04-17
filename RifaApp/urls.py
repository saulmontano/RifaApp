from django.urls import path
from . import views


urlpatterns={
    # llamar a la funcion inicio en el archivo views.py y donde en esta responde con el archivo base.html
    path('',views.inicio, name='inicio'),
}
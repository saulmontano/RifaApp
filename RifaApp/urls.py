from django.urls import path
from . import views

urlpatterns = [
    # Llamar a la función inicio en el archivo views.py y responder con el archivo base.html
    path('', views.pagina_principal, name='pagina_principal'),
    path('carrito/', views.carrito, name='carrito'),
    
]
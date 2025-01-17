"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt  # Importa csrf_exempt
from platos.views import index, solicitudes
from pedidos.views import listar_pedidos
from platosPedidos.views import mostrar_carrito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datosTarjetas/', csrf_exempt(index), name='lista_platos'),  # Aplica csrf_exempt a la vista
    path('cocina/', csrf_exempt(listar_pedidos) ),
    path('carrito/', csrf_exempt(mostrar_carrito)),
    path("solicitudes/",csrf_exempt(solicitudes)),
]





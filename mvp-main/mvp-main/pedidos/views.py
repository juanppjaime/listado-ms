from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

def listar_pedidos(request):
    restaurantes = settings.DB["Restaurantes"]
    documento = restaurantes.find_one({"nombre": "Restaurante de los Alpes"})
    pedidos = documento["pedido"]
    estado = documento["estado"]
    if estado == "ordenando":
        return render(request, "lista_pedidos.html", {"mensaje": "No hay pedidos aún"})
    if request.method == "POST":
        restaurantes.update_one({"nombre": "Restaurante de los Alpes"}, {"$set": {"estado": "ordenando", "pedido": []}})
    return render(request, "lista_pedidos.html", {"pedidos": pedidos, "mensaje": "¡Pedidos Actuales!"})
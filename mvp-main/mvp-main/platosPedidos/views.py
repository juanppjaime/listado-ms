from django.shortcuts import render
from django.conf import settings

def mostrar_carrito(request):
    restaurantes = settings.DB["Restaurantes"]
    documento = restaurantes.find_one({"nombre": "Restaurante de los Alpes"})
    pedidos = documento["pedido"]
    estado = documento["estado"]
    if estado == "confirmado":
        return render(request, "carrito.html", {"mensaje": "Se esta preparando su pedido, por favor espere...", "total": 0})
    if not pedidos:
        return render(request, "carrito.html", {"mensaje": "No hay productos en el carrito", "total": 0})
    if request.method == "POST":
        restaurantes.update_one({"nombre": "Restaurante de los Alpes"}, {"$set": {"estado": "confirmado"}})
        return render(request, "carrito.html", {"mensaje": "Pedido confirmado, gracias por su compra", "total": 0})

    
    return render(request, "carrito.html", {"pedidos": pedidos, "total": sum([p["precio"] for p in pedidos])})

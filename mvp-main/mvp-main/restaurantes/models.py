from djongo import models
from mesas.models import Mesa
from pedidos.models import Pedido
from platos.models import Plato

class Restaurante(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    logo = models.CharField(max_length=255)
    mesas = models.ArrayField(model_container=Mesa, null=True, blank=True)
    pedidos = models.ArrayField(model_container=Pedido, null=True, blank=True)
    platos = models.ArrayField(model_container=Plato, null=True, blank=True)

    def __str__(self):
        return self.nombre
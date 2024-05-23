from djongo import models

class Pedido(models.Model):
    class Estado(models.TextChoices):
        ORDENADO = 'ORDENADO', 'Ordenado'
        LISTO = 'LISTO', 'Listo'
        ENTREGADO = 'ENTREGADO', 'Entregado'
        PAGADO = 'PAGADO', 'Pagado'

    id_plato = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=50, choices=Estado.choices, default=Estado.ORDENADO)
    total = models.IntegerField(null=True, blank=True)

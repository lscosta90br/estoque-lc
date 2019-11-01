from django.db import models
from django.utils import timezone
from projeto.cliente.models import Cliente
from projeto.produto.models import Produto


class Pedido(models.Model):
    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    observacoes = models.CharField(max_length=300, null=False, blank=False)
    data_pedido = models.DateTimeField(default=timezone.now)
    valor = models.FloatField(blank=False, null=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False)
    produtos = models.ManyToManyField(Produto)

    def __str__(self):
        return self.cliente.nome

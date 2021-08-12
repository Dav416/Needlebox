from django.db import models

# Create your models here.

# ---TABLAS/MODELOS DEL MODULO PEDIDOS---
# Modelo/tabla de modulo cronograma, para registrar pedidos
class Todopedido(models.Model):
    # DeleteAccount = models.ForeignKey(Profile, on_delete=models.PROTECT)  # foreing key borrar info al borrar perfil
    # DeleteClient = models.ForeignKey(InfoClient, on_delete=models.PROTECT)  # foreing key borrar info al borrar cliente
    #numPedido = models.IntegerField(max_length=None, unique=True, verbose_name="Número de pedido")
    pedido = models.CharField(max_length=20, verbose_name="Pedido")
    estado = models.CharField(max_length=20, verbose_name="Estado")
    descri = models.CharField(max_length=20, verbose_name="Descripción")
    client = models.CharField(max_length=20, verbose_name="Cliente")
    fechadEnt = models.CharField(max_length=100, blank=True, verbose_name='Fecha de entrega')

    def __str__(self):
        return self.numPedido

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']
from crum import get_current_user
from django.db import models

# ---TABLAS/MODELOS DEL MODULO CRONOGRAMA---
# Modelo/tabla de modulo cronograma, para registrar pedidos
from django.forms import model_to_dict

from core.models import BaseModel


class RegisPedido(BaseModel):
    # DeleteAccount = models.ForeignKey(Profile, on_delete=models.PROTECT)  # foreing key borrar info al borrar perfil
    # DeleteClient = models.ForeignKey(InfoClient, on_delete=models.PROTECT)  # foreing key borrar info al borrar client
    nombCli = models.CharField(max_length=50, verbose_name='Nombre cliente')
    descriped = models.TextField(max_length=2000, verbose_name="Detalles del pedido")
    costoped = models.PositiveIntegerField(default=0, verbose_name="Costo del pedido")
    fecharec = models.DateField(max_length=100, verbose_name='Fecha de recibo')
    fechaLiEn = models.DateField(max_length=100, blank=True, verbose_name='Fecha de limite de entrega')
    med_entr = [
        ('', 'Seleccione un medio de entrega'),
        ('Correo', 'Servicio de correo o mensajería'),
        ('Fábrica / local', 'Directamente en fábrica / local'),
        ('Otro', 'Otro punto o medio'),
    ]
    medentr = models.CharField(max_length=50, choices=med_entr, null=False, default='', verbose_name="Medio de entrega")
    DetailEntr = models.TextField(max_length=1000, verbose_name="Lugar de entrega")
    estped = models.CharField(max_length=50, null=False, verbose_name="Estado del pedido")


    def __str__(self):
        return self.nombCli

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(RegisPedido, self).save()


    def pedidotojson(self):
        itemped = model_to_dict(self)
        return itemped

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']
from django.db import models



# ---TABLAS/MODELOS DEL MODULO CRONOGRAMA---
# Modelo/tabla de modulo cronograma, para registrar pedidos
class CronoForm(models.Model):
    # DeleteAccount = models.ForeignKey(Profile, on_delete=models.PROTECT)  # foreing key borrar info al borrar perfil
    # DeleteClient = models.ForeignKey(InfoClient, on_delete=models.PROTECT)  # foreing key borrar info al borrar cliente
    nombCli = models.CharField(max_length=50, verbose_name='Nombre cliente')
    fecharec = models.CharField(max_length=100, verbose_name='Fecha de recibo')

    # opciones para seleccion de tipo de pedido
    prenda = 'Prenda(s)'
    colecc = 'Colección'
    modifi = 'Modificación'
    repara = 'Reparación'

    tipo_pedido = (
        (prenda, 'Prenda(s)'),
        (colecc, 'Colección'),
        (modifi, 'Modificación'),
        (repara, 'Reparación')
    )
    tipoped = models.CharField(max_length=100, choices=tipo_pedido, unique=True, verbose_name='Tipo de pedido')
    fechaLiEn = models.CharField(max_length=100, blank=True, verbose_name='Fecha de limite de entrega')
    lugarEntr = models.CharField(max_length=200, verbose_name="Lugar de entrega")

    # opciones para seleccion de medio de entrega
    correo = 'Correo'
    fab_loc = 'Fábrica o local'
    pyhde = 'Acordar punto y hora'
    medio_entre = (
        (correo, 'Correo'),
        (fab_loc, 'Fábrica o local'),
        (pyhde, 'Acordar punto y hora')
    )
    medentr = models.CharField(max_length=100, choices=medio_entre, unique=True, verbose_name='Medio de entrega')

    def __str__(self):
        return self.nombCli

    class Meta:
        verbose_name = 'Cronograma'
        verbose_name_plural = 'Cronograma'
        ordering = ['id']



from django.db import models


# ---No se crea Modelo/tabla para recuperar ocntraseña o iniciar sesión por obvias razones.---

# Modelo/tabla de modulo contactar desarroladores
class ContactUs(models.Model):
    cont_nombre = models.CharField(max_length=100, verbose_name="Nombre")
    correo_proveedor = models.EmailField(max_length=50, verbose_name="E-mail de contacto", unique=True)
    cont_asunto = models.CharField(max_length=500, verbose_name="Asunto")
    cont_mensaje = models.TextField(max_length=2000, verbose_name="Asunto")

    def __str__(self):
        return self.cont_nombre

    class Meta:
        verbose_name = 'Usuario en contacto'
        verbose_name_plural = 'Usuarios en contacto'
        ordering = ['id']



# ---TABLAS/MODELOS DEL MODULO CRONOGRAMA---
# Modelo/tabla de modulo cronograma, para registrar pedidos
class CronoForm(models.Model):
    # DeleteAccount = models.ForeignKey(Profile, on_delete=models.PROTECT)  # foreing key borrar info al borrar perfil
    #DeleteClient = models.ForeignKey(InfoClient, on_delete=models.PROTECT)  # foreing key borrar info al borrar cliente
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


# ---TABLAS/MODELOS DEL MODULO PEDIDOS---
# Modelo/tabla de modulo cronograma, para registrar pedidos
class Todopedido(models.Model):
    # DeleteAccount = models.ForeignKey(Profile, on_delete=models.PROTECT)  # foreing key borrar info al borrar perfil
    #DeleteClient = models.ForeignKey(InfoClient, on_delete=models.PROTECT)  # foreing key borrar info al borrar cliente
    numPedido = models.IntegerField(max_length=None, unique=True, verbose_name="Número de pedido")
    pedido = models.CharField(max_length=20, verbose_name="Pedido")
    descri = models.CharField(max_length=20, verbose_name="Descripción")
    client = models.CharField(max_length=20, verbose_name="Cliente")
    fechadEnt = models.CharField(max_length=100, blank=True, verbose_name='Fecha de entrega')

    def __str__(self):
        return self.numPedido

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']
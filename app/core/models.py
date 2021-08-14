from django.db import models


# Modelo/tabla para llevar conteo de registro, podría permitir que un usuario recupere su cuenta
# Tabla de resgistro de usuario
class RegUsu(models.Model):
    nomComUsu = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    e_mailUsu = models.EmailField(unique=True, verbose_name='E-mail')
    passwordUsu = models.CharField(max_length=10, verbose_name='Contraseña')
    conf_passwordUsu = models.CharField(max_length=10, verbose_name='Confirmar Contraseña')
    accept_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.e_mailUsu

    class Meta:
        verbose_name = 'Registrar usuario'
        verbose_name_plural = 'Registrar Usuarios'
        ordering = ['id']


# ---No se crea Modelo/tabla para recuperar ocntraseña o iniciar sesión por obvias razones.---





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



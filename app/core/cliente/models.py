from django.db import models

# Create your models here.

# ---TABLAS/MODELOS DEL MODULO CLIENTES---

# Modelo/tabla de modulo clientes, para registrar información básica de cliente
class InfoClient(models.Model):
    # DeleteAccount = models.ForeignKey(Profile, on_delete=models.PROTECT)  # foreing key: borrar info al borrar perfil
    # codecli = models.IntegerField(max_length=None, unique=True, verbose_name="codigo identificador cliente")
    nomCli = models.CharField(max_length=50, unique=True, verbose_name='Nombre cliente')
    apeCli = models.CharField(max_length=50, unique=True, verbose_name='Apellido cliente')
    telCli = models.IntegerField(default=0, unique=True, verbose_name="Teléfono cliente")
    celCli = models.IntegerField(default=0, unique=True, verbose_name="celular cliente")
    e_mailCli = models.EmailField(unique=True, verbose_name='E-mail cliente')
    dirCli = models.CharField(max_length=50, verbose_name="Dirección de cliente")
    imgCli = models.ImageField(upload_to='Fotos-Clientes', null=True, blank=True)

    def __str__(self):
        return self.nomCli, self.apeCli

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


# Modelo/tabla de modulo clientes, para registrar medidas y otra información de pedidos
class InfoGeneClient(models.Model):

    # opciones tipo cliente
    cli_loc = 'cliente local'
    cli_nal = 'cliente nacional'

    cliente_opciones = (
        (cli_loc, 'cliente local'),
        (cli_nal, 'cliente nacional'))

    # opciones estilo cliente
    clasico = 'clasico'
    deportivo = 'deportivo'
    moderno = 'moderno'
    oficio = 'oficio'
    otro = 'otro'
    ninguno = 'ninguno'

    estilo_clientes = (
        (clasico, 'clasico'),
        (deportivo, 'deportivo'),
        (moderno, 'moderno'),
        (oficio, 'oficio'),
        (otro, 'otro'),
        (ninguno, 'ninguno'))

    # opciones medio de pago cliente
    efec = 'Efectivo'
    tarj = 'Tarjeta'
    trans = 'Transferencia'
    giro = 'Giro'

    medio_pago = (
        (efec, 'Efectivo'),
        (tarj, 'Tarjeta'),
        (trans, 'Transferencia'),
        (giro, 'Giro'))

    # DeleteAccount = models.ForeignKey(Profile, on_delete=models.PROTECT)  # foreing key borrar info al borrar  perfil
    #DeleteClient = models.ForeignKey(InfoClient, on_delete=models.PROTECT)  # foreing key borrar info al borrar cliente
    # codecli2 = models.IntegerField(InfoClient.codecli, unique=True, default=InfoClient.codecli) llama atributo ajeno
    infoTCli = models.TextField(max_length=3000, verbose_name="Info técnica cliente")
    ver_ITC = models.CharField(max_length=200, null=True, blank=True, verbose_name='verificación realizada')
    revP_ITC = models.CharField(max_length=200, null=True, blank=True, verbose_name='Revisar pronto')
    revIM_ITC = models.CharField(max_length=200,  null=True, blank=True, verbose_name='Revisar de inmediato')
    tipoCli = models.CharField(choices=cliente_opciones, default=cli_loc, max_length=100)
    prenda = models.BooleanField(null=True, verbose_name='tipos de prenda')
    estilCli = models.CharField(choices=estilo_clientes, default=ninguno, max_length=100)
    medPag = models.CharField(choices=medio_pago, default=efec, max_length=100)

    def __str__(self):
        return self.prenda  # codecli2 (mostraría este atributo de la entidad InfoClient para identificar la prenda)

    class Meta:
        verbose_name = 'Detalle Cliente'
        verbose_name_plural = 'Detalles Clientes'
        ordering = ['id']


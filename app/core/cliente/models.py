from django.db import models

# Create your models here.

# ---TABLAS/MODELOS DEL MODULO CLIENTES---

# Modelo/tabla de modulo clientes, para registrar información básica de cliente
class InfoClient(models.Model):
    # DeleteAccount = models.ForeignKey(Profile, on_delete=models.PROTECT)  # foreing key: borrar info al borrar perfil
    # codecli = models.IntegerField(max_length=None, unique=True, verbose_name="codigo identificador cliente")
    id = models.AutoField(primary_key=True)
    nomCli = models.CharField(max_length=50, verbose_name='Nombre cliente')
    apeCli = models.CharField(max_length=50, verbose_name='Apellido cliente')
    telCli = models.PositiveIntegerField(default=0, unique=False, verbose_name="Teléfono cliente")
    celCli = models.PositiveIntegerField(default=0, unique=False, verbose_name="celular cliente")
    e_mailCli = models.EmailField(unique=True, verbose_name='E-mail cliente')
    dirCli = models.CharField(max_length=50, unique=False, verbose_name="Dirección de cliente")

    def nombreCompleto(self):
        txt = '{} {}'
        return txt.format(self.nomCli, self.apeCli)


    def __str__(self):
        txt = 'Cliente {}, Número {}'
        return txt.format(self.nombreCompleto(), self.id)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


# Modelo/tabla de modulo clientes, para registrar medidas y otra información de pedidos
class InfoGeneClient(models.Model):

    # opciones tipo cliente
    cli_loc = 'Cliente local'
    cli_nal = 'Cliente nacional'

    cliente_opciones = [
        (cli_loc, 'Cliente local'),
        (cli_nal, 'Cliente nacional')
    ]

    # opciones tipo prenda
    vestido = 'Vestido'
    pantalon = 'Pantalón'
    chaqueta = 'Chaqueta'
    blusa_camisa = 'Blusa/Camisa'

    tipos_prendas = [
        (vestido, 'Vestido'),
        (pantalon, 'Pantalón'),
        (chaqueta, 'Chaqueta'),
        (blusa_camisa, 'Blusa/Camisa')
    ]

    # opciones estilo cliente
    clasico = 'Clasico'
    deportivo = 'Deportivo'
    moderno = 'Moderno'
    oficio = 'Oficio'
    otro = 'Otro'
    ninguno = 'Ninguno'

    estilo_clientes = [
        (clasico, 'Clasico'),
        (deportivo, 'Deportivo'),
        (moderno, 'Moderno'),
        (oficio, 'Oficio'),
        (otro, 'Otro'),
        (ninguno, 'Ninguno')
    ]

    # opciones medio de pago cliente
    efec = 'Efectivo'
    tarj = 'Tarjeta'
    trans = 'Transferencia'
    giro = 'Giro'

    medio_pago = [
        (efec, 'Efectivo'),
        (tarj, 'Tarjeta'),
        (trans, 'Transferencia'),
        (giro, 'Giro')
    ]

    # DeleteAccount = models.ForeignKey(Profile, on_delete=models.PROTECT)  # foreing key borrar info al borrar  perfil
    #DeleteClient = models.ForeignKey(InfoClient, on_delete=models.PROTECT)  # foreing key borrar info al borrar cliente
    # codecli2 = models.IntegerField(InfoClient.codecli, unique=True, default=InfoClient.codecli) llama atributo ajeno
    infoTCli = models.TextField(max_length=3000, verbose_name="Información técnica del cliente")
    ver_ITC = models.CharField(max_length=200, null=False, blank=False, verbose_name='Nota de Verificación realizada')
    revP_ITC = models.CharField(max_length=200, null=True, blank=True, verbose_name='Nota Revisar pronto')
    revIM_ITC = models.CharField(max_length=200,  null=True, blank=True, verbose_name='Nota Revisar de inmediato')
    tipoCli = models.CharField(choices=cliente_opciones, default=cli_loc, max_length=100, verbose_name='Tipo de cliente')
    prenda = models.CharField(choices=tipos_prendas, default= vestido, max_length=100, verbose_name='Tipos de prenda')
    estilCli = models.CharField(choices=estilo_clientes, default=ninguno, max_length=100, verbose_name='Estilo del cliente')
    medPag = models.CharField(choices=medio_pago, default=efec, max_length=100, verbose_name='Medio de pago habitual')

    def __str__(self):
        txt = 'Información adicional {}'
        return txt.format(self.tipoCli)

    class Meta:
        verbose_name = 'Detalle Cliente'
        verbose_name_plural = 'Detalles Clientes'
        ordering = ['id']


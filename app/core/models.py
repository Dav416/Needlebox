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
    DeleteClient = models.ForeignKey(InfoClient, on_delete=models.PROTECT)  # foreing key borrar info al borrar cliente
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


# ---TABLAS/MODELOS DEL MODULO CRONOGRAMA---
# Modelo/tabla de modulo cronograma, para registrar pedidos
class CronoForm(models.Model):
    # DeleteAccount = models.ForeignKey(Profile, on_delete=models.PROTECT)  # foreing key borrar info al borrar perfil
    DeleteClient = models.ForeignKey(InfoClient, on_delete=models.PROTECT)  # foreing key borrar info al borrar cliente
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
    DeleteClient = models.ForeignKey(InfoClient, on_delete=models.PROTECT)  # foreing key borrar info al borrar cliente
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
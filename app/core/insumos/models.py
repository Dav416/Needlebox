from django.db import models


# Create your models here.
# ---TABLAS/MODELOS DEL MODULO INSUMOS---
# Modelo/tabla de modulo insumos, para registrar INSUMOS de confección
class InsRegInsu(models.Model):
    select_tip = 'Sel-tip-ins'
    tela = 'telas'
    hilo = 'hi-y-la'
    adorno = 'ado-y-bis'
    accesorio = 'acc-cin-com'
    herramienta = 'he-in'
    otros = 'otr'

    SQ_CHOICES = [
        ('select_tip', 'Seleccione un tipo de insumo'),
        ('tela', 'Telas'),
        ('hilo', 'Hilos y lanas'),
        ('adorno', 'Adorno y bisutería'),
        ('accesorio', 'Accesorios, cintas y complementos'),
        ('herramienta', 'Herramientas e instrumentos'),
        ('otros', 'Otros'),
    ]
    # DeleteAccount = models.ForeignKey(Profile, on_delete=models.PROTECT)  # foreing key borrar info al borrar perfil
    # DeleteClient = models.ForeignKey(InfoClient, on_delete=models.PROTECT) # foreing key borrar info al borrar cliente
    # rel_InsuProv = models.ManyToManyField(InsRegProv)  # rel muchos insumos / muchos proveedores (agotamiento insumo)
    tipo_insumo = models.CharField(max_length=30, choices=SQ_CHOICES, default=select_tip)
    especificacion_insumo = models.TextField(max_length=1500, verbose_name="Tipo, marca y otros")
    estado_insumo = models.CharField(max_length=30, verbose_name="Cantidad o estado")
    costxunid_insumo_costo = models.PositiveIntegerField(default=0)
    costxunid_insumo_unidad = models.CharField(max_length=20, verbose_name="cm, kilos, unidades, etc")

    def __str__(self):
        return self.tipo_insumo

    class Meta:
        verbose_name = 'Registro insumo'
        verbose_name_plural = 'Registro insumos'
        ordering = ['id']


# Modelo/tabla de modulo insumos, para registrar PROVEEDORES de confección
class InsRegProv(models.Model):
    # DeleteAccount = models.ForeignKey(Profile, on_delete=models.PROTECT) # foreing key borrar info al borrar el perfil
    # DeleteClient = models.ForeignKey(InfoClient, on_delete=models.PROTECT) # foreing key borrar info al borrar cliente
    rel_ProvInsu = models.ManyToManyField(InsRegInsu)  # rel muchos proveedores/muchos insumos (para agotamiento insumo)
    nombre_proveedor = models.CharField(max_length=100, verbose_name="Establecimiento/persona")
    Insumos_proveedor = models.TextField(max_length=2000, verbose_name="Insumos que vende")
    telefono_proveedor = models.IntegerField(default=0, unique=True)
    correo_proveedor = models.EmailField(max_length=50, verbose_name="E-mail proveedor", unique=True)
    ubicacion_proveedor = models.CharField(max_length=50, verbose_name="Dirección de proveedor")

    def __str__(self):
        return self.nombre_proveedor

    class Meta:
        verbose_name = 'Registro proveedor'
        verbose_name_plural = 'Registro proveedores'
        ordering = ['id']
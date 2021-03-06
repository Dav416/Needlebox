from crum import get_current_user
from django.db import models


# Create your models here.
# ---TABLAS/MODELOS DEL MODULO INSUMOS---
# Modelo/tabla de modulo insumos, para registrar INSUMOS de confección
from django.forms import model_to_dict
from core.user.models import User
from core.models import BaseModel


class InsRegInsu(BaseModel):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # foreing key: borrar info al borrar perfil
    SQ_CHOICES = [
        ('', 'Seleccione un tipo de insumo'),
        ('Tela', 'Telas'),
        ('Hilos/lanas/cordones', 'Hilos, lanas, cordones'),
        ('Adorno/Bisuteria', 'Adorno y bisutería'),
        ('Accesorios/Complementos', 'Accesorios, cintas y complementos'),
        ('Herramienta/instrumento', 'Herramientas e instrumentos'),
        ('Otros', 'Otros'),
    ]
    tipo_insumo = models.CharField(max_length=30, choices=SQ_CHOICES, null=False, default='', verbose_name="Sel\
    eccione un tipo de insumo")
    especificacion_insumo = models.TextField(max_length=100, verbose_name="Tipo, marca y otros")
    estado_insumo = models.CharField(max_length=30, verbose_name="Cantidad o estado")
    costxunid_insumo_costo = models.PositiveIntegerField(default=0, verbose_name="Costo insumo")
    costxunid_insumo_unidad = models.CharField(max_length=20, verbose_name="Cm, kilos, unidades, etc")

    def __str__(self):
        return self.tipo_insumo

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(InsRegInsu, self).save()


    def insutojson(self):
        iteminsu = model_to_dict(self)
        return iteminsu

    class Meta:
        verbose_name = 'Registro insumo'
        verbose_name_plural = 'Registro insumos'
        ordering = ['id']


# Modelo/tabla de modulo insumos, para registrar PROVEEDORES de confección
class InsRegProv(BaseModel):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)  # foreing key: borrar info al borrar perfil
    nombre_proveedor = models.CharField(max_length=60, verbose_name="Establecimiento/persona")
    Insumos_proveedor = models.TextField(max_length=222, verbose_name="Insumos que vende")
    telefono_proveedor = models.IntegerField(unique=True, verbose_name="Teléfono proveedor")
    correo_proveedor = models.EmailField(max_length=50, unique=True, verbose_name="E-mail proveedor")
    ubicacion_proveedor = models.CharField(max_length=50, verbose_name="Dirección de proveedor")

    def __str__(self):
        return self.nombre_proveedor

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(InsRegProv, self).save()


    def provtojson(self):
        itemprov = model_to_dict(self)
        return itemprov

    class Meta:
        verbose_name = 'Registro proveedor'
        verbose_name_plural = 'Registro proveedores'
        ordering = ['id']

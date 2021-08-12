from django.db import models

# Create your models here.

# Modelo/tabla de modulo reportar error

class Reportfail(models.Model):

    SQ_CHOICES = [
        ('Select_type', 'Seleccione un tipo de error'),
        ('Leve', 'Error Leve'),
        ('Moderado', 'Error Moderado'),
        ('Grave', 'Error Grave'),
    ]

    error_nombre = models.CharField(max_length=100, verbose_name="Nombre")
    correo_usu = models.EmailField(max_length=50, verbose_name="Correo electronico", unique=True)
    tip_error = models.CharField(max_length=30, verbose_name='Seleccione un tipo de error', choices=SQ_CHOICES, null=False, default='Select_type')
    cont_mensaje = models.TextField(max_length=2000, verbose_name="Mensaje")

    def __str__(self):
        return self.error_nombre

    class Meta:
        verbose_name = 'Reportar un error'
        verbose_name_plural = 'Reportar unos errores'
        ordering = ['id']
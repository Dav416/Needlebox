from django.db import models

# Create your models here.

# Modelo/tabla de modulo contactar desarroladores
class ContactUs(models.Model):
    cont_nombre = models.CharField(max_length=100, verbose_name="Nombre")
    correo_usu= models.EmailField(max_length=50, verbose_name="E-mail de contacto", unique=True)
    cont_asunto = models.CharField(max_length=500, verbose_name="Asunto")
    cont_mensaje = models.TextField(max_length=2000, verbose_name="Mensaje")

    def __str__(self):
        return self.cont_nombre

    class Meta:
        verbose_name = 'Usuario en contacto'
        verbose_name_plural = 'Usuarios en contacto'
        ordering = ['id']
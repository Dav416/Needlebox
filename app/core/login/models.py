from django.db import models

# Create your models here.

# Modelo/tabla para llevar conteo de registro, podría permitir que un usuario recupere su cuenta
# Tabla de resgistro de usuario
class RegUsu(models.Model):
    nomComUsu = models.CharField(max_length=100, unique=False, verbose_name='Nombre')
    e_mailUsu = models.EmailField(unique=True, verbose_name='E-mail')
    passwordUsu = models.CharField(max_length=10, verbose_name='Contraseña')
    conf_passwordUsu = models.CharField(max_length=10, verbose_name='Confirmar Contraseña')
    accept_terms = models.BooleanField(default=False, verbose_name='Aceptar términos y condiciones')

    def __str__(self):
        return self.e_mailUsu

    class Meta:
        verbose_name = 'Registrar usuario'
        verbose_name_plural = 'Registrar Usuarios'
        ordering = ['id']



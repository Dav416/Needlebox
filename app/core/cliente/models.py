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
    infoTCli = models.TextField(max_length=3000, verbose_name="Información técnica del cliente")

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




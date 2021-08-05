from django.db import models


# Create your models here.
# Modelo/tabla de modulo perfil, para modificar la información de cada cuenta
class Profile(models.Model):
    select_q = 'Sel-una-pre'
    color = 'Col-fav'
    food = 'Ali-fav'
    pet = 'Mas-inf'
    admired = 'Per-adm'
    book = 'Lib-fav'
    song = 'Can-fav'

    SQ_CHOICES = [
        ('select_q', 'Seleccione una pregunta'),
        ('color', 'Color favorito'),
        ('food', 'Alimento favorito'),
        ('pet', 'Mascota de la infancia'),
        ('admired', 'Persona admirada'),
        ('book', 'Libro favorito'),
        ('song', 'Canción favorita'),
    ]

    # re_RegyProf = models.OneToOneField(RegUsu, on_delete=models.PROTECT)  # Rel registro usuario e info de cuenta
    nom_usu = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    e_mail = models.EmailField(unique=True, verbose_name='E-mail')
    password = models.CharField(max_length=50, verbose_name='Contraseña')
    conf_password = models.CharField(max_length=50, verbose_name='Confirmar Contraseña')
    show_password = models.BooleanField(default=False)
    security_question = models.CharField(max_length=30, choices=SQ_CHOICES, default=select_q)
    security_answer = models.CharField(max_length=50, verbose_name="Respect")
    accept_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.nom_usu

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['id']

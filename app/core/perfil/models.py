from django.db import models


# Create your models here.
# Modelo/tabla de modulo perfil, para modificar la información de cada cuenta
class Profile(models.Model):

    SQ_CHOICES = [
        ('', 'Seleccione una pregunta'),
        ('Color favorito', 'Color favorito'),
        ('Comida favorita ', 'Alimento favorito'),
        ('Mascota de la infancia', 'Mascota de la infancia'),
        ('Persona admirada', 'Persona admirada'),
        ('Libro favorito', 'Libro favorito'),
        ('Canción Favorita', 'Canción favorita'),
    ]

    # re_RegyProf = models.OneToOneField(RegUsu, on_delete=models.PROTECT)  # Rel registro usuario e info de cuenta
    nom_usu = models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario')
    e_mail = models.EmailField(unique=True, verbose_name='E-mail')
    password = models.CharField(max_length=50, verbose_name='Contraseña')
    conf_password = models.CharField(max_length=50, verbose_name='Confirmar Contraseña')
    show_password = models.BooleanField(default=False)
    security_question = models.CharField(max_length=30, choices=SQ_CHOICES, default='', null=False)
    security_answer = models.CharField(max_length=50, verbose_name="Respect", null=False)
    accept_terms = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.nom_usu

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['id']
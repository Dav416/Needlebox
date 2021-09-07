from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    SQ_CHOICES = [
        ('', 'Seleccione una pregunta'),
        ('Color favorito', 'Color favorito'),
        ('Comida favorita ', 'Alimento favorito'),
        ('Mascota de la infancia', 'Mascota de la infancia'),
        ('Persona admirada', 'Persona admirada'),
        ('Libro favorito', 'Libro favorito'),
        ('Canción Favorita', 'Canción favorita'),
    ]
    security_question = models.CharField(max_length=30, choices=SQ_CHOICES, default=None, null=False)
    security_answer = models.CharField(max_length=50, verbose_name="Respect", null=False, default=None)
    conf_password = models.CharField(max_length=50, verbose_name='Confirmar Contraseña', default=None, blank=True)
    accept_terms = models.BooleanField(default=False, null=False, blank=False)
    AbstractUser._meta.get_field('email')._unique = True

    token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.set_password(self.password)
        else:
            user = User.objects.get(pk=self.pk)
            if user.password != self.password:
                self.set_password(self.password)
        super().save(*args, **kwargs)

from django.db import models
from datetime import datetime

"""
class Employee(models.Model):
    names = models.CharField(max_length = 150,verbose_name='Nombres')
    cc = models.CharField(max_length = 10,verbose_name='Cedula')
    date_joined = models.DateField(default= datetime.now, verbose_name='Fecha de registro')
    date_creation = models.DateTimeField(auto_now=True)
    date_uptdate = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00,max_digits=9,decimal_places=2)
    state = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/%y/%m/%d', null=True, blank=True)
    curriculum = models.FileField(upload_to='avatar/%y/%m/%d',null=True, blank=True)

        def __str__(self):
            return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
        db_table = 'empleado'
    """

class informacion_personal(models.Model):
    user_name = models.TextField(verbose_name='Nombre de usuario')
    user_email = models.TextField(verbose_name='Correo electronico')
    register_joined = models.DateField(auto_now=True,verbose_name='Fecha de registro')

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name = 'informacion personal'
        db_table = 'Informacion Personal'
        ordering = ['id']

class editar_usuario(models.Model):
    user_name = models.TextField(verbose_name='Nombre de usuario')
    user_email = models.TextField(verbose_name='Correo electronico')
    user_password = models.TextField(verbose_name='Contraseña')
    user_password2 = models.TextField(verbose_name='Confirmar contraseña')
    security_question = models.TextField(verbose_name='Pregunta de seguridad')
    answer = models.TextField(verbose_name='Respuesta')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'editar usuario'
        db_table = 'Editar Usuario'
        ordering = ['id']

class reportar_error(models.Model):
    user_name = models.TextField(verbose_name='Nombre de usuario')
    user_email = models.TextField(verbose_name='Correo electronico')
    type_error = models.TextField(verbose_name='Tipo de error')
    details_error = models.TextField(verbose_name='Detalles del error')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'reportar error'
        db_table = 'Reportar Error'
        ordering = ['id']

class contactar_desarrolladores(models.Model):
    user_name = models.TextField(verbose_name='Nombre de usuario')
    user_email = models.TextField(verbose_name='Correo electronico')
    affair = models.TextField(verbose_name='Asunto')
    message = models.TextField(verbose_name='Mensaje')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'contactar desarrolladores'
        db_table = 'Contactar Desarrolladores'
        ordering = ['id']






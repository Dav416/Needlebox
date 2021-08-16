# Generated by Django 3.2.4 on 2021-08-16 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegUsu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomComUsu', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('e_mailUsu', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('passwordUsu', models.CharField(max_length=10, verbose_name='Contraseña')),
                ('conf_passwordUsu', models.CharField(max_length=10, verbose_name='Confirmar Contraseña')),
                ('accept_terms', models.BooleanField(default=False, verbose_name='Aceptar términos y condiciones')),
            ],
            options={
                'verbose_name': 'Registrar usuario',
                'verbose_name_plural': 'Registrar Usuarios',
                'ordering': ['id'],
            },
        ),
    ]

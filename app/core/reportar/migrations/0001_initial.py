# Generated by Django 3.2.4 on 2021-08-16 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reportfail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error_nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('correo_usu', models.EmailField(max_length=50, unique=True, verbose_name='Correo electronico')),
                ('tip_error', models.CharField(choices=[('Select_type', 'Seleccione un tipo de error'), ('Leve', 'Error Leve'), ('Moderado', 'Error Moderado'), ('Grave', 'Error Grave')], default='Select_type', max_length=30, verbose_name='Seleccione un tipo de error')),
                ('cont_mensaje', models.TextField(max_length=2000, verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Reportar un error',
                'verbose_name_plural': 'Reportar unos errores',
                'ordering': ['id'],
            },
        ),
    ]
# Generated by Django 3.2.4 on 2021-08-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportfail',
            name='tip_error',
            field=models.CharField(choices=[('Select_type', 'Seleccione un tipo de error'), ('Leve', 'Error Leve'), ('Moderado', 'Error Moderado'), ('Grave', 'Error Grave')], default='Select_type', max_length=30, verbose_name='Seleccione un tipo de error'),
        ),
    ]

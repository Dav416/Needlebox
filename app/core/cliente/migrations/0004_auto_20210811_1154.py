# Generated by Django 3.2.4 on 2021-08-11 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20210810_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoclient',
            name='celCli',
            field=models.IntegerField(default=0, unique=True, verbose_name='celular cliente'),
        ),
        migrations.AlterField(
            model_name='infoclient',
            name='telCli',
            field=models.IntegerField(default=0, unique=True, verbose_name='Teléfono cliente'),
        ),
    ]

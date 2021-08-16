# Generated by Django 3.2.4 on 2021-08-16 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_usu', models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario')),
                ('e_mail', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('password', models.CharField(max_length=50, verbose_name='Contraseña')),
                ('conf_password', models.CharField(max_length=50, verbose_name='Confirmar Contraseña')),
                ('show_password', models.BooleanField(default=False)),
                ('security_question', models.CharField(choices=[('', 'Seleccione una pregunta'), ('Color favorito', 'Color favorito'), ('Comida favorita ', 'Alimento favorito'), ('Mascota de la infancia', 'Mascota de la infancia'), ('Persona admirada', 'Persona admirada'), ('Libro favorito', 'Libro favorito'), ('Canción Favorita', 'Canción favorita')], default='', max_length=30)),
                ('security_answer', models.CharField(max_length=50, verbose_name='Respect')),
                ('accept_terms', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
                'ordering': ['id'],
            },
        ),
    ]
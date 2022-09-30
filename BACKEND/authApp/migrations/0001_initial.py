# Generated by Django 4.1.1 on 2022-09-30 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('primerNombre', models.CharField(max_length=50, verbose_name='PrimerNombre')),
                ('segundoNombre', models.CharField(max_length=50, verbose_name='SegundoNombre')),
                ('primerApellido', models.CharField(max_length=50, verbose_name='PrimerApellido')),
                ('segundoApellido', models.CharField(max_length=50, verbose_name='SegundoApellido')),
                ('celular', models.CharField(max_length=50, verbose_name='Celular')),
                ('pais', models.CharField(max_length=100, verbose_name='Pais')),
                ('departamento', models.CharField(max_length=100, verbose_name='Departamento')),
                ('municipio', models.CharField(max_length=100, verbose_name='Municipio')),
                ('barrio', models.CharField(max_length=256, verbose_name='Barrio')),
                ('direccion', models.CharField(max_length=256, verbose_name='Direccion')),
                ('email', models.EmailField(max_length=250, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idRol', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipoUsuario', models.CharField(max_length=50, verbose_name='tipoUsuario')),
                ('permisos', models.IntegerField(default=0)),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='id_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('especializacion', models.CharField(max_length=100, verbose_name='Especializacion')),
                ('fechaIngreso', models.DateTimeField()),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripcion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

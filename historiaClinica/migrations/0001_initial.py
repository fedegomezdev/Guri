# Generated by Django 2.2.7 on 2019-11-22 15:59

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Categoria')),
                ('fechaCreacion', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha creacion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=55, verbose_name='Nombre del Medico')),
                ('apellido', models.CharField(max_length=55, verbose_name='Apellido del Medico')),
                ('tipoDocumento', models.CharField(blank=True, max_length=20, null=True)),
                ('numeroDoc', models.CharField(max_length=8)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono')),
                ('celular', models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular')),
                ('horaIng', models.DateField(blank=True, null=True)),
                ('horaSalida', models.DateField(blank=True, null=True)),
                ('turnoMax', models.IntegerField(blank=True, null=True)),
                ('fechaCreacion', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha creacion')),
                ('fechaNacimiento', models.DateField(null=True, verbose_name='Fecha nacimiento')),
                ('correo', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('estado', models.BooleanField(default=True)),
                ('fechaBaja', models.DateField(blank=True, null=True)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='historiaClinica.Categoria')),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
            },
        ),
        migrations.CreateModel(
            name='ObraSocial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Obra Social',
                'verbose_name_plural': 'Obras Sociales',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=55, verbose_name='Nombre del Paciente')),
                ('apellido', models.CharField(max_length=55, verbose_name='Apellido del Paciente')),
                ('tipoDocumento', models.CharField(blank=True, max_length=20, null=True)),
                ('numeroDoc', models.CharField(max_length=8)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('fechaCreacion', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha creacion')),
                ('fechaNacimiento', models.DateField(null=True, verbose_name='Fecha nacimiento')),
                ('correo', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('estado', models.BooleanField(default=True)),
                ('fechaBaja', models.DateField(blank=True, null=True)),
                ('obraSocial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='historiaClinica.ObraSocial')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('horario', models.DateField()),
                ('fechaCreacion', models.DateField(default=django.utils.timezone.now)),
                ('medico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='historiaClinica.Medico')),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='historiaClinica.Paciente')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('historial', ckeditor.fields.RichTextField(verbose_name='Historia Clinica')),
                ('fechaCreacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fechaModificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historiaClinica.Paciente')),
            ],
            options={
                'verbose_name': 'Historial',
                'verbose_name_plural': 'Historiales',
            },
        ),
    ]

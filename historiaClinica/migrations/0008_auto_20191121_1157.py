# Generated by Django 2.2.7 on 2019-11-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiaClinica', '0007_paciente_obrasocial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='celular',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='celular',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]

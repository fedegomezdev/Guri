# Generated by Django 2.2.7 on 2019-11-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiaClinica', '0016_auto_20191122_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='tipoDocumento',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tipoDocumento',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
# Generated by Django 2.2.7 on 2019-12-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiaClinica', '0012_auto_20191209_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='horaIng',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='horaSalida',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]

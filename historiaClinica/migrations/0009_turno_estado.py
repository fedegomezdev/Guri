# Generated by Django 2.2.7 on 2019-12-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiaClinica', '0008_turno_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='estado',
            field=models.BooleanField(default=False, verbose_name='Completo/Pendiente'),
        ),
    ]

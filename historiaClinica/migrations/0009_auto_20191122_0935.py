# Generated by Django 2.2.7 on 2019-11-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiaClinica', '0008_auto_20191121_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='fechaBaja',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='fechaBaja',
            field=models.DateField(blank=True, null=True),
        ),
    ]

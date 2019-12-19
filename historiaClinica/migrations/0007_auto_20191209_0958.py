# Generated by Django 2.2.7 on 2019-12-09 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('historiaClinica', '0006_delete_turnos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='medico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='historiaClinica.Medico'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='historiaClinica.Paciente'),
        ),
    ]

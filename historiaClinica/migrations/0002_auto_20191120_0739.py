# Generated by Django 2.2.7 on 2019-11-20 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('historiaClinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='celular',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='turnoMax',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='celular',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('horario', models.DateField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historiaClinica.Medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historiaClinica.Paciente')),
            ],
            options={
                'verbose_name': 'Turno',
                'verbose_name_plural': 'Turnos',
            },
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiaClinica', '0011_auto_20191209_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'ordering': ['-id'], 'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.AddField(
            model_name='turno',
            name='hora',
            field=models.TimeField(null=True),
        ),
    ]

# Generated by Django 2.2.7 on 2019-12-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historiaClinica', '0007_auto_20191209_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]

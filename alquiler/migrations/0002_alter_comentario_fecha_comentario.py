# Generated by Django 5.1.3 on 2024-11-24 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquiler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha_comentario',
            field=models.DateTimeField(),
        ),
    ]

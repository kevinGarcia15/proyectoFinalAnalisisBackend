# Generated by Django 3.2.4 on 2024-11-01 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0005_alter_prueba_fecharegistro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criterioaceptacion',
            name='fechaRegistro',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='logestadoprueba',
            name='fechaRegistro',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

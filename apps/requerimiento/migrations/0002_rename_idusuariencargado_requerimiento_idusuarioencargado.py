# Generated by Django 3.2.4 on 2024-10-27 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requerimiento', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requerimiento',
            old_name='idUsuariEncargado',
            new_name='idUsuarioEncargado',
        ),
    ]

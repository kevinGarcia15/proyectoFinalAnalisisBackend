# Generated by Django 3.2.4 on 2024-10-25 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyecto', '0002_auto_20241022_0357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logestadoproyecto',
            name='usuarioRegistro',
        ),
        migrations.AddField(
            model_name='logestadoproyecto',
            name='idUsuarioRegistro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='logProyecto_registro', to='user.user'),
            preserve_default=False,
        ),
    ]
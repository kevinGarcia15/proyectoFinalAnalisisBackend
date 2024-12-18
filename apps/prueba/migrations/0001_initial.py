# Generated by Django 3.2.4 on 2024-10-31 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proyecto', '0003_auto_20241025_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasoPrueba',
            fields=[
                ('idCasoPrueba', models.AutoField(primary_key=True, serialize=False)),
                ('casoPrueba', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Escenario',
            fields=[
                ('idEscenario', models.AutoField(primary_key=True, serialize=False)),
                ('escenario', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoPrueba',
            fields=[
                ('idEstadoPrueba', models.AutoField(primary_key=True, serialize=False)),
                ('estadoPrueba', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('idPrueba', models.AutoField(primary_key=True, serialize=False)),
                ('prueba', models.CharField(max_length=60)),
                ('descripcion', models.TextField()),
                ('fechaRegistro', models.DateTimeField()),
                ('usuarioRegistro', models.CharField(max_length=20)),
                ('idCasoPrueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.casoprueba')),
                ('idEscenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.escenario')),
                ('idEstadoPrueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.estadoprueba')),
                ('idProyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='LogEstadoPrueba',
            fields=[
                ('idLogEstadoPrueba', models.AutoField(primary_key=True, serialize=False)),
                ('fechaRegistro', models.DateTimeField()),
                ('usuarioRegistro', models.CharField(max_length=20)),
                ('idEstadoPrueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.estadoprueba')),
                ('idPrueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.prueba')),
            ],
        ),
        migrations.CreateModel(
            name='CriterioAceptacion',
            fields=[
                ('idCriterioAceptacion', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('aceptado', models.BooleanField()),
                ('fechaRegistro', models.DateTimeField()),
                ('idPrueba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prueba.prueba')),
            ],
        ),
    ]

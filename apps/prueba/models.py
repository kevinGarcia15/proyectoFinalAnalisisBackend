from django.db import models
from apps.proyecto.models import Proyecto
from django.contrib.auth import get_user_model

class EstadoPrueba(models.Model):
    idEstadoPrueba = models.AutoField(primary_key=True)
    estadoPrueba = models.CharField(max_length=45)

    def __str__(self):
        return self.estadoPrueba

class Prueba(models.Model):
    idPrueba = models.AutoField(primary_key=True)
    prueba = models.CharField(max_length=60)
    descripcion = models.TextField()
    escenarioPrueba = models.TextField()
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    idUsuarioRegistro = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='prueba_registro')
    idProyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    idEstadoPrueba = models.ForeignKey(EstadoPrueba, on_delete=models.CASCADE)

    def __str__(self):
        return self.prueba

class CriterioAceptacion(models.Model):
    idCriterioAceptacion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=200)
    aceptado = models.BooleanField()
    fechaRegistro = models.DateTimeField()
    idPrueba = models.ForeignKey(Prueba, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion

class LogEstadoPrueba(models.Model):
    idLogEstadoPrueba = models.AutoField(primary_key=True)
    fechaRegistro = models.DateTimeField()
    idUsuarioRegistro = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='logprueba_registro')
    idEstadoPrueba = models.ForeignKey(EstadoPrueba, on_delete=models.CASCADE)
    idPrueba = models.ForeignKey(Prueba, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.idLogEstadoPrueba} - {self.idPrueba}"

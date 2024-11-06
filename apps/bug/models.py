from django.db import models
from django.contrib.auth import get_user_model
from apps.prueba.models import Prueba

class Clasificacion(models.Model):
    idClasificacion = models.AutoField(primary_key=True)
    clasificacion = models.CharField(max_length=45)

    def __str__(self):
        return self.clasificacion

class EstadoBug(models.Model):
    idEstadoBug = models.AutoField(primary_key=True)
    estadoBug = models.CharField(max_length=45)

    def __str__(self):
        return self.estadoBug

class Bug(models.Model):
    idBug = models.AutoField(primary_key=True)
    bug = models.CharField(max_length=60)
    idUsuarioEncargado = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='bug_encargado')
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    fechaResolucion = models.DateTimeField(null=True, blank=True)
    idUsuarioRegistro = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='bug_registro')
    idEstadoBug = models.ForeignKey(EstadoBug, on_delete=models.CASCADE, related_name='bugs')
    idPrueba = models.ForeignKey(Prueba, on_delete=models.CASCADE)
    idClasificacion = models.ForeignKey(Clasificacion, on_delete=models.CASCADE, related_name='bugs')

    def __str__(self):
        return self.bug

class LogEstadoBug(models.Model):
    idLogEstadoBug = models.AutoField(primary_key=True)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    idUsuarioRegistro = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='log_usaurioRegsitro')
    comentario = models.TextField()
    idBug = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name='logsBug')
    idEstadoBug = models.ForeignKey(EstadoBug, on_delete=models.CASCADE, related_name='logsEstado')

    def __str__(self):
        return f"Log {self.idLogEstadoBug} for Bug {self.idBug.idBug}"

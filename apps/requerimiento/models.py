from django.db import models
from django.contrib.auth import get_user_model
from apps.proyecto.models import Proyecto

class EstadoRequerimiento(models.Model):
    idEstadoRequerimiento = models.AutoField(primary_key=True)
    estadoRequerimiento = models.CharField(max_length=45)

    def __str__(self):
        return self.estadoRequerimiento


class Requerimiento(models.Model):
    idRequerimiento = models.AutoField(primary_key=True)
    requerimiento = models.CharField(max_length=150)
    orden = models.IntegerField()
    fechaEstimadoEntrega = models.DateField()
    fechaInicioPropuesto = models.DateField()
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    idEstadoRequerimiento = models.ForeignKey(EstadoRequerimiento, on_delete=models.CASCADE)

    idUsuarioEncargado = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='requerimiento_encargado')
    idUsuarioRegistro = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='requerimiento_registro')
    idProyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.requerimiento

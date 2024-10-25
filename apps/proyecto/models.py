from django.db import models
from django.contrib.auth import get_user_model

class Prioridad(models.Model):
    idPrioridad = models.AutoField(primary_key=True)
    prioridad = models.CharField(max_length=20)

    def __str__(self):
        return self.prioridad

class Complejidad(models.Model):
    idComplejidad = models.AutoField(primary_key=True)
    complejidad = models.CharField(max_length=20)
    

    def __str__(self):
        return self.complejidad

class TipoRequerimiento(models.Model):
    idTipoRequerimiento = models.AutoField(primary_key=True)
    tipoRequerimiento = models.CharField(max_length=60)

    def __str__(self):
        return self.tipoRequerimiento

class EstadoProyecto(models.Model):
    idEstadoProyecto = models.AutoField(primary_key=True)
    estadoProyecto = models.CharField(max_length=45)

    def __str__(self):
        return self.estadoProyecto

class Proyecto(models.Model):
    idProyecto = models.AutoField(primary_key=True)
    fechaRequerimiento = models.DateField()
    nombreProyecto = models.CharField(max_length=60)
    descripcion = models.TextField()
    fechaEstimadoInicio = models.DateField()
    planificado = models.BooleanField()
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    
    # Relaciones con otras tablas
    idUsuariEncargado = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='proyecto_encargado')
    idUsuarioRegistro = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='proyecto_registro')
    idPrioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)
    idComplejidad = models.ForeignKey(Complejidad, on_delete=models.CASCADE)
    idTipoRequerimiento = models.ForeignKey(TipoRequerimiento, on_delete=models.CASCADE)
    idEstadoProyecto = models.ForeignKey(EstadoProyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProyecto

class LogEstadoProyecto(models.Model):
    idLogEstadoProyecto = models.AutoField(primary_key=True)
    fechaRegistro = models.DateField()
    
    # Relaciones con otras tablas
    idUsuarioRegistro = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='logProyecto_registro')
    idProyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    idEstadoProyecto = models.ForeignKey(EstadoProyecto, on_delete=models.CASCADE)

class Recurso(models.Model):
    idRecurso = models.AutoField(primary_key=True)
    recurso = models.CharField(max_length=45)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Relación con proyecto
    idProyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.recurso

from rest_framework import serializers
from .models import Requerimiento, EstadoRequerimiento

class EstadoRequerimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoRequerimiento
        fields = ['estadoRequerimiento']

class RequerimientoSerializer(serializers.ModelSerializer):
    estadoRequerimiento = EstadoRequerimientoSerializer(read_only=True, source='idEstadoRequerimiento')  # Serializador anidado para estado

    class Meta:
        model = Requerimiento
        fields = [
            'idRequerimiento',
            'requerimiento',
            'orden',
            'fechaEstimadoEntrega',
            'fechaInicioPropuesto',
            'idUsuarioEncargado',
            'idUsuarioRegistro',
            'idEstadoRequerimiento',
            'estadoRequerimiento',
            'idProyecto',
        ]
        read_only_fields = ['idRequerimiento', 'fechaRegistro']
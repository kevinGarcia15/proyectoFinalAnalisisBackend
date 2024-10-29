from rest_framework import serializers
from .models import Requerimiento, EstadoRequerimiento
from apps.user.serializers import CustomUserSerializer
from apps.proyecto.serializers import ProyectoSerializer

class EstadoRequerimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoRequerimiento
        fields = ['idEstadoRequerimiento','estadoRequerimiento']

class RequerimientoSerializer(serializers.ModelSerializer):
    estadoRequerimiento = EstadoRequerimientoSerializer(read_only=True, source='idEstadoRequerimiento')  # Serializador anidado para estado
    usuarioEncargado = CustomUserSerializer(read_only=True, source='idUsuarioEncargado')
    proyecto = ProyectoSerializer(read_only=True, source='idProyecto')

    class Meta:
        model = Requerimiento
        fields = [
            'idRequerimiento',
            'requerimiento',
            'orden',
            'fechaEstimadoEntrega',
            'fechaInicioPropuesto',
            'idUsuarioEncargado',
            'usuarioEncargado',
            'idUsuarioRegistro',
            'idEstadoRequerimiento',
            'estadoRequerimiento',
            'idProyecto',
            'proyecto',
        ]
        read_only_fields = ['idRequerimiento', 'fechaRegistro']
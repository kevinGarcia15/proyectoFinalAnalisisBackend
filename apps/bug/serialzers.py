from rest_framework import serializers
from .models import Clasificacion, EstadoBug, Bug, LogEstadoBug
from apps.user.serializers import CustomUserSerializer


class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        fields = '__all__'

class EstadoBugSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoBug
        fields = '__all__'

class BugSerializer(serializers.ModelSerializer):
    estadoBug = EstadoBugSerializer(read_only=True, source='idEstadoBug')
    clasificacion = ClasificacionSerializer(read_only=True, source='idClasificacion')
    usuarioEncargado = CustomUserSerializer(read_only=True, source='idUsuarioEncargado')

    class Meta:
        model = Bug
        fields = '__all__'
        read_only_fields = ['idBug', 'fechaRegistro']

class LogEstadoBugSerializer(serializers.ModelSerializer):
    idBug = BugSerializer(read_only=True)
    idEstadoBug = EstadoBugSerializer(read_only=True)

    class Meta:
        model = LogEstadoBug
        fields = '__all__'

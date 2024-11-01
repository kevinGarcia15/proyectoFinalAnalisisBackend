from rest_framework import serializers
from .models import EstadoPrueba, Prueba, CriterioAceptacion, LogEstadoPrueba
from apps.proyecto.serializers import ProyectoSerializer
from apps.user.serializers import CustomUserSerializer

class EstadoPruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPrueba
        fields = '__all__'

class PruebaSerializer(serializers.ModelSerializer):
    proyecto = ProyectoSerializer(read_only=True, source='idProyecto')
    estado = EstadoPruebaSerializer(read_only=True, source='idEstadoPrueba')
    usuarioRegistro = CustomUserSerializer(read_only=True, source='idUsuarioRegistro')

    class Meta:
        model = Prueba
        fields = '__all__'
        read_only_fields = ['fechaRegistro']

class CriterioAceptacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CriterioAceptacion
        fields = '__all__'

class LogEstadoPruebaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEstadoPrueba
        fields = '__all__'

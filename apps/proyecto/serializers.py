from rest_framework import serializers
from .models import Proyecto, Prioridad, Complejidad, TipoRequerimiento, EstadoProyecto

class ProyectoSerializer(serializers.ModelSerializer):
    """ proyecto Document Serializer """
    class Meta:
        model = Proyecto
        fields = '__all__'
        read_only_fields = ['idProyecto', 'fechaRegistro']
        


    def create(self, validated_data):
        """ Create proyecto Document """
        return Proyecto.objects.create(**validated_data)
    
class PrioridadSerializer(serializers.ModelSerializer):
    """ proyecto Document Serializer """
    class Meta:
        model = Prioridad
        fields = '__all__'

class ComplejidadSerializer(serializers.ModelSerializer):
    """ complejidad Document Serializer """
    class Meta:
        model = Complejidad
        fields = '__all__'

class TipoRequerimientoSerializer(serializers.ModelSerializer):
    """ TipoRequerimiento Document Serializer """
    class Meta:
        model = TipoRequerimiento
        fields = '__all__'


class EstadoProyectoSerializer(serializers.ModelSerializer):
    """ EstadoProyecto Document Serializer """
    class Meta:
        model = EstadoProyecto
        fields = '__all__'
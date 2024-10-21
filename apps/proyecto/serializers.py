from rest_framework import serializers
from .models import Proyecto, Prioridad, Complejidad, TipoRequerimiento, EstadoProyecto

class ProyectoSerializer(serializers.ModelSerializer):
    """ proyecto Document Serializer """
    class Meta:
        model = Proyecto
        fields = '__all__'
        read_only_fields = ['idProyecto', 'fechaRegistro', 'usuarioRegistro']


    def create(self, validated_data):
        """ Create proyecto Document """
        return Proyecto.objects.create(**validated_data)
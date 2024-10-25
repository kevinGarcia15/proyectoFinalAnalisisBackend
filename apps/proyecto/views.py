from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from django.shortcuts import render
from django.db import transaction
from rest_framework.permissions import AllowAny, IsAuthenticated

""" SERIALIZERS """
from .serializers import  ProyectoSerializer, PrioridadSerializer, ComplejidadSerializer, TipoRequerimientoSerializer, EstadoProyectoSerializer
from apps.user.serializers import UserSerializer

""" MODELS """
from .models import Proyecto, Prioridad, Complejidad, TipoRequerimiento, EstadoProyecto
from apps.user.models import User

class ProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer
    queryset = Proyecto.objects.all()
    
    def get_permissions(self):
        """" Define permisos para este recurso """
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


    def create(self, request, *args, **kwargs):
        # Sobrescribimos el comportamiento para añadir el usuario responsable
        data = request.data.copy()  # Hacemos una copia del request data
        data['idUsuarioRegistro'] = request.user.id  # Asignamos el usuario que hace la petición
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        proyecto = self.get_object()  # Obtiene el proyecto a eliminar

        # Lógica personalizada antes de eliminar
        if proyecto.idEstadoProyecto_id == 6:  # Ejemplo: no permitir eliminar proyectos completados
            return Response({'detail': 'No puedes eliminar proyectos completados.'}, status=status.HTTP_400_BAD_REQUEST)

        # Si pasa las validaciones, procede con la eliminación
        self.perform_destroy(proyecto)
        return Response({"message": "Proyecto eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
    
"""    def delete(self, request, id):
        print(id)
        try:
            proyecto = Proyecto.objects.get(id=id)
        except Proyecto.DoesNotExist:
            return Response({"message": "Proyecto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProyectoSerializer(proyecto, data=99, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Proyecto eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

class PrioridadViewSet(viewsets.ModelViewSet):
    serializer_class = PrioridadSerializer
    queryset = Prioridad.objects.all()
    
    def get_permissions(self):
        """" Define permisos para este recurso """
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class ComplejidadViewSet(viewsets.ModelViewSet):
    serializer_class = ComplejidadSerializer
    queryset = Complejidad.objects.all()
    
    def get_permissions(self):
        """" Define permisos para este recurso """
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
class TipoRequerimientoViewSet(viewsets.ModelViewSet):
    serializer_class = TipoRequerimientoSerializer
    queryset = TipoRequerimiento.objects.all()
    
    def get_permissions(self):
        """" Define permisos para este recurso """
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
class EstadoProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = EstadoProyectoSerializer
    queryset = EstadoProyecto.objects.all()
    
    def get_permissions(self):
        """" Define permisos para este recurso """
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
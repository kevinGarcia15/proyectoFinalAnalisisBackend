from rest_framework import viewsets, status
from .models import EstadoPrueba, Prueba, CriterioAceptacion, LogEstadoPrueba
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    EstadoPruebaSerializer,
    PruebaSerializer, CriterioAceptacionSerializer, LogEstadoPruebaSerializer
)

class EstadoPruebaViewSet(viewsets.ModelViewSet):
    queryset = EstadoPrueba.objects.all()
    serializer_class = EstadoPruebaSerializer

class PruebaViewSet(viewsets.ModelViewSet):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer

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

class CriterioAceptacionViewSet(viewsets.ModelViewSet):
    queryset = CriterioAceptacion.objects.all()
    serializer_class = CriterioAceptacionSerializer
    
    def create(self, request, *args, **kwargs):
        # Sobrescribimos el comportamiento para añadir el usuario responsable
        data = request.data.copy()  # Hacemos una copia del request data
        data['aceptado'] = 0  # Asignamos el usuario que hace la petición

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        idPrueba = self.request.query_params.get('idprueba')

        # Si se proporciona un id de proyecto, filtramos por él
        if idPrueba:
            queryset = queryset.filter(idPrueba=idPrueba)
        return queryset

class LogEstadoPruebaViewSet(viewsets.ModelViewSet):
    queryset = LogEstadoPrueba.objects.all()
    serializer_class = LogEstadoPruebaSerializer

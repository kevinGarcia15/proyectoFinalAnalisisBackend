from rest_framework import viewsets, status
from .models import Clasificacion, EstadoBug, Bug, LogEstadoBug
from .serialzers import ClasificacionSerializer, EstadoBugSerializer, BugSerializer, LogEstadoBugSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils.timezone import now

class ClasificacionViewSet(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer

class EstadoBugViewSet(viewsets.ModelViewSet):
    queryset = EstadoBug.objects.all()
    serializer_class = EstadoBugSerializer

class BugViewSet(viewsets.ModelViewSet):
    queryset = Bug.objects.all()
    serializer_class = BugSerializer

    def get_permissions(self):
        """ Define permisos para este recurso """
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
    
    def get_queryset(self):
        queryset = super().get_queryset()
        idPrueba = self.request.query_params.get('idprueba')

        # Si se proporciona un id de prueba, filtramos por él
        if idPrueba:
            queryset = queryset.filter(idPrueba=idPrueba)
        return queryset

    def update(self, request, *args, **kwargs):
        bug = self.get_object()

        # Verificar si el usuario autenticado es el responsable del bug
        if bug.idUsuarioEncargado != request.user:
            return Response(
                {"detail": "No tienes permiso para cambiar el estado de este bug."},
                status=status.HTTP_403_FORBIDDEN
            )

        # Actualizar la fecha de resolución si el estado es 3
        if request.data.get('idEstadoBug') == 3:
            bug.fechaResolucion = now()
        else:
            bug.fechaResolucion = None

        serializer = self.get_serializer(bug, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class LogEstadoBugViewSet(viewsets.ModelViewSet):
    queryset = LogEstadoBug.objects.all()
    serializer_class = LogEstadoBugSerializer

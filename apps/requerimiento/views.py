from rest_framework import viewsets, status
from .models import Requerimiento, EstadoRequerimiento
from .serializers import RequerimientoSerializer, EstadoRequerimientoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters  import OrderingFilter


class EstadoRequerimientoViewSet(viewsets.ModelViewSet):
    queryset = EstadoRequerimiento.objects.all()
    serializer_class = EstadoRequerimientoSerializer

class RequerimientoViewSet(viewsets.ModelViewSet):
    queryset = Requerimiento.objects.all()
    serializer_class = RequerimientoSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        proyecto_id = self.request.query_params.get('idProyecto')

        # Si se proporciona un id de proyecto, filtramos por él
        if proyecto_id:
            queryset = queryset.filter(idProyecto=proyecto_id)
        return queryset
    
    def get_permissions(self):
        """" Define permisos para este recurso """
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        # Sobrescribimos el comportamiento para añadir el usuario responsable
        data = request.data.copy()  # Hacemos una copia del request data
        data['idUsuarioRegistro'] = request.user.id  # Asignamos el usuario que hace la petición
        data['idEstadoRequerimiento'] = request.data['idEstadoRequerimiento']

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
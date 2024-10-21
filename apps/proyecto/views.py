from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from django.shortcuts import render
from django.db import transaction
from rest_framework.permissions import AllowAny, IsAuthenticated

""" SERIALIZERS """
from .serializers import  ProyectoSerializer
from apps.user.serializers import UserSerializer

""" MODELS """
from .models import Proyecto
from apps.user.models import User

class ProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer
    queryset = Proyecto.objects.all()
    
    def get_permissions(self):
        """" Define permisos para este recurso """
        permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
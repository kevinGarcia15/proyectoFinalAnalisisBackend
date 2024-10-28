from django.urls import path, include
from . import views
from apps.requerimiento import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'requerimientos', views.RequerimientoViewSet, basename='requerimientos')
router.register(r'estadorequerimiento', views.EstadoRequerimientoViewSet, basename='estadorequerimiento')

urlpatterns = [
    path('', include(router.urls)),
]

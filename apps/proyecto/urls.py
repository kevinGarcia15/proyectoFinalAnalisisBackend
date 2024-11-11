from django.urls import path, include

""" views """
from . import views
from apps.proyecto import views
from apps.proyecto.views import ReporteViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'proyecto', views.ProyectoViewSet, basename = 'proyecto')
router.register(r'prioridad', views.PrioridadViewSet, basename = 'prioridad')
router.register(r'complejidad', views.ComplejidadViewSet, basename = 'complejidad')
router.register(r'tiporequerimiento', views.TipoRequerimientoViewSet, basename = 'tiporequerimiento')
router.register(r'estadoproyecto', views.EstadoProyectoViewSet, basename = 'estadoproyecto')
router.register(r'reportes', ReporteViewSet, basename='reportes')

urlpatterns = [
    path('', include(router.urls)),

]
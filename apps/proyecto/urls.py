from django.urls import path, include

""" views """
from . import views
from apps.proyecto import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'proyecto', views.ProyectoViewSet, basename = 'proyecto')

urlpatterns = [
    path('', include(router.urls)),
]
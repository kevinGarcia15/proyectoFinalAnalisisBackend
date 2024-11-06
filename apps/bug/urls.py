from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clasificaciones', views.ClasificacionViewSet)
router.register(r'estadosbug', views.EstadoBugViewSet)
router.register(r'bugs', views.BugViewSet)
router.register(r'logsbug', views.LogEstadoBugViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

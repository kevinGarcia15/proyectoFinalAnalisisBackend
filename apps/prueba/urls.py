from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EstadoPruebaViewSet,
    PruebaViewSet, CriterioAceptacionViewSet, LogEstadoPruebaViewSet
)

router = DefaultRouter()
router.register(r'estadoprueba', EstadoPruebaViewSet)
router.register(r'prueba', PruebaViewSet)
router.register(r'criterioaceptacion', CriterioAceptacionViewSet)
router.register(r'log-estado-prueba', LogEstadoPruebaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

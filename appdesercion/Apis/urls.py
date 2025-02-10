from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appdesercion.Apis.views.modulo_view import ModuloViewSet

router = DefaultRouter()
router.register(r'modulos', ModuloViewSet, basename='modulo')

urlpatterns = [
    path('', include(router.urls)),  # Esto genera automáticamente las rutas CRUD
]

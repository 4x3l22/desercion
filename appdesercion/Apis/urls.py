from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appdesercion.Apis.views.modulo_view import CuestionarioViewSet, DesercionesViewSet, LoginView, ModuloViewSet, PersonaViewSet, PreguntasViewSet, ProcesoViewSet, RespuestasViewSet, RolViewSet, RolVistaViewSet, UsuarioRolViewSet, UsuarioViewSet, VistaViewSet

router = DefaultRouter()
router.register(r'modulos', ModuloViewSet, basename='modulo')
router.register(r'vistas', VistaViewSet, basename='vista')
router.register(r'rolvista', RolVistaViewSet, basename='rolvista')
router.register(r'rol', RolViewSet, basename='rol')
router.register(r'usuariorol', UsuarioRolViewSet, basename='usuariorol')
router.register(r'usuario', UsuarioViewSet, basename='usuario')
router.register(r'persona', PersonaViewSet, basename='persona')
# router.register(r'recuperarcontrasena', RecuperarContrasenaViewSet, basename='recuperarcontrasena')
router.register(r'cuestionario', CuestionarioViewSet, basename='cuestionario')
router.register(r'preguntas', PreguntasViewSet, basename='preguntas')
router.register(r'respuestas', RespuestasViewSet, basename='respuestas')
router.register(r'proceso', ProcesoViewSet, basename='proceso')
router.register(r'deserciones', DesercionesViewSet, basename='deserciones')
# router.register(r'login', LoginView, basename='login')

urlpatterns = [
    path('', include(router.urls)),  # Esto genera automáticamente las rutas CRUD
    path('login/', LoginView.as_view(), name='login'),  # Ruta personalizada para el login
]

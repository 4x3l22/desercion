from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from appdesercion.Apis.views.modulo_view import CuestionarioViewSet, DesercionesViewSet, ModuloViewSet, PersonaViewSet, PreguntasViewSet, ProcesoViewSet, RespuestasViewSet, RolViewSet, RolVistaViewSet, SolicitarRecuperacionView, UsuarioRolViewSet, UsuarioViewSet, VistaViewSet
=======
from appdesercion.Apis.views.modulo_view import CuestionarioViewSet, DesercionesViewSet, LoginView, ModuloViewSet, PreguntasViewSet, ProcesoViewSet, RecuperarContrasenaViewSet, RespuestasViewSet, RolViewSet, RolVistaViewSet, UsuarioRolViewSet, UsuarioViewSet, VistaViewSet
>>>>>>> d51a7b93d2ee2a2a1229fedb9851238f7c37f52b

router = DefaultRouter()
router.register(r'modulos', ModuloViewSet, basename='modulo')
router.register(r'vistas', VistaViewSet, basename='vista')
router.register(r'rolvista', RolVistaViewSet, basename='rolvista')
router.register(r'rol', RolViewSet, basename='rol')
router.register(r'usuariorol', UsuarioRolViewSet, basename='usuariorol')
router.register(r'usuario', UsuarioViewSet, basename='usuario')
router.register(r'recuperarcontrasena', RecuperarContrasenaViewSet, basename='recuperarcontrasena')
router.register(r'cuestionario', CuestionarioViewSet, basename='cuestionario')
router.register(r'preguntas', PreguntasViewSet, basename='preguntas')
router.register(r'respuestas', RespuestasViewSet, basename='respuestas')
router.register(r'proceso', ProcesoViewSet, basename='proceso')
router.register(r'deserciones', DesercionesViewSet, basename='deserciones')

urlpatterns = [
        path('solicitar-recuperacion/', SolicitarRecuperacionView.as_view(), name='solicitar-recuperacion'),
    path('', include(router.urls)),  # Esto genera automáticamente las rutas CRUD
    path('login/', LoginView.as_view(), name='login'),  # Ruta personalizada para el login
]

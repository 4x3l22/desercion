from django.urls import path, include
from rest_framework.routers import DefaultRouter
from appdesercion.Apis.views.viewSet import CuestionarioViewSet, DesercionesViewSet, LoginView, ModuloViewSet, \
    ProcesoViewSet, RecuperarContrasenaViewSet, RespuestasViewSet, RolViewSet, RolVistaViewSet, \
    UsuarioRolViewSet, UsuarioViewSet, VistaViewSet, AprendizViewSet, ComentarioViewSet, PreguntaViewSet

router = DefaultRouter()
router.register(r'modulos', ModuloViewSet, basename='modulo')
router.register(r'vistas', VistaViewSet, basename='vista')
router.register(r'rolvista', RolVistaViewSet, basename='rolvista')
router.register(r'rol', RolViewSet, basename='rol')
router.register(r'usuariorol', UsuarioRolViewSet, basename='usuariorol')
router.register(r'usuario', UsuarioViewSet, basename='usuario')
router.register(r'recuperarcontrasena', RecuperarContrasenaViewSet, basename='recuperarcontrasena')
router.register(r'cuestionario', CuestionarioViewSet, basename='cuestionario')
router.register(r'aprendiz', AprendizViewSet, basename='aprendiz')
router.register(r'respuestas', RespuestasViewSet, basename='respuestas')
router.register(r'proceso', ProcesoViewSet, basename='proceso')
router.register(r'deserciones', DesercionesViewSet, basename='deserciones')
router.register(r'comentarios', ComentarioViewSet, basename='comentarios')
router.register(r'pregunta', PreguntaViewSet, basename='pregunta')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
]

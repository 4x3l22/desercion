from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.utils import timezone  # ✅ Importar timezone correctamente
from appdesercion.Business.usuario_service import UsuarioService
from appdesercion.models import Cuestionario, Deserciones, Modulo, Preguntas, Proceso, RecuperarContrasena, Respuestas, Rol, RolVista, Usuario, UsuarioRol, Vista  # ✅ Importar solo lo necesario
from appdesercion.Apis.serializers.modulo_serializer import CuestionarioSerializers, DesercionesSerializer, ModuloSerializer, PreguntasSerializer, ProcesoSerializer, RecuperarContrasenaSerializer, RespuestasSerializer, RolSerializer, RolVistaSerializer, UsuarioLoginSerializer, UsuarioRolSerializer, UsuarioSerializer, VistaSerializer  # ✅ Importar explícitamente

class ModuloViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet en VistaViewSet
    queryset = Modulo.objects.filter(estado=True)  # Filtra solo los activos
    serializer_class = ModuloSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Módulo eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

class VistaViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Vista.objects.filter(estado=True)
    serializer_class = VistaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Vista eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido

class RolVistaViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = RolVista.objects.filter(estado=True)
    serializer_class = RolVistaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Rol vista eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class RolViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Rol.objects.filter(estado=True)
    serializer_class = RolSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Rol eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class UsuarioViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Usuario.objects.filter(estado=True)
    serializer_class = UsuarioSerializer

    def create(self, request, *args, **kwargs):
        """Sobrescribe el método create para usar UsuarioService."""
        data = request.data
        usuario = UsuarioService.crear(
            correo=data.get("correo"),
            contrasena=data.get("contrasena"),
            estado=data.get("estado", True), # ✅ Valor predeterminado para estado
        )
        serializer = self.get_serializer(usuario)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Usuario eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    

    
class UsuarioRolViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = UsuarioRol.objects.filter(estado=True)
    serializer_class = UsuarioRolSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Usuario Rol eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class CuestionarioViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Cuestionario.objects.filter(estado=True)
    serializer_class = CuestionarioSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Cuestionario eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class PreguntasViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Preguntas.objects.filter(estado=True)
    serializer_class = PreguntasSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Preguntas eliminadas correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class RespuestasViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Respuestas.objects.filter(estado=True)
    serializer_class = RespuestasSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Respuestas eliminadas correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class ProcesoViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Proceso.objects.filter(estado=True)
    serializer_class = ProcesoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Proceso eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class DesercionesViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Deserciones.objects.filter(estado=True)
    serializer_class = DesercionesSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Deserciones eliminadas correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class LoginView(APIView):

    @swagger_auto_schema(
        request_body=UsuarioLoginSerializer, 
        responses={200: "Login exitoso", 400: "Credenciales inválidas"}
    )
    
    def post(self, request):
        serializer = UsuarioLoginSerializer(data=request.data)

        if serializer.is_valid():
            correo = serializer.validated_data["correo"]
            contrasena = serializer.validated_data["contrasena"]
            
            usuario = UsuarioService.autenticar_usuario(correo, contrasena)
            
            if usuario:
                return Response(usuario, status=status.HTTP_200_OK)
            return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

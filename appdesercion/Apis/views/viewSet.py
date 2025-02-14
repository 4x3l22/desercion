from rest_framework.decorators import action 
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.utils import timezone  # ✅ Importar timezone correctamente
from appdesercion.Business.recuperarContrasena_service import RecuperarContrasenaService
from appdesercion.Business.usuario_service import UsuarioService
from appdesercion.models import Cuestionario, Deserciones, Modulo, Proceso, RecuperarContrasena, Respuestas, Rol, \
    RolVista, Usuario, UsuarioRol, Vista, Aprendiz, Comentario  # ✅ Importar solo lo necesario
from appdesercion.Apis.serializers.serializer import CuestionarioSerializers, DesercionesSerializer, \
    EnviarCodigoSerializer, ModuloSerializer, ProcesoSerializer, RecuperarContrasenaSerializer, \
    RespuestasSerializer, RolSerializer, RolVistaSerializer, UsuarioLoginSerializer, UsuarioRolSerializer, \
    UsuarioSerializer, VerificarCodigoSerializer, VistaSerializer, AprendizSerializer, \
    ComentarioSerializer  # ✅ Importar explícitamente

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
            nombres=data.get("nombres"),
            apellidos=data.get("apellidos"),
            documento=data.get("documento"),
            contrasena=data.get("contrasena"),
            estado=data.get("estado", True),
        )
        serializer = self.get_serializer(usuario)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data

        usuario_actualizado = UsuarioService.actualizar(
            instance.id,
            correo=data.get("correo", instance.correo),
            contrasena=data.get("contrasena") if "contrasena" in data else None,
            estado=data.get("estado", instance.estado)
        )

        if usuario_actualizado:
            serializer = self.get_serializer(usuario_actualizado)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"error": "No se pudo actualizar el usuario."}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Usuario eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    

    
class UsuarioRolViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = UsuarioRol.objects.filter(fechaElimino__isnull=True)
    serializer_class = UsuarioRolSerializer

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.fechaElimino = timezone.now()
    #     instance.save()
    #     return Response({"message": "Usuario Rol eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
        
class RecuperarContrasenaViewSet(viewsets.GenericViewSet):  # ✅ Cambiado ModelViewSet
    queryset = RecuperarContrasena.objects.filter(usado=True)
    serializer_class = RecuperarContrasenaSerializer
    
    @swagger_auto_schema(
        request_body=EnviarCodigoSerializer, 
        responses={200: "Codigo enviado", 400: "Correo inválido"}
    )
    
    @action(detail=False, methods=["post"], url_path="enviar-codigo", url_name="enviar_codigo")
    def enviar_codigo(self, request):
        serializer = EnviarCodigoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        correo = request.data.get("correo")
        if not correo:  
            return Response({"error": "El correo es obligatorio"}, status=status.HTTP_400_BAD_REQUEST)

        resultado = RecuperarContrasenaService.EnviarCodigo(correo)

        if isinstance(resultado, str): 
            return Response({"error": resultado}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Código enviado correctamente", "codigo": resultado.codigo}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=VerificarCodigoSerializer, 
        responses={200: "Código verificado", 400: "Código inválido"}
    )
    
    @action(detail=False, methods=["post"], url_path="verificar-codigo", url_name="verificar_codigo")
    def verificar_codigo(self, request):
        serializer = VerificarCodigoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        codigo = request.data.get("codigo")
        usuario_id = request.data.get("usuario_id")
        if not codigo or not usuario_id:
            return Response({"error": "El código y el usuario son obligatorios"}, status=status.HTTP_400_BAD_REQUEST)

        resultado = RecuperarContrasenaService.VerificarCodigo(codigo, usuario_id)

        if isinstance(resultado, str):
            return Response({"error": resultado}, status=status.HTTP_404_NOT_FOUND)

        return Response({"message": "Código verificado correctamente"}, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Vista eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class CuestionarioViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Cuestionario.objects.filter(estado=True)
    serializer_class = CuestionarioSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Cuestionario eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
class AprendizViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Aprendiz.objects.filter(fechaElimino__isnull=True)
    serializer_class = AprendizSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Aprendiz eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
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
    queryset = Proceso.objects.filter(fechaElimino__isnull=True)
    serializer_class = ProcesoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
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

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.filter(fechaElimino__isnull=True)
    serializer_class = ComentarioSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Comentario Eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
class LoginView(APIView):

    @swagger_auto_schema(
        request_body=UsuarioLoginSerializer,
        responses={200: "Login exitoso", 400: "Credenciales inválidas", 403: "Usuario sin rol asignado"}
    )
    def post(self, request):
        serializer = UsuarioLoginSerializer(data=request.data)

        if serializer.is_valid():
            correo = serializer.validated_data["correo"]
            contrasena = serializer.validated_data["contrasena"]

            usuario = UsuarioService.autenticar_usuario(correo, contrasena)

            if usuario:
                if not usuario.get("rol_id"):
                    return Response({"error": "Usuario sin rol asignado"}, status=status.HTTP_403_FORBIDDEN)

                return Response(usuario, status=status.HTTP_200_OK)

            return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
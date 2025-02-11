from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone  # ✅ Importar timezone correctamente
from appdesercion.models import Cuestionario, Deserciones, Modulo, Persona, Preguntas, Proceso, RecuperarContrasena, Respuestas, Rol, RolVista, Usuario, UsuarioRol, Vista  # ✅ Importar solo lo necesario
from appdesercion.Apis.serializers.modulo_serializer import CuestionarioSerializers, DesercionesSerializer, ModuloSerializer, PersonaSerializer, PreguntasSerializer, ProcesoSerializer, RecuperarContrasenaSerializer, RespuestasSerializer, RolSerializer, RolVistaSerializer, UsuarioRolSerializer, UsuarioSerializer, VistaSerializer  # ✅ Importar explícitamente

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
    
class PersonaViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
    queryset = Persona.objects.filter(estado=True)
    serializer_class = PersonaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Persona eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
# class RecuperarContrasenaViewSet(viewsets.ModelViewSet):  # ✅ Cambiado ModelViewSet
#     queryset = RecuperarContrasena.objects.filter(estado=True)
#     serializer_class = RecuperarContrasenaSerializer

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.estado = False
#         instance.fechaElimino = timezone.now()
#         instance.save()
#         return Response({"message": "Vista eliminada correctamente"}, status=status.HTTP_204_NO_CONTENT)  # ✅ Mensaje corregido
    
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
from rest_framework import serializers
from appdesercion.models import *

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rol
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class RolVistaSerializer(serializers.ModelSerializer):
    class Meta:
        model= RolVista
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model= UsuarioRol
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class VistaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vista
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class RecuperarContrasenaSerializer(serializers.ModelSerializer):
    class Meta:
        model= RecuperarContrasena
        fields= '__all__'

class CuestionarioSerializers(serializers.ModelSerializer):
    class Meta:
        model= Cuestionario
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class AprendizSerializer(serializers.ModelSerializer):
    class Meta:
        model= Aprendiz
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class RespuestasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Respuesta
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Proceso
        fields='__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class DesercionesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Deserciones
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Pregunta
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class UsuarioLoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    contrasena = serializers.CharField(write_only=True)
    
class EnviarCodigoSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    
class VerificarCodigoSerializer(serializers.Serializer):
    codigo = serializers.CharField(max_length=10)
    usuario_id = serializers.IntegerField()

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comentario
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model= TipoDocumento
        fields= '__all__'
        extra_kwargs = {
            'fechaElimino': {'read_only': True}
        }
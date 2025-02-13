from rest_framework import serializers
from appdesercion.models import *

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rol
        fields= '__all__'

class RolVistaSerializer(serializers.ModelSerializer):
    class Meta:
        model= RolVista
        fields= '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields= '__all__'

class UsuarioRolSerializer(serializers.ModelSerializer):
    class Meta:
        model= UsuarioRol
        fields= '__all__'

class VistaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vista
        fields= '__all__'

class RecuperarContrasenaSerializer(serializers.ModelSerializer):
    class Meta:
        model= RecuperarContrasena
        fields= '__all__'

class CuestionarioSerializers(serializers.ModelSerializer):
    class Meta:
        model= Cuestionario
        fields= '__all__'

class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Preguntas
        fields= '__all__'

class RespuestasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Respuestas
        fields= '__all__'

class ProcesoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Proceso
        fields='__all__'

class DesercionesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Deserciones
        fields= '__all__'

class UsuarioLoginSerializer(serializers.Serializer):
    correo = serializers.EmailField()
    contrasena = serializers.CharField(write_only=True)
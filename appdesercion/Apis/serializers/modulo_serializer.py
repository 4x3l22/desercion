from rest_framework import serializers
from appdesercion.models import Modulo

class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = '__all__'
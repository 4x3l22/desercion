from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from appdesercion.models import Modulo
from appdesercion.Apis.serializers.modulo_serializer import ModuloSerializer

class ModuloViewSet(viewsets.ModelViewSet):
    queryset = Modulo.objects.filter(estado=True)  # Filtra solo los activos
    serializer_class = ModuloSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.estado = False
        instance.fechaElimino = timezone.now()
        instance.save()
        return Response({"message": "Módulo eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)

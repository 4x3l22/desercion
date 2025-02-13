from django.db import models
from django.utils import timezone
from appdesercion.models import Usuario

class RecuperarContrasena(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='recuperaciones')
    codigo = models.CharField(max_length=6)
    expiracion = models.DateTimeField()
    usado = models.BooleanField(default=False)

    def __str__(self):
        return f"Recuperación de {self.usuario.correo}"
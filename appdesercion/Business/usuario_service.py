import logging
import random
from datetime import timedelta
from django.utils.timezone import now
from appdesercion.models import RecuperarContrasena, Usuario
from appdesercion.ulits.email_utils import EmailService

logger = logging.getLogger(__name__)

class UsuarioService:
    @staticmethod
    def solicitar_recuperacion(email: str) -> bool:
        """
        Genera un código de recuperación y lo envía por correo.
        """
        try:
            usuario = Usuario.objects.get(correo=email)
        except Usuario.DoesNotExist:
            logger.error("❌ Usuario no encontrado para recuperación: %s", email)
            return False

        # Genera un código de recuperación aleatorio
        codigo = str(random.randint(100000, 999999))
        expiracion = now() + timedelta(minutes=15)

        # Guarda el código en la base de datos
        RecuperarContrasena.objects.create(
            usuario=usuario,
            codigo=codigo,
            expiracion=expiracion,
            usado=False
        )

        # Envía el código por correo
        try:
            EmailService.send_password_reset_email(email, codigo)
            logger.info("📧 Código de recuperación enviado a %s", email)
            return True
        except Exception as e:
            logger.error("❌ Error al enviar el código de recuperación a %s: %s", email, str(e))
            return False

    @staticmethod
    def validar_codigo(email: str, codigo: str) -> bool:
        """
        Valida el código de recuperación.
        """
        try:
            usuario = Usuario.objects.get(correo=email)
            recuperacion = RecuperarContrasena.objects.filter(
                usuario=usuario,
                codigo=codigo,
                usado=False,
                expiracion__gte=now()  # Verifica que el código no haya expirado
            ).first()

            if recuperacion:
                # Marca el código como usado
                recuperacion.usado = True
                recuperacion.save()
                return True
            else:
                return False
        except Usuario.DoesNotExist:
            logger.error("❌ Usuario no encontrado: %s", email)
            return False

    @staticmethod
    def cambiar_contrasena(email: str, nueva_contrasena: str) -> bool:
        """
        Cambia la contraseña del usuario.
        """
        try:
            usuario = Usuario.objects.get(correo=email)
            usuario.contrasena = make_password(nueva_contrasena)
            usuario.save()
            return True
        except Usuario.DoesNotExist:
            logger.error("❌ Usuario no encontrado: %s", email)
            return False
from django.core.mail import send_mail
from django.conf import settings
from django.utils.timezone import now, timedelta
import random
from appdesercion.models import RecuperarContrasena, Usuario


class EmailService:
    @staticmethod
    def send_welcome_email( email: str) -> bool:
        """
        Envía un correo de bienvenida con el nombre del usuario.
        """
        subject = "Bienvenido a nuestra plataforma"
        message = f"Hola {email}, gracias por registrarte en nuestra plataforma. ¡Disfruta el servicio!"
        sender = settings.DEFAULT_FROM_EMAIL
        recipient = [email]

        try:
            send_mail(subject, message, sender, recipient)
            print(f"📧 Correo de bienvenida enviado a {email}")
            return True
        except Exception as e:
            print(f"❌ Error al enviar correo de bienvenida a {email}: {str(e)}")
            return False

    @staticmethod
    def send_password_reset_email(email, codigo):
        subject = "Recuperación de contraseña"
        message = f"""
        Hola,

        Has solicitado recuperar tu contraseña. Utiliza el siguiente código para restablecerla:

        {codigo}

        Este código expirará en 5 minutos.

        Si no solicitaste este cambio, por favor ignora este correo.

        Saludos,
        El equipo de soporte
        """
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]

        try:
            send_mail(subject, message, from_email, recipient_list)
            return True
        except Exception as e:
            print(f"Error al enviar correo de recuperación: {str(e)}")
            return False
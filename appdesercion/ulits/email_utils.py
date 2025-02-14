from django.core.mail import EmailMultiAlternatives  # Para enviar correos con HTML
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class EmailService:
    @staticmethod
    def send_welcome_email(email: str) -> bool:
        """
        Envía un correo de bienvenida con una plantilla HTML.
        """
        subject = "Bienvenido a nuestra plataforma"
        html_message = render_to_string('emails/welcome_email.html', {'email': email})
        plain_message = strip_tags(html_message)  # Versión en texto plano
        sender = settings.DEFAULT_FROM_EMAIL
        recipient = [email]

        try:
            email = EmailMultiAlternatives(
                subject,
                plain_message,
                sender,
                recipient
            )
            email.attach_alternative(html_message, "text/html")  # Adjunta el contenido HTML
            email.send()
            print(f"📧 Correo de bienvenida enviado a {email}")
            return True
        except Exception as e:
            print(f"❌ Error al enviar correo de bienvenida a {email}: {str(e)}")
            return False
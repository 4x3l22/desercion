import logging

logger = logging.getLogger(__name__)

def enviar_correo_bienvenida(correo_destino, nombre_usuario):
    asunto = 'Bienvenido a Nuestra Plataforma'
    mensaje = f'Hola {nombre_usuario},\n\nGracias por registrarte en nuestra plataforma. Esperamos que disfrutes de nuestros servicios.\n\nSaludos,\nEl Equipo de Soporte'
    correo_remitente = settings.DEFAULT_FROM_EMAIL

    try:
        send_mail(asunto, mensaje, correo_remitente, [correo_destino], fail_silently=False)
        logger.info(f'Correo enviado correctamente a {correo_destino}')
        return True
    except Exception as e:
        logger.error(f'Error al enviar el correo a {correo_destino}: {str(e)}')
        return False
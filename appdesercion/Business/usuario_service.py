import logging
from appdesercion.models import Usuario
from appdesercion.Entity.Dao.Usuario_dao import UsuarioDAO
from appdesercion.utils.email_utils import enviar_correo_bienvenida
from appdesercion.Business.base_service import BaseService

# Definir logger
logger = logging.getLogger(__name__)

class UsuarioService():
    model = Usuario
    dao = UsuarioDAO

    @classmethod
    def crear (cls, **kwargs):
        # Crear usuario
        obj = cls.model(**kwargs)
        obj.save()  # Guardar en la base de datos

        # Enviar correo de bienvenida
        try:
            print(f'Creando usuario: {obj.usuario}, Correo: {obj.correo}')
            enviar_correo_bienvenida(obj.correo, obj.usuario)
            logger.info(f'📩 Correo de bienvenida enviado a: {obj.correo}')
        except Exception as e:
            logger.error(f'❌ Error al enviar correo a {obj.correo}: {e}')

        return obj
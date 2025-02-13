from appdesercion.Entity.Dao.Usuario_dao import UsuarioDAO
from appdesercion.Entity.Dto.usuario import UsuarioDTO
from appdesercion.data.baseData import BaseData
from appdesercion.Business.usuario_service import UsuarioService  # Importamos UsuarioService

class UsuarioData(BaseData):
    dao = UsuarioDAO
    dto_class = UsuarioDTO

    
@classmethod
def crear(cls, **kwargs):
    try:
        # Crear el usuario
        obj = cls.model(**kwargs)
        obj.save()  # Guardar el usuario en la base de datos

        # Enviar correo de bienvenida
        correo_enviado = enviar_correo_bienvenida(obj.correo, obj.usuario)
        if not correo_enviado:
            logger.warning(f'No se pudo enviar el correo de bienvenida a {obj.correo}')

        logger.info(f'Usuario creado: {obj}')
        return obj
    except Exception as e:
        logger.error(f'Error al crear usuario: {str(e)}')
        raise
from datetime import datetime, timedelta
import random
from appdesercion.Business.usuario_service import UsuarioService
from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.recuperarcontrasena_dao import RecuperarContrasenaDAO
from appdesercion.models import RecuperarContrasena


class RecuperarContrasenaService(BaseService):
    model=RecuperarContrasena
    dao=RecuperarContrasenaDAO
    
    @classmethod
    def EnviarCodigo(cls, correo):
        usuario = UsuarioService.consultar_por_correo(correo)
        if usuario:
            codigo =  cls.crear(
                codigo = random.randint(1000, 9999),
                expiracion = datetime.now() + timedelta(minutes=5),
                usuario_id = usuario
            )
            
            return codigo
        
        return "No existe un usuario con ese correo."
    
    
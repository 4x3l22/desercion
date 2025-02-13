from datetime import datetime, timedelta
import random
from appdesercion.Business.usuario_service import UsuarioService
from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.recuperarcontrasena_dao import RecuperarContrasenaDAO
from appdesercion.models import RecuperarContrasena
from appdesercion.utils.email_utils import EmailService


class RecuperarContrasenaService(BaseService):
    model=RecuperarContrasena
    dao=RecuperarContrasenaDAO
    
    @classmethod
    def EnviarCodigo(cls, correo):
        usuario = UsuarioService.consultar_por_correo(correo)
        if usuario:
            obj =  cls.crear(
                codigo = random.randint(1000, 9999),
                expiracion = datetime.now() + timedelta(minutes=5),
                usuario_id = usuario
            )
            
            EmailService.send_password_reset_email(correo, obj.codigo)
            
            return obj
        
        return "No existe un usuario con ese correo."
    
    @classmethod
    def VerificarCodigo(cls, codigo, usuario_id):
        obj = cls.dao.obtener_por_codigo(codigo, usuario_id)
        if obj:
            expiracion_naive = obj.expiracion.replace(tzinfo=None)
            if expiracion_naive > datetime.now():
                cls.dao.actualizar(obj.id, usado=True)
                return obj
            else:
                obj.delete()
                return "El código ha expirado."
        
        return "Código no válido."
    
    
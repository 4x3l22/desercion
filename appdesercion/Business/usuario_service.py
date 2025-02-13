from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.Usuario_dao import UsuarioDAO
from appdesercion.Entity.Dao.rolvista_dao import RolVistaDAO
from appdesercion.models import  Usuario
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


class UsuarioService(BaseService):
    model=Usuario
    dao=UsuarioDAO

    @classmethod
    def crear(cls, **kwargs):

        if "contrasena" in kwargs:
            kwargs["contrasena"] = make_password(kwargs["contrasena"])  
            print("🔒 Contraseña hasheada:", kwargs["contrasena"])

        # Llamar al método crear de la clase base
        instance = super(UsuarioService, cls).crear(**kwargs)  
        return instance
    
    @staticmethod
    def autenticar_usuario(correo, contrasena):
        usuario = UsuarioDAO.obtener_usuario_por_correo(correo)
        
        if not usuario:
            return None 

        usuario = usuario[0]
        
        if check_password(contrasena, usuario["contrasena"]):

            vistas_rol = RolVistaDAO.obtener_vistas_por_rol(usuario["rol_id"])
            
            # Convertimos cada objeto MenuDto a un diccionario
            vistas_rol_dict = [vars(vista) for vista in vistas_rol]

            return {
                "usuario_id": usuario["usuario_id"],
                "rol_id": usuario["rol_id"], 
                "vistas_rol": vistas_rol_dict
            }
        return None  # Contraseña incorrecta

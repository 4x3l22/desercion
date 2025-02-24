from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.Usuario_dao import UsuarioDAO
from appdesercion.Entity.Dao.rolvista_dao import RolVistaDAO
from appdesercion.Entity.Dto.dto_personalizado.usuariosinrol_dto import UsuarioSinRolDTO
from appdesercion.models import  Usuario
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime
from appdesercion.utils.email_utils import EmailService 

class UsuarioService(BaseService):
    model=Usuario
    dao=UsuarioDAO

    @classmethod
    def crear(cls, **kwargs):
        """
        Crea un nuevo usuario y envía un correo de bienvenida.
        """

        # Hashear la contraseña si está presente
        if "contrasena" in kwargs:
            kwargs["contrasena"] = make_password(kwargs["contrasena"])

        # Crear la instancia del usuario
        instance = super(UsuarioService, cls).crear(**kwargs)

        # Enviar correo de bienvenida si el usuario se creó correctamente
        if instance and "correo" in kwargs:
            print(" Intentando enviar correo de bienvenida a:", kwargs["correo"])
            EmailService.send_welcome_email(kwargs["correo"])

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
                "nombre_rol": usuario["nombre_rol"],
                "vistas_rol": vistas_rol_dict
            }
        return None 
    
    @classmethod
    def actualizar(cls, id, **kwargs):
        obj = cls.obtener_por_id(id)
        if obj:
            if "contrasena" in kwargs:
                kwargs["contrasena"] = make_password(kwargs["contrasena"])

            for key, value in kwargs.items():
                setattr(obj, key, value)

            obj.fechaModifico = datetime.now()
            obj.save()
            return obj

        return None
    
    @classmethod
    def consultar_por_correo(cls, correo):
        return cls.model.objects.filter(correo=correo).first()

    @classmethod
    def listusuarios_sin_rol(cls):
        usuarios_sin_rol_query = UsuarioDAO.list_usuarios_sin_rol()

        usuarios_sin_rol = [
            UsuarioSinRolDTO(
                id=usuario['id'],
                nombres=usuario['nombres'],
                apellidos=usuario['apellidos'],
                correo=usuario['correo'],
                documento=usuario['documento'],
                tipoDocumento_nombre=usuario['tipoDocumento__nombre']
            )
            for usuario in usuarios_sin_rol_query
        ]

        return usuarios_sin_rol
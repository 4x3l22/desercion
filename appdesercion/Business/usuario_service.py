from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.Usuario_dao import UsuarioDAO
from appdesercion.models import  Usuario
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime

class UsuarioService(BaseService):
    model=Usuario
    dao=UsuarioDAO

    @classmethod
    def crear(cls, **kwargs):
        print("🔥 Método crear de UsuarioService llamado con:", kwargs)

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
            return None  # Usuario no encontrado

        usuario = usuario[0]  # Como la consulta devuelve una lista, tomamos el primer resultado
        
        if check_password(contrasena, usuario["contrasena"]):
            return {
                "id": usuario["usuario_id"],
                "rol_id": usuario["rol_id"],  # Asegúrate del nombre correcto de la columna
                "mensaje": "Autenticación exitosa"
            }
        return None  # Contraseña incorrecta
    
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

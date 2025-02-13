from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.Usuario_dao import UsuarioDAO
from appdesercion.models import Persona, Usuario
from django.contrib.auth.hashers import make_password
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

        # Obtener instancia de Persona si se pasó persona_id
        if "persona_id" in kwargs:
            try:
                kwargs["persona_id"] = Persona.objects.get(id=kwargs["persona_id"])  
            except Persona.DoesNotExist:
                raise ValueError("❌ No existe una persona con el ID proporcionado.")  

        # Llamar al método crear de la clase base
        instance = super(UsuarioService, cls).crear(**kwargs)  
        return instance
    
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

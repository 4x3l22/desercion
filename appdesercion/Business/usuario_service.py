from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.Usuario_dao import UsuarioDAO
from appdesercion.Entity.Dao.rolvista_dao import RolVistaDAO
from appdesercion.models import Usuario
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime
from appdesercion.ulits.email_utils import EmailService


class UsuarioService(BaseService):
    model = Usuario
    dao = UsuarioDAO

    @classmethod
    def crear(cls, **kwargs):
        """
        Crea un nuevo usuario y envía un correo de bienvenida.
        """
        print("🔍 kwargs recibidos:", kwargs)

        # Hashear la contraseña si está presente
        if "contrasena" in kwargs:
            print("🔑 Contraseña recibida:", kwargs["contrasena"])
            kwargs["contrasena"] = make_password(kwargs["contrasena"])
            print("🔒 Contraseña hasheada:", kwargs["contrasena"])

        # Crear la instancia del usuario
        instance = super(UsuarioService, cls).crear(**kwargs)
        print("🔍 Instancia creada:", instance)

        # Enviar correo de bienvenida si el usuario se creó correctamente
        if instance and "correo" in kwargs:
            print("📧 Intentando enviar correo de bienvenida a:", kwargs["correo"])
            EmailService.send_welcome_email(kwargs["correo"])

        return instance

    @staticmethod
    def autenticar_usuario(correo, contrasena):
        """
        Autentica un usuario y devuelve sus datos si las credenciales son válidas.
        """
        usuario = UsuarioDAO.obtener_usuario_por_correo(correo)

        if not usuario:
            return None  # Usuario no encontrado

        usuario = usuario[0]

        # Verificar la contraseña
        if check_password(contrasena, usuario["contrasena"]):
            # Obtener las vistas asociadas al rol del usuario
            vistas_rol = RolVistaDAO.obtener_vistas_por_rol(usuario["rol_id"])

            # Convertir cada objeto MenuDto a un diccionario
            vistas_rol_dict = [vars(vista) for vista in vistas_rol]

            return {
                "usuario_id": usuario["usuario_id"],
                "rol_id": usuario["rol_id"],
                "vistas_rol": vistas_rol_dict
            }

        return None  # Contraseña incorrecta

    @classmethod
    def actualizar(cls, id, **kwargs):
        """
        Actualiza los datos de un usuario existente.
        """
        obj = cls.obtener_por_id(id)
        if obj:
            # Hashear la contraseña si está presente
            if "contrasena" in kwargs:
                kwargs["contrasena"] = make_password(kwargs["contrasena"])

            # Actualizar los campos del usuario
            for key, value in kwargs.items():
                setattr(obj, key, value)

            # Actualizar la fecha de modificación
            obj.fechaModifico = datetime.now()
            obj.save()
            return obj

        return None  # Usuario no encontrado

    @classmethod
    def consultar_por_correo(cls, correo):
        """
        Consulta un usuario por su correo electrónico.
        """
        return cls.model.objects.filter(correo=correo).first()
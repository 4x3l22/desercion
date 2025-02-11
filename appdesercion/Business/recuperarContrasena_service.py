from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.recuperarcontrasena_dao import RecuperarContrasenaDAO
from appdesercion.models import RecuperarContrasena


class RecuperarContrasenaService(BaseService):
    model=RecuperarContrasena
    dao=RecuperarContrasenaDAO
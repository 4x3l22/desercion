from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.Usuario_dao import UsuarioDAO
from appdesercion.models import Usuario


class UsuarioService(BaseService):
    model=Usuario
    dao=UsuarioDAO
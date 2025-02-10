from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.usuarioRol_dao import UsuarioRolDAO
from appdesercion.models import UsuarioRol


class UsuarioRolService(BaseService):
    model=UsuarioRol
    dao=UsuarioRolDAO
from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.usuarioRol_dao import UsuarioRolDAO
from appdesercion.Entity.Dto.usuarioRol_dto import UsuarioRolDTO


class UsuarioRolService(BaseService):
    model=UsuarioRolDTO
    dao=UsuarioRolDAO
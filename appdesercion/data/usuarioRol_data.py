from appdesercion.Entity.Dao.usuarioRol_dao import UsuarioRolDAO
from appdesercion.Entity.Dto.usuarioRol_dto import UsuarioRolDTO
from appdesercion.data.baseData import BaseData


class UsuarioRolData(BaseData):
    dao=UsuarioRolDAO
    dto_class=UsuarioRolDTO
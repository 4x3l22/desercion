from appdesercion.Entity.Dao.Usuario_dao import UsuarioDAO
from appdesercion.Entity.Dto.usuario import UsuarioDTO
from appdesercion.data.baseData import BaseData


class UsuarioData(BaseData):
    dao=UsuarioDAO
    dto_class=UsuarioDTO
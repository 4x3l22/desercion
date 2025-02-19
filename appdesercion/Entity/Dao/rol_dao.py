from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.Entity.Dto.rol_dto import RolDTO
from appdesercion.models import Rol


class RolDAO(BaseDAO):
    model = Rol
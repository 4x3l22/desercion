from appdesercion.Entity.Dao.rol_dao import RolDAO
from appdesercion.Entity.Dto.rol_dto import RolDTO
from appdesercion.data.baseData import BaseData


class RolData(BaseData):
    dao=RolDAO
    dto_class=RolDTO
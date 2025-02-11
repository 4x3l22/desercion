from appdesercion.Entity.Dao.cuentionario_dao import CuentionarioDAO
from appdesercion.Entity.Dto.cuestionario_dto import CuestionarioDTO
from appdesercion.data.baseData import BaseData


class CuestionarioData(BaseData):
    dao=CuentionarioDAO
    dto_class=CuestionarioDTO
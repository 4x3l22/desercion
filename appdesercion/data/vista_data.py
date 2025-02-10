from appdesercion.Entity.Dao.vista_dao import VistaDAO
from appdesercion.Entity.Dto.vista_dto import VistaDTO
from appdesercion.data.baseData import BaseData


class Vista(BaseData):
    dao=VistaDAO
    dto_class=VistaDTO
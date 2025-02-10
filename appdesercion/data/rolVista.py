from appdesercion.Entity.Dao.rolvista_dao import RolVistaDAO
from appdesercion.Entity.Dto.rolVista_dto import RolVistaDTO
from appdesercion.data.baseData import BaseData


class RolVistaData(BaseData):
    dao=RolVistaDAO
    dto_class=RolVistaDTO
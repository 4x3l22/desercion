from appdesercion.Entity.Dao.proceso_dao import ProcesoDAO
from appdesercion.Entity.Dto.proceso_dto import ProcesoDTO
from appdesercion.data.baseData import BaseData


class ProcesoData(BaseData):
    dao=ProcesoDAO
    dto_class=ProcesoDTO
from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.proceso_dao import ProcesoDAO
from appdesercion.Entity.Dto.proceso_dto import ProcesoDTO


class ProcesoService(BaseService):
    model=ProcesoDTO
    dao=ProcesoDAO
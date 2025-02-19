from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.Entity.Dto.proceso_dto import ProcesoDTO
from appdesercion.models import Proceso


class ProcesoDAO(BaseDAO):
    model=Proceso
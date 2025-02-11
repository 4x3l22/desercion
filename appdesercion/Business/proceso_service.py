from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.proceso_dao import ProcesoDAO
from appdesercion.models import Proceso


class ProcesoService(BaseService):
    model=Proceso
    dao=ProcesoDAO
from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.vista_dao import VistaDAO
from appdesercion.Entity.Dto.vista_dto import VistaDTO


class VistaService(BaseService):
    dao=VistaDAO
    model=VistaDTO
from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.rol_dao import RolDAO
from appdesercion.Entity.Dto.vista_dto import VistaDTO


class RolService(BaseService):
    dao=RolDAO
    model=VistaDTO
from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.rolvista_dao import RolVistaDAO
from appdesercion.Entity.Dto.rolVista_dto import RolVistaDTO


class RolVistaService(BaseService):
    model=RolVistaDTO
    dao=RolVistaDAO

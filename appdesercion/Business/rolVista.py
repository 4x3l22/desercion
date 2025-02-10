from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.rolvista_dao import RolVistaDAO
from appdesercion.models import RolVista


class RolVistaService(BaseService):
    model=RolVista
    dao=RolVistaDAO
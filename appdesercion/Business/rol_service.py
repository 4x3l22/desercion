from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.rol_dao import RolDAO
from appdesercion.models import Vista


class RolService(BaseService):
    dao=RolDAO
    model=Vista
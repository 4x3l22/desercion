from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.vista_dao import VistaDAO
from appdesercion.models import Vista


class VistaService(BaseService):
    dao=VistaDAO
    model=Vista
from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.cuentionario_dao import CuentionarioDAO
from appdesercion.models import Cuestionario


class CuestionarioService(BaseService):
    model=Cuestionario
    dao=CuentionarioDAO
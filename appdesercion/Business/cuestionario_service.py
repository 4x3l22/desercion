from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.cuentionario_dao import CuentionarioDAO
from appdesercion.Entity.Dto.cuestionario_dto import CuestionarioDTO


class CuestionarioService(BaseService):
    model=CuestionarioDTO
    dao=CuentionarioDAO

    @staticmethod
    def obtener_cuestionarios(cuestionario_id):
        return CuentionarioDAO.list_cuestionarios(cuestionario_id)
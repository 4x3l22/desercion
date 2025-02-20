from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.rolvista_dao import RolVistaDAO
from appdesercion.Entity.Dto.rolVista_dto import RolVistaDTO


class RolVistaService(BaseService):
    model=RolVistaDTO
    dao=RolVistaDAO

    @classmethod
    def obtener_datos(cls):
        query = RolVistaDAO.obtener_datos()

        return [
            RolVistaDTO(
                rol_id=rolvista['rol_id'],
                nombre_rol=rolvista['nombre_rol'],
                vista_id=rolvista['vista_id'],
                nombre_vista=rolvista['nombre_vista'],
            )
            for rolvista in query
        ]
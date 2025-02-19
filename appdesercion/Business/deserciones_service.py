from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.deserciones_dto import DesercionesDAO
from appdesercion.Entity.Dto.deserciones_dto import DesercionesDTO


class DesercionesService(BaseService):
    model=DesercionesDTO
    dao=DesercionesDAO
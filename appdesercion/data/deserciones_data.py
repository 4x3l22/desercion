from appdesercion.Entity.Dao.deserciones_dto import DesercionesDAO
from appdesercion.Entity.Dto.deserciones_dto import DesercionesDTO
from appdesercion.data.baseData import BaseData


class DesercionesData(BaseData):
    dao=DesercionesDAO
    dto_class=DesercionesDTO
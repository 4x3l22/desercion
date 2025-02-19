from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.Entity.Dto.deserciones_dto import DesercionesDTO
from appdesercion.models import Deserciones


class DesercionesDAO(BaseDAO):
    model=Deserciones
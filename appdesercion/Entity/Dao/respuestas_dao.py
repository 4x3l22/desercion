from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.Entity.Dto.respuestas_dto import RespuestasDTO
from appdesercion.models import Respuesta


class RespuestasDAO(BaseDAO):
    model=Respuesta
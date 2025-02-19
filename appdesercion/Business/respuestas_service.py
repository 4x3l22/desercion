from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.respuestas_dao import RespuestasDAO
from appdesercion.Entity.Dto.respuestas_dto import RespuestasDTO


class RespuestasService(BaseService):
    model=RespuestasDTO
    dao=RespuestasDAO
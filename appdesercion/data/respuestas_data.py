from appdesercion.Entity.Dao.respuestas_dao import RespuestasDAO
from appdesercion.Entity.Dto.respuestas_dto import RespuestasDTO
from appdesercion.data.baseData import BaseData


class RespuestasData(BaseData):
    dao=RespuestasDAO
    dto_class=RespuestasDTO
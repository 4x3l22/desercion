from appdesercion.Entity.Dao.preguntas_dao import PreguntasDAO
from appdesercion.Entity.Dto.preguntas_dto import PreguntasDTO
from appdesercion.data.baseData import BaseData


class PreguntasData(BaseData):
    dao=PreguntasDAO
    dto_class=PreguntasDTO
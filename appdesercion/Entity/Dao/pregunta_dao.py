from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.Entity.Dto.pregunta_dto import PreguntaDTO
from appdesercion.models import Pregunta


class PreguntaDAO(BaseDAO):
    model = Pregunta
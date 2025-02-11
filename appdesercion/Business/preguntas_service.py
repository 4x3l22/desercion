from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.preguntas_dao import PreguntasDAO
from appdesercion.models import Preguntas


class PreguntasService(BaseService):
    model=Preguntas
    dao=PreguntasDAO
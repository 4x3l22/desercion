from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.respuestas_dao import RespuestasDAO
from appdesercion.models import Respuestas


class RespuestasService(BaseService):
    model=Respuestas
    dao=RespuestasDAO
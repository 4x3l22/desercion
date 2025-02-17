from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.pregunta_dao import PreguntaDAO
from appdesercion.models import Pregunta


class PreguntaService(BaseService):
    DAO = PreguntaDAO
    model = Pregunta
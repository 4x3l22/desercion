from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.pregunta_dao import PreguntaDAO
from appdesercion.Entity.Dto.pregunta_dto import PreguntaDTO


class PreguntaService(BaseService):
    DAO = PreguntaDAO
    model = PreguntaDTO
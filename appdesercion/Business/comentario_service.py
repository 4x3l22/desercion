from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.comentario_dao import ComentarioDAO
from appdesercion.models import Comentario


class ComentarioService(BaseService):
    model = Comentario
    dao = ComentarioDAO
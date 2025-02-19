from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.Entity.Dto.comentario_dto import ComentarioDTO
from appdesercion.models import Comentario


class ComentarioDAO(BaseDAO):
    model = Comentario
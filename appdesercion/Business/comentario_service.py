from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.comentario_dao import ComentarioDAO
from appdesercion.Entity.Dto.comentario_dto import ComentarioDTO


class ComentarioService(BaseService):
    model = ComentarioDTO
    dao = ComentarioDAO
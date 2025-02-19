from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.aprendiz_dao import AprendizDAO
from appdesercion.Entity.Dto.aprendiz_dto import AprendizDTO


class AprendizService(BaseService):
    model=AprendizDTO
    dao=AprendizDAO

    @classmethod
    def consultar_por_documento(documento):
        return AprendizDTO.objects.filter(documento=documento).first()
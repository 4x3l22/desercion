from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.aprendiz_dao import AprendizDAO
from appdesercion.Entity.Dto.aprendiz_dto import AprendizDTO
from appdesercion.models import Aprendiz


class AprendizService(BaseService):
    model=Aprendiz
    dao=AprendizDAO

    @classmethod
    def consultar_por_documento(documento):
        return Aprendiz.objects.filter(documento=documento).first()

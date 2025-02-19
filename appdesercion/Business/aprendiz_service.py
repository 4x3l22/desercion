from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.aprendiz_dao import AprendizDAO
from appdesercion.Entity.Dto.aprendiz_dto import AprendizDTO


class AprendizService(BaseService):
    model=AprendizDTO
    dao=AprendizDAO

    @classmethod
    def consultar_por_documento(documento):
<<<<<<< HEAD
        return AprendizDTO.objects.filter(documento=documento).first()
=======
        return Aprendiz.objects.filter(documento=documento).first()
>>>>>>> e16736cdfa0ceff72e88a13031abed5700e3ea13

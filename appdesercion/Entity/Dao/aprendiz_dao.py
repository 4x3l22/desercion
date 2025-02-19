from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.models import Aprendiz


class AprendizDAO(BaseDAO):
    model=Aprendiz

    @staticmethod
    def consultar_por_documento(documento):
        return Aprendiz.objects.select_related('tipoDocumento').filter(documento=documento).first()
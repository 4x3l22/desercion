from django.db.models import F

from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.Entity.Dto.vista_dto import VistaDTO
from appdesercion.models import Vista


class VistaDAO(BaseDAO):
    model = VistaDTO

    @staticmethod
    def obtener_datos():
        return Vista.objects.select_related('modulo_id').all()
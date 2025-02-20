from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.models import Respuesta


class RespuestasDAO(BaseDAO):
    model=Respuesta

    @staticmethod
    def guardar_respuestas(respuestas):
        return Respuesta.objects.bulk_create(respuestas)
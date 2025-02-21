from django.db import transaction

from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.respuestas_dao import RespuestasDAO
from appdesercion.Entity.Dto.respuestas_dto import RespuestasDTO
from appdesercion.models import Usuario, Pregunta, Aprendiz, Respuesta


class RespuestasService(BaseService):
    model=RespuestasDTO
    dao=RespuestasDAO

    @staticmethod
    def guardar_respuestas(datos):
        respuestas = []
        try:
            with transaction.atomic():
                for dato in datos:
                    usuario = Usuario.objects.get(id=dato["usuario"])
                    pregunta = Pregunta.objects.get(id=dato["pregunta"])
                    aprendiz = Aprendiz.objects.get(id=dato["aprendiz"])

                    respuesta = Respuesta.objects.create(
                        respuesta=dato["respuesta"],
                        usuario=usuario,
                        pregunta=pregunta,
                        aprendiz=aprendiz
                    )
                    respuestas.append(respuesta)

            return {"data": respuestas}
        except Exception as e:
            return {"error": str(e)}
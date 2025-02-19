from django.db import transaction

from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.respuestas_dao import RespuestasDAO
from appdesercion.Entity.Dto.respuestas_dto import RespuestasDTO
from appdesercion.models import Usuario, Pregunta, Aprendiz, Respuesta


class RespuestasService(BaseService):
    model=RespuestasDTO
    dao=RespuestasDAO

    def guardar_respuestas(datos):
        respuestas = []
        try:
            with transaction.atomic():  # Garantiza que todo se guarde correctamente
                for dato in datos:
                    usuario = Usuario.objects.get(id=dato["usuario"])
                    pregunta = Pregunta.objects.get(id=dato["pregunta"])
                    aprendiz = Aprendiz.objects.get(id=dato["aprendiz"])

                    respuesta = Respuesta(
                        respuesta=dato["respuesta"],
                        usuario=usuario,
                        pregunta=pregunta,
                        aprendiz=aprendiz
                    )
                    respuestas.append(respuesta)

                # Llama al DAO para guardar las respuestas
                RespuestasDAO.guardar_respuestas(respuestas)

            return {"data": {"message": "Respuestas guardadas correctamente."}, "status": 201}
        except Usuario.DoesNotExist:
            return {"data": {"error": "Algún usuario no existe."}, "status": 400}
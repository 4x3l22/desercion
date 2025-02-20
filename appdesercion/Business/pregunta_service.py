from django.db import transaction

from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.pregunta_dao import PreguntaDAO
from appdesercion.Entity.Dto.pregunta_dto import PreguntaDTO
from appdesercion.models import Pregunta, Cuestionario


class PreguntaService(BaseService):
    DAO = PreguntaDAO
    model = PreguntaDTO

    @staticmethod
    def save_question(datos):
        preguntas = []
        try:
            with transaction.atomic():
                for pregunta in datos:
                    cuestionario = Cuestionario.objects.get(id=pregunta["cuestionario"])
                    pregunta_obj = Pregunta.objects.create(
                        cuestionario=cuestionario,
                        texto=pregunta['texto'],
                        tipo=pregunta['tipo'],
                        opciones=pregunta['opciones']
                    )
                    preguntas.append(pregunta_obj)

            return {'data': preguntas}
        except Exception as e:
            return {"error": str(e)}
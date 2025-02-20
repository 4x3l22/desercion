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
                    # cuestionario = Cuestionario.objects.get(id=pregunta["cuestionario_id"])  # Ajuste: El modelo correcto
                    pregunta_dto = PreguntaDTO(  # Cambié el nombre para mayor claridad
                        # id=pregunta['id'],
                        cuestionario_id=pregunta['cuestionario_id'],
                        texto=pregunta['texto'],
                        tipo=pregunta['tipo'],
                        opciones=pregunta['opciones']
                    )
                    preguntas.append(pregunta_dto)  # Corregido: Se agregan los objetos DTO a la lista

                PreguntaDAO.save_question(preguntas)
            return {'data': preguntas}  # Corrección en la clave de retorno
        except Exception as e:
            return {"error": str(e)}  # Corrección en la estructura de error
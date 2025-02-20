from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.models import Pregunta


class PreguntaDAO(BaseDAO):
    model = Pregunta

    @staticmethod
    def save_question(preguntas):
        return Pregunta.objects.bulk_create(preguntas)
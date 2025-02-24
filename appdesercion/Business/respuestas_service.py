from django.db import transaction

from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.respuestas_dao import RespuestasDAO
from appdesercion.Entity.Dto.respuestas_dto import RespuestasDTO
from appdesercion.models import Usuario, Pregunta, Aprendiz, Respuesta, Proceso


class RespuestasService(BaseService):
    model=RespuestasDTO
    dao=RespuestasDAO

    @staticmethod
    def guardar_respuestas(datos):
        respuestas = []
        try:
            with transaction.atomic():
                cambiar_estado = False
                proceso = None
                for dato in datos:
                    usuario = Usuario.objects.get(id=dato["usuario"])
                    pregunta = Pregunta.objects.get(id=dato["pregunta"])

                    respuesta = Respuesta.objects.create(
                        respuesta=dato["respuesta"],
                        usuario=usuario,
                        pregunta=pregunta
                    )
                    respuestas.append(respuesta)

                    # ✅ Verificar si la respuesta empieza con "CF"
                    if dato["respuesta"].startswith("CF"):
                        cambiar_estado = True  # ✅ Se activa la bandera

                    # ✅ Obtener el proceso solo una vez
                    if not proceso:
                        cuestionario = pregunta.cuestionario
                        proceso = Proceso.objects.filter(cuestionario_id=cuestionario.id).first()

                    if proceso:
                        proceso.estado_aprobacion = "coordinadorFPI" if cambiar_estado else "coordinadorAcademico"
                        proceso.save()

            return {"data": respuestas}
        except Exception as e:
            return {"error": str(e)}
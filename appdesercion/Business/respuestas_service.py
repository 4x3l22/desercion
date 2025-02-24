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
                cambiar_estado = False  # Bandera para cambiar estado
                # print("=== Iniciando guardado de respuestas ===")
                # print(f"Datos recibidos: {datos}")

                for dato in datos:
                    # print(f"\nProcesando dato: {dato}")

                    usuario = Usuario.objects.get(id=dato["usuario"])
                    pregunta = Pregunta.objects.get(id=dato["pregunta"])
                    aprendiz = Aprendiz.objects.get(id=dato["aprendiz"])

                    respuesta = Respuesta.objects.create(
                        respuesta=dato["respuesta"],
                        usuario=usuario,
                        pregunta=pregunta,
                        aprendiz=aprendiz,
                    )
                    respuestas.append(respuesta)

                    # print(f"Respuesta guardada: {respuesta.respuesta}")

                    # ✅ Verificar si la respuesta empieza con "CF"
                    if dato["respuesta"].startswith("CF"):
                        cambiar_estado = True
                        # print("Estado cambiar_estado activado (CF detectado)")

                    # ✅ Obtener el cuestionario asociado a la pregunta
                    cuestionario = pregunta.cuestionario
                    # print(f"Cuestionario asociado: {cuestionario}")

                    # ✅ Obtener el proceso relacionado con el cuestionario y el aprendiz
                    proceso = Proceso.objects.filter(
                        cuestionario_id=cuestionario.id,
                        aprendiz_id=aprendiz.id  # 🔹 Solo el proceso del aprendiz actual
                    ).first()

                    if proceso:
                        # estado_anterior = proceso.estado_aprobacion
                        proceso.estado_aprobacion = "coordinadorFPI" if cambiar_estado else "coordinadorAcademico"
                        proceso.save()
                        # print(f"Estado del proceso cambiado de {estado_anterior} a {proceso.estado_aprobacion}")
                    else:
                        print("❌ No se encontró un proceso asociado a este aprendiz y cuestionario.")

                # print("=== Guardado de respuestas finalizado ===")
                return {"data": respuestas}

        except Exception as e:
            # print(f"❌ Error en guardar_respuestas: {str(e)}")
            return {"error": str(e)}
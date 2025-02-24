from django.db import transaction

from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.comentario_dao import ComentarioDAO
from appdesercion.Entity.Dto.comentario_dto import ComentarioDTO
from appdesercion.models import Proceso, Usuario, Comentario


class ComentarioService(BaseService):
    model = ComentarioDTO
    dao = ComentarioDAO

    @staticmethod
    def registrar_comentario(datos):
        try:
            with transaction.atomic():
                # print("=== Iniciando registro de comentario ===")
                # print(f"Datos recibidos: {datos}")

                # ✅ Obtener el proceso al que pertenece el comentario
                proceso = Proceso.objects.get(id=datos["proceso_id"])
                usuario = Usuario.objects.get(id=datos["usuario_id"])

                # ✅ Guardar el comentario
                comentario = Comentario.objects.create(
                    texto=datos["texto"],
                    usuario_id=usuario,
                    proceso_id=proceso
                )
                # print(f"✅ Comentario guardado: {comentario}")

                # ✅ Validar el estado actual del proceso y cambiarlo según las reglas
                estado_anterior = proceso.estado_aprobacion
                nuevo_estado = estado_anterior  # Mantener por defecto

                if estado_anterior == "coordinadorAcademico":
                    nuevo_estado = "instructor"
                elif estado_anterior == "coordinadorFPI":
                    nuevo_estado = "bienestar"
                elif estado_anterior == "bienestar":
                    nuevo_estado = "instructor"

                # ✅ Si el estado cambió, actualizarlo en la base de datos
                if nuevo_estado != estado_anterior:
                    proceso.estado_aprobacion = nuevo_estado
                    proceso.save()
                    # print(f"✅ Estado del proceso cambiado de {estado_anterior} a {nuevo_estado}")
                else:
                    print("⚠️ No hubo cambio en el estado del proceso.")

            # print("=== Registro de comentario finalizado ===")
            return {"data": comentario}

        except Exception as e:
            # print(f"❌ Error en registrar_comentario: {str(e)}")
            return {"error": str(e)}
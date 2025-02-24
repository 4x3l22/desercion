from dataclasses import asdict
from django.db import transaction
from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.comentario_dao import ComentarioDAO
from appdesercion.Entity.Dto.comentario_dto import ListaProcesosCuestionariosCommetDTO, QuestionCommentDTO, \
    AnswerCommentDTO
from appdesercion.models import Proceso, Usuario, Comentario


class ComentarioService(BaseService):
    model = Comentario
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

    @classmethod
    def list_comment(cls, usuario_id, approval_status):
        query = cls.dao.list_comment(usuario_id=usuario_id, approval_status=approval_status)

        comments_dict = {}

        for comment in query:
            proceso_id = comment["proceso_id"]

            if proceso_id not in comments_dict:
                comments_dict[proceso_id] = ListaProcesosCuestionariosCommetDTO(
                    proceso_id=proceso_id,
                    estado_aprobacion=comment["estado_aprobacion"],
                    correo_usuario=comment["correo_usuario"],
                    nombres_usuario=comment["nombres_usuario"],
                    apellidos_usuario=comment["apellidos_usuario"],
                    numero_documento_usuario=comment["numero_documento_usuario"],
                    nombre_aprendiz=comment["nombre_aprendiz"],
                    apellidos_aprendiz=comment["apellidos_aprendiz"],
                    documento_aprendiz=comment["documento_aprendiz"],
                    cuestionario_nombre=comment["cuestionario_nombre"],
                    cuestionario_descripcion=comment["cuestionario_descripcion"],
                    comentario=[],
                    preguntas=[]
                )
            comment_dto = comments_dict[proceso_id]

            # Agregar comentario como string directamente
            comment_dto.comentario.append(comment["comentario"])

            pregunta_id = comment["pregunta_id"]
            pregunta_existente = next((p for p in comment_dto.preguntas if p.pregunta_id == pregunta_id), None)

            if not pregunta_existente:
                pregunta_existente = QuestionCommentDTO(
                    pregunta_id=pregunta_id,
                    texto_pregunta=comment["texto_pregunta"],
                    tipo_pregunta=comment["tipo_pregunta"],
                    opciones_pregunta=comment["opciones_pregunta"],
                    respuestas=[]
                )
                comment_dto.preguntas.append(pregunta_existente)

            # Agregar la respuesta a la pregunta
            respuesta_dto = AnswerCommentDTO(
                respuesta_id=comment["respuesta_id"],
                respuesta_texto=comment["respuesta_texto"]
            )
            pregunta_existente.respuestas.append(respuesta_dto)

        # ✅ Convertir a lista de diccionarios antes de devolver
        return [asdict(dto) for dto in comments_dict.values()]
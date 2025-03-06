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
                proceso = Proceso.objects.get(id=datos["proceso_id"])
                usuario = Usuario.objects.get(id=datos["usuario_id"])

                comentario = Comentario.objects.create(
                    texto=datos["texto"],
                    estado=datos["estado"],
                    usuario_id=usuario,
                    proceso_id=proceso
                )

                estado_anterior = proceso.estado_aprobacion
                nuevo_estado = estado_anterior

                # Cambiar estado directamente si el comentario está "rechazado"
                if datos["estado"] == "rechazado":
                    nuevo_estado = "instructor"
                else:
                    # Lógica existente para otros casos
                    if estado_anterior == "coordinadorAcademico":
                        nuevo_estado = "instructor"
                    elif estado_anterior == "coordinadorFPI":
                        nuevo_estado = "bienestar"
                    elif estado_anterior == "bienestar":
                        nuevo_estado = "instructor"

                # Actualiza el estado solo si hay un cambio
                if nuevo_estado != estado_anterior:
                    proceso.estado_aprobacion = nuevo_estado
                    proceso.save()
                else:
                    print("⚠️ No hubo cambio en el estado del proceso.")

            return {"data": comentario}

        except Exception as e:
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
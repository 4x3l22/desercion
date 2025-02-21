from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.proceso_dao import ProcesoDAO
from appdesercion.Entity.Dto.dto_personalizado.listardataprocesos_dto import ListaProcesosCuestionariosDTO, QuestionDTO, \
    AnswerDTO
from appdesercion.Entity.Dto.proceso_dto import ProcesoDTO


class ProcesoService(BaseService):
    model=ProcesoDTO
    dao=ProcesoDAO

    @classmethod
    def obtener_procesos(cls):
        query = cls.dao.list_proceso()

        procesos_dict = {}

        for proc in query:
            proceso_id = proc["proceso_id"]

            # Si el proceso no existe en el diccionario, lo creamos
            if proceso_id not in procesos_dict:
                procesos_dict[proceso_id] = ListaProcesosCuestionariosDTO(
                    proceso_id=proceso_id,
                    estado_aprobacion=proc["estado_aprobacion"],
                    correo_usuario=proc["correo_usuario"],
                    nombres_usuario=proc["nombres_usuario"],
                    apellidos_usuario=proc["apellidos_usuario"],
                    numero_documento_usuario=proc["numero_documento_usuario"],
                    cuestionario_nombre=proc["cuestionario_nombre"],
                    cuestionario_descripcion=proc["cuestionario_descripcion"],
                    preguntas=[]
                )

            # Obtener el proceso actual
            proceso_dto = procesos_dict[proceso_id]

            # Verificar si la pregunta ya está en la lista
            pregunta_id = proc["pregunta_id"]
            pregunta_existente = next((p for p in proceso_dto.preguntas if p.pregunta_id == pregunta_id), None)

            if not pregunta_existente:
                pregunta_existente = QuestionDTO(
                    pregunta_id=pregunta_id,
                    texto_pregunta=proc["texto_pregunta"],
                    tipo_pregunta=proc["tipo_pregunta"],
                    opciones_pregunta=proc["opciones_pregunta"],
                    respuestas=[]
                )
                proceso_dto.preguntas.append(pregunta_existente)

            # Agregar la respuesta a la pregunta
            respuesta_dto = AnswerDTO(
                respuesta_id=proc["respuesta_id"],
                respuesta_texto=proc["respuesta_texto"]
            )
            pregunta_existente.respuestas.append(respuesta_dto)

        # Convertimos el diccionario en una lista de objetos DTO
        return list(procesos_dict.values())
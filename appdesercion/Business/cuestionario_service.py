from appdesercion.Business.base_service import BaseService
from appdesercion.Entity.Dao.cuentionario_dao import CuentionarioDAO
from appdesercion.Entity.Dto.dto_personalizado.procesos_dto import ProcesosCuestionariosDTO
from appdesercion.models import Cuestionario


class CuestionarioService(BaseService):
    model=Cuestionario
    dao=CuentionarioDAO

    @staticmethod
    def obtener_cuestionarios(cuestionario_id):
        query = CuentionarioDAO.list_cuestionarios(cuestionario_id)

        cuestionarios_dict = {}

        for questionarie in query:
            # Convertir el diccionario en un DTO para acceder como objeto
            dto = ProcesosCuestionariosDTO(
                cuestionario_id=questionarie["cuestionario_id"],
                cuestionario_nombre=questionarie["cuestionario_nombre"],
                cuestionario_descripcion=questionarie["cuestionario_descripcion"],
                preguntas=[]
            )

            cuestionario_id = dto.cuestionario_id

            # Si el cuestionario aún no está en el diccionario, lo agregamos
            if cuestionario_id not in cuestionarios_dict:
                cuestionarios_dict[cuestionario_id] = dto  # Guardamos el DTO en el diccionario

            # Agregamos la pregunta al cuestionario correspondiente
            cuestionarios_dict[cuestionario_id].preguntas.append({
                "pregunta_id": questionarie["pregunta_id"],
                "pregunta_texto": questionarie["pregunta_texto"],
                "pregunta_tipo": questionarie["pregunta_tipo"],
                "pregunta_opciones": questionarie["pregunta_opciones"]
            })

        # Convertimos el diccionario en una lista de DTOs
        return list(cuestionarios_dict.values())

    @staticmethod
    def list_all_questionnaries():
        query = CuentionarioDAO.list_all_questionnarie()

        cuestionarios_dict = {}

        for questionarie in query:
            # Convertir el diccionario en un DTO para acceder como objeto
            dto = ProcesosCuestionariosDTO(
                cuestionario_id=questionarie["cuestionario_id"],
                cuestionario_nombre=questionarie["cuestionario_nombre"],
                cuestionario_descripcion=questionarie["cuestionario_descripcion"],
                preguntas=[]
            )

            cuestionario_id = dto.cuestionario_id  # Ahora sí podemos acceder al atributo

            # Si el cuestionario aún no está en el diccionario, lo agregamos
            if cuestionario_id not in cuestionarios_dict:
                cuestionarios_dict[cuestionario_id] = dto  # Guardamos el DTO en el diccionario

            # Agregamos la pregunta al cuestionario correspondiente
            cuestionarios_dict[cuestionario_id].preguntas.append({
                "pregunta_id": questionarie["pregunta_id"],
                "pregunta_texto": questionarie["pregunta_texto"],
                "pregunta_tipo": questionarie["pregunta_tipo"],
                "pregunta_opciones": questionarie["pregunta_opciones"]
            })

        # Convertimos el diccionario en una lista de DTOs
        return list(cuestionarios_dict.values())

from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.Entity.Dto.cuestionario_dto import CuestionarioDTO
from django.db import connection


class CuentionarioDAO(BaseDAO):
    model=CuestionarioDTO

    @staticmethod
    def list_cuestionarios(cuestionario_id):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT c.id AS cuestionario_id,
                    c.nombre AS cuestionario_nombre,
                    c.descripcion AS cuestionario_descripcion,
                    p.id AS pregunta_id,
                    p.texto AS pregunta_texto,
                    p.tipo AS pregunta_tipo,
                    p.opciones AS pregunta_opciones
                FROM sena.Cuestionario AS c
                INNER JOIN sena.Pregunta AS p ON p.cuestionario_id = c.id
                WHERE c.id = %s;
            """, [cuestionario_id])
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, fila)) for fila in cursor.fetchall()]
        return results

    @staticmethod
    def list_all_questionnarie():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT c.id AS cuestionario_id,
                    c.nombre AS cuestionario_nombre,
                    c.descripcion AS cuestionario_descripcion,
                    p.id AS pregunta_id,
                    p.texto AS pregunta_texto,
                    p.tipo AS pregunta_tipo,
                    p.opciones AS pregunta_opciones
                FROM sena.Cuestionario AS c
                INNER JOIN sena.Pregunta AS p ON p.cuestionario_id = c.id
                WHERE c.fechaElimino IS NULL ;
            """)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return result
from django.db import connection

from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.models import Comentario


class ComentarioDAO(BaseDAO):
    model = Comentario

    @classmethod
    def list_comment(cls, approval_status, usuario_id):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                P.id AS proceso_id,
                P.estado_aprobacion,
                C1.texto AS comentario,
                
                U.correo AS correo_usuario,
                U.nombres AS nombres_usuario,
                U.apellidos AS apellidos_usuario,
                U.documento AS numero_documento_usuario,
                
                A.nombres As nombre_aprendiz,
                A.apellidos As apellidos_aprendiz,
                A.documento AS documento_aprendiz,
                
                C.nombre AS cuestionario_nombre,
                C.descripcion AS cuestionario_descripcion,
                
                P2.id AS pregunta_id,
                P2.texto AS texto_pregunta,
                P2.tipo AS tipo_pregunta,
                P2.opciones AS opciones_pregunta,
                
                R.id AS respuesta_id,
                R.respuesta AS respuesta_texto
                
                FROM sena.Comentario AS C1
                INNER JOIN sena.Proceso AS P ON P.id = C1.proceso_id_id
                INNER JOIN sena.Cuestionario C on P.cuestionario_id_id = C.id
                INNER JOIN sena.Pregunta P2 on C.id = P2.cuestionario_id
                LEFT JOIN sena.Respuesta R on P2.id = R.pregunta_id
                INNER JOIN sena.Usuario U on U.id = C1.usuario_id_id
                INNER JOIN sena.Aprendiz A on A.id = P.aprendiz_id
                WHERE P.estado_aprobacion = %s
                AND U.id = %s
                AND P.fechaElimino IS NULL
                AND R.aprendiz_id = P.aprendiz_id;
            """,[approval_status, usuario_id])
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return results
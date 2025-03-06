from django.db import connection


class ProcessInstructorDao:

    @staticmethod
    def process_instructor(user_id, state):
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT
            P.id AS process_id,
            P.estado_aprobacion,
            C1.texto AS comment,
            C1.estado AS comment_state,
            
            U.correo AS user_email,
            CONCAT(U.nombres, ' ',U.apellidos) AS user_name,
            U.documento AS user_document,
            
            CONCAT(A.nombres, ' ',A.apellidos) AS trainee_name,
            A.documento AS trainee_document,
            
            C.nombre AS questionnaire_name,
            C.descripcion AS questionnaire_description,
            
            P2.id AS question_id,
            P2.texto AS question_text,
            P2.tipo AS question_type,
            P2.opciones AS question_option,
            
            R.id AS reply_id,
            R.respuesta AS reply
            
            FROM sena.Comentario AS C1
            INNER JOIN sena.Proceso AS P ON P.id = C1.proceso_id_id
            INNER JOIN sena.Cuestionario C on P.cuestionario_id_id = C.id
            INNER JOIN sena.Pregunta P2 on C.id = P2.cuestionario_id
            INNER JOIN sena.Usuario U on U.id = C1.usuario_id_id
            INNER JOIN sena.Aprendiz A on A.id = P.aprendiz_id
            LEFT JOIN sena.Respuesta R on R.aprendiz_id = A.id
            WHERE P.estado_aprobacion = 'instructor'
            AND U.id = %s
            AND P.fechaElimino IS NULL
            AND C1.estado = %s
            """, [user_id, state])
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return result
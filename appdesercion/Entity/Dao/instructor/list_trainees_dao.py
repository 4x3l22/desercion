from django.db import connection


class ListTraineesDAO:

    @staticmethod
    def list_for_instructor(id_instructor):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                A.id AS ID_trainees,
                CONCAT(A.nombres, ' ', A.apellidos) AS trainees_name,
                A.documento AS trainees_document,
                A.correo AS trainees_email,
                C.nombre AS trainees_process
                FROM Proceso P
                INNER JOIN sena.Aprendiz A on P.aprendiz_id = A.id
                LEFT JOIN sena.Cuestionario C on P.cuestionario_id_id = C.id
                WHERE usuario_id_id = %s;
            """, [id_instructor])
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return results
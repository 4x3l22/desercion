from django.db import connection

from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.models import Proceso


class ProcesoDAO(BaseDAO):
    model=Proceso


    @staticmethod
    def list_proceso(approved_status):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    P.id AS proceso_id,
                    P.estado_aprobacion,
                    
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
                FROM sena.Proceso AS P
                INNER JOIN sena.Cuestionario C on P.cuestionario_id_id = C.id
                INNER JOIN sena.Pregunta P2 on C.id = P2.cuestionario_id
                INNER JOIN sena.Respuesta R on P2.id = R.pregunta_id
                INNER JOIN sena.Usuario U on U.id = R.usuario_id
                INNER JOIN sena.Aprendiz A on A.id = P.aprendiz_id 
                WHERE P.fechaElimino IS NULL
                AND P.estado_aprobacion = %s
                AND R.aprendiz_id = P.aprendiz_id;
            """, [approved_status])
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return results

    @staticmethod
    def existe_proceso(aprendiz_id, cuestionario_id):
        return Proceso.objects.filter(aprendiz_id=aprendiz_id,cuestionario_id=cuestionario_id).exists()
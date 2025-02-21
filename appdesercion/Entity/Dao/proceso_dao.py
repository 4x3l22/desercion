from django.db import connection

from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.models import Proceso


class ProcesoDAO(BaseDAO):
    model=Proceso


    @staticmethod
    def list_proceso():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    P.id AS proceso_id,
                    P.estado_aprobacion,
                    
                    U.correo AS correo_usuario, 
                    U.nombres AS nombres_usuario, 
                    U.apellidos AS apellidos_usuario, 
                    U.documento AS numero_documento_usuario,
                    
                    C.nombre AS cuestionario_nombre, 
                    C.descripcion AS cuestionario_descripcion,
                    
                    P2.id AS pregunta_id, 
                    P2.texto AS texto_pregunta, 
                    P2.tipo AS tipo_pregunta, 
                    P2.opciones AS opciones_pregunta,
                    
                    R.id AS respuesta_id, 
                    R.respuesta AS respuesta_texto
                FROM sena.Proceso AS P
                INNER JOIN sena.Usuario U on P.usuario_id_id = U.id
                INNER JOIN sena.Cuestionario C on P.cuestionario_id_id = C.id
                INNER JOIN sena.Pregunta P2 on C.id = P2.cuestionario_id
                INNER JOIN sena.Respuesta R on P2.id = R.pregunta_id
                WHERE P.fechaElimino IS NULL
            """)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return results
from django.db import connection
from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.models import Usuario


class UsuarioDAO(BaseDAO):
    model=Usuario

    @staticmethod
    def obtener_usuario_por_correo(correo):

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT U.Id AS usuario_id, 
                U.contrasena, 
                ur.Id AS rol_id
                FROM sena.Usuario AS U
                INNER JOIN sena.UsuarioRol AS ur ON ur.usuario_id_id = U.Id
                WHERE U.correo = %s;
            """, [correo])
            columnas= [col[0] for col in cursor.description]
            resultados= [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
        return resultados
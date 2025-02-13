from django.db import connection
from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.models import Usuario


class UsuarioDAO(BaseDAO):
    model=Usuario

    @staticmethod
    def obtener_usuario_por_correo(correo):

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT U.Id, 
                U.contrasena, 
                ur.RolId
                FROM Usuario AS U
                INNER JOIN UsuarioRol AS ur ON ur.usuario_id = U.Id
                WHERE U.correo = %s;
            """, [correo])
            columnas= [col[0] for col in cursor.description]
            resultados= [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
        return resultados
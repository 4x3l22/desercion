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
                ur.rol_id_id AS rol_id
                FROM sena.Usuario AS U
                LEFT JOIN sena.UsuarioRol AS ur ON ur.usuario_id_id = U.Id
                WHERE U.correo = %s;
            """, [correo])
            columnas= [col[0] for col in cursor.description]
            resultados= [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
        return resultados

    @staticmethod
    def list_usuarios_sin_rol():
        usuarios_sin_rol = Usuario.objects.filter(usuariorol__isnull=True).distinct()
        return usuarios_sin_rol
from django.db import connection
from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.models import RolVista


class RolVistaDAO(BaseDAO):
    model=RolVista

    @staticmethod
    def obtener_vistas_por_rol(rol_id):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    v.Nombre AS nombreVista, 
                    m.Nombre AS nombreModulo, 
                    v.Id AS vistaId,
                    m.Id AS moduloId,
                    m.Items AS moduloIconos,
                    v.Items AS vistaIconos,
                    v.Ruta AS RutaVista
                FROM Rols AS r 
                INNER JOIN RolVistas AS rv ON rv.RolId = r.Id
                INNER JOIN Vistas AS v ON v.Id = rv.VistaId
                INNER JOIN Modulos AS m ON m.Id = v.ModuloId
                WHERE r.Id = %s;
            """, [rol_id])
            columnas = [col[0] for col in cursor.description]
            resultados = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
        return resultados
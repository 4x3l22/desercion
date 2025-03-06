from django.db import connection
from django.db.models import F

from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.Entity.Dto.menu_dto import MenuDto
from appdesercion.Entity.Dto.rolVista_dto import RolVistaDTO
from appdesercion.models import RolVista


class RolVistaDAO(BaseDAO):
    model=RolVista

    @staticmethod
    def obtener_vistas_por_rol(rol_id):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                   v.nombre AS nombreVista, 
                    m.nombre AS nombreModulo, 
                    v.Id AS vistaId,
                    m.Id AS moduloId,
                    m.icono AS moduloIconos,
                    v.icono AS vistaIconos,
                    v.ruta AS RutaVista
                FROM sena.Rol AS r 
                INNER JOIN sena.RolVista AS rv ON rv.rol_id_id = r.Id
                INNER JOIN sena.Vista AS v ON v.Id = rv.vista_id_id
                INNER JOIN sena.Modulo AS m ON m.Id = v.modulo_id_id
                WHERE r.Id = %s
                AND rv.fechaElimino IS NULL
                ORDER BY nombreVista ASC;
            """, [rol_id])
            columnas = [col[0] for col in cursor.description]
            resultados = [MenuDto(**dict(zip(columnas, fila))) for fila in cursor.fetchall()]
        return resultados

    @staticmethod
    def obtener_datos():
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT RV.id AS rolvista_id,
                    R.id AS rol_id,
                    R.nombre AS nombre_rol,
                   V.id AS vista_id,
                   V.nombre AS nombre_vista
                FROM sena.RolVista AS RV
                INNER JOIN sena.Rol AS R on RV.rol_id_id = R.id
                INNER JOIN sena.Vista AS V on RV.vista_id_id = V.id
                WHERE RV.fechaElimino IS NULL 
            """)
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return result
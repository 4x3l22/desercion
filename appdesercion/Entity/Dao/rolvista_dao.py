from django.db import connection
from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.Entity.Dto.menu_dto import MenuDto
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
                FROM Sena1.Rol AS r 
                INNER JOIN Sena1.RolVista AS rv ON rv.rol_id_id = r.Id
                INNER JOIN Sena1.Vista AS v ON v.Id = rv.vista_id_id
                INNER JOIN Sena1.Modulo AS m ON m.Id = v.modulo_id_id
                WHERE r.Id = %s;
            """, [rol_id])
            columnas = [col[0] for col in cursor.description]
            resultados = [MenuDto(**dict(zip(columnas, fila))) for fila in cursor.fetchall()]
        return resultados
from django.db import connection
from django.db.models import F

from appdesercion.Entity.Dao.base_dao import BaseDAO
from appdesercion.Entity.Dto.menu_dto import MenuDto
from appdesercion.Entity.Dto.rolVista_dto import RolVistaDTO
from appdesercion.models import RolVista


class RolVistaDAO(BaseDAO):
    model=RolVistaDTO

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
                WHERE r.Id = %s;
            """, [rol_id])
            columnas = [col[0] for col in cursor.description]
            resultados = [MenuDto(**dict(zip(columnas, fila))) for fila in cursor.fetchall()]
        return resultados

    @staticmethod
    def obtener_datos():
        return RolVista.objects.select_related('vista', 'rol').annotate(
            vista_rol=F('rol_id__nombre'),
            vista_nombre=F('vista_id__nombre')
        ).values(
            "id", "rol_id_id", "vista_rol", "vista_id_id", "vista_nombre"
        )
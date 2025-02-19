from dataclasses import dataclass

from appdesercion.Entity.Dao.base_dao import BaseDAO


@dataclass
class ProcesosCuestionariosDTO():
    cuestionario_id: int
    cuestionario_nombre: str
    cuestionario_descripcion: str
    pregunta_id: int
    pregunta_texto: str
    pregunta_tipo: str
    pregunta_opciones: list
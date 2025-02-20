from dataclasses import dataclass, field
from typing import List


@dataclass
class ProcesosCuestionariosDTO():
    cuestionario_id: int
    cuestionario_nombre: str
    cuestionario_descripcion: str
    preguntas: List[dict] = field(default_factory=list)
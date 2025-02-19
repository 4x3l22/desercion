from dataclasses import dataclass
from datetime import datetime
from typing import List

from appdesercion.Entity.Dto.pregunta_dto import PreguntaDTO


@dataclass
class CuestionarioDTO:
    id=int
    nombre= str
    descripcion= str
    usuario_id= str
    preguntas= List[PreguntaDTO]
    fechaCreo= datetime
    fechaModifico= datetime | None
    fechaElimino= datetime | None
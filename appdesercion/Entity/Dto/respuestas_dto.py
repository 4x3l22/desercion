from dataclasses import dataclass
from datetime import datetime


@dataclass
class RespuestasDTO:
    id=int
    pregunta_id= int
    usuario_id= int
    aprendiz_id= int
    respuestas= str
    fechaCreo= datetime
    fechaModifico= datetime | None
    fechaElimino= datetime | None
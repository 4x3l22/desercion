from dataclasses import dataclass
import datetime


@dataclass
class RespuestasDTO:
    id=int
    cuestionario_id=int
    respuestas=str
    estado= bool
    fechaCreo= datetime
    fechaModifico= datetime | None
    fechaElimino= datetime | None
from datetime import datetime
from dataclasses import dataclass


@dataclass
class ComentarioDTO:
    id= int
    proceso_id= int
    usuario_id= int
    texto= str
    fechaCreo= datetime
    fechaModificado= datetime | None
    fechaElimino= datetime | None
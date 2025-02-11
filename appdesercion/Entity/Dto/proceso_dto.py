from dataclasses import dataclass
import datetime


@dataclass
class ProcesoDTO:
    id=intestado= bool
    texto= str
    usuario_id= int
    cuestionario_id=int
    estado= bool
    fechaCreo= datetime
    fechaModifico= datetime | None
    fechaElimino= datetime | None
from dataclasses import dataclass
import datetime


@dataclass
class CuestionarioDTO:
    id=int
    nombre_cuestionario= str
    descripcion= str
    usuario_id= str
    estado= bool
    fechaCreo= datetime
    fechaModifico= datetime | None
    fechaElimino= datetime | None
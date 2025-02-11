from dataclasses import dataclass
import datetime


@dataclass
class DesercionesDTO:
    id=int
    usuario_id= int
    proceso_id= int
    estado= bool
    fechaCreo= datetime
    fechaModifico= datetime | None
    fechaElimino= datetime | None

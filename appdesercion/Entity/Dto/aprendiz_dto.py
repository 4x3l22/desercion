from dataclasses import dataclass
import datetime


@dataclass
class AprendizDTO:
    id=int
    nombres= str
    apellidos= str
    documento= str
    proceso_id= int | None
    estado= bool
    fechaCreo= datetime
    fechaModifico= datetime | None
    fechaElimino= datetime | None
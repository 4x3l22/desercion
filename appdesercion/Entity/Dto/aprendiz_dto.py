from dataclasses import dataclass
from datetime import datetime


@dataclass
class AprendizDTO:
    id:int
    nombres: str
    apellidos: str
    documento: str
    estado: bool
    fechaCreo: datetime
    fechaModifico: datetime | None
    fechaElimino: datetime | None
from dataclasses import dataclass
from datetime import datetime


@dataclass
class PersonaDTO:
    id=int
    nombre=str
    apellidos=str
    ciudad=str
    documento=int
    estado: bool
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore
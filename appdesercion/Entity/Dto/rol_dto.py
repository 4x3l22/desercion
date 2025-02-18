from dataclasses import dataclass
from datetime import datetime


@dataclass   
class RolDTO:
    id: int
    nombre: str
    descripcion: str
    
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore
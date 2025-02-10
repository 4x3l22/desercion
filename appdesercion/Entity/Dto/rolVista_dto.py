from dataclasses import dataclass
from datetime import datetime


@dataclass
class RolVistaDTO:
    id: int
    rol_id: int
    vista_id: int
    estado: bool
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore
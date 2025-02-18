from dataclasses import dataclass
from datetime import datetime


@dataclass
class UsuarioRolDTO:
    id=int
    usuario_id=int
    rol_id=int
    
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore
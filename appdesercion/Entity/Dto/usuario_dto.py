from dataclasses import dataclass
from datetime import datetime


@dataclass
class UsuarioDTO:
    id=int
    usuario_id=int
    correo= str
    contrasena= str
    estado: bool
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore
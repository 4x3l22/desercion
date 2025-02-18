from dataclasses import dataclass
from datetime import datetime


@dataclass
class UsuarioDTO:
    id=int
    correo= str
    contrasena= str
    nombres= str
    apellidos= str
    tipoDocumento_id= int
    documento= int
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore

from dataclasses import dataclass
from datetime import datetime


@dataclass
class VistaDTO:
    id: int
    modulo_id: int
    nombre: str
    descripcion: str
    icono: str
    ruta: str
    estado: bool
    fechaCreo: datetime
    fechaModifico: datetime | None # type: ignore
    fechaElimino: datetime | None # type: ignore
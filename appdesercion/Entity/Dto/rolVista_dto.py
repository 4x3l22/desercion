from dataclasses import dataclass
from datetime import datetime


@dataclass
class RolVistaDTO:
    rolvista_id: int
    rol_id: int
    nombre_rol: str
    vista_id: int
    nombre_vista: str
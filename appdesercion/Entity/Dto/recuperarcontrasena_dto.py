from dataclasses import dataclass
from datetime import datetime


@dataclass
class RecuperarContrasenaDTO:
    id=int
    usuario_id=int
    codigo=int
    expiracion=datetime
    usado=bool
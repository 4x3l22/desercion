from dataclasses import dataclass
from datetime import datetime


@dataclass
class ProcesoDTO:
    id=intestado= bool
    usuario_id= int
    cuestionario_id= int
    estado_aprobacion= ['coordinadorFPI', 'coordinadorAcademico', 'Bienestar', 'Instructor']
    fechaCreo= datetime
    fechaModifico= datetime | None
    fechaElimino= datetime | None
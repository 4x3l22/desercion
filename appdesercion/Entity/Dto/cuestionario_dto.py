from dataclasses import dataclass
import datetime


@dataclass
class CuestionarioDTO:
    id=int
    nombre_cuestionario= str
    descripcion= str
    usuario_id= str
    tipo_pregunta= ['abierta', 'seleccion multiple']
    opciones_id = int
    textoopciones= str
    fechaCreo= datetime
    fechaModifico= datetime | None
    fechaElimino= datetime | None